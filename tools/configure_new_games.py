"""One-off: configure the seven games added on 2026-11-12 for store orders.

Enshrouded, 7 Days to Die, The Isle, Don't Starve Together, Garry's Mod,
Factorio and Satisfactory. The previous commit holds upstream's files as they
ship, so this commit's diff is what Tekkura changed. Same rules as the other
tools: text edits, formatting and line endings kept, every file parsed back
before it is written. Run once; a second run refuses, since every egg's uuid
has already moved.

    python tools/configure_new_games.py

What each egg gets, and why, is in its NOTES.md and in status.json.
"""
import json
import pathlib
import re
import sys
import uuid

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from configure_names import SERVER_LIST, add_variable  # noqa: E402

# configure.py runs its whole pass when imported, so its two helpers are copied here.

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = {e["slug"]: e for e in json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))}
RAW = "https://raw.githubusercontent.com/kolikada/tekkura-eggs/main/"
AUTHOR = "admin@tekkura.cloud"
NAME_RULES = ["required", "string", "max:60"]


def new_uuid(text: str) -> str:
    text, n = re.subn(r'("uuid": "|\nuuid: )[0-9a-f-]{36}', lambda m: m.group(1) + str(uuid.uuid4()), text, count=1)
    if n != 1:
        raise SystemExit("uuid not found")
    return text


def lock(text: str, env: str) -> str:
    return set_field(text, env, "user_editable", False)


def load(path: pathlib.Path, text: str) -> dict:
    return json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)


def is_json(text: str) -> bool:
    return text.lstrip().startswith("{")


def json_swap(text: str, old: str, new: str) -> str:
    """Replace the one JSON string whose value is `old`, escaped as that string was.

    Upstream files mix an escaped and a plain `/` from one value to the next, so the match is
    on the decoded value, not on a guess at how it was written."""
    hits = [m for m in re.finditer(r'"(?:[^"\\]|\\.)*"', text) if json.loads(m.group(0)) == old]
    if len(hits) != 1:
        raise SystemExit(f"expected one string {old[:60]!r}, found {len(hits)}")
    m = hits[0]
    encoded = json.dumps(new, ensure_ascii=False)
    if "\\/" in m.group(0):
        encoded = encoded.replace("/", "\\/")
    return text[: m.start()] + encoded + text[m.end() :]


def esc(text: str, value: str) -> str:
    """A value as it would be written inside a JSON string in this file."""
    out = json.dumps(value, ensure_ascii=False)[1:-1]
    return out.replace("/", "\\/") if "\\/" in text else out


def swap(text: str, old: str, new: str, count: int = 1) -> str:
    found = text.count(old)
    if found != count:
        raise SystemExit(f"expected {count} of {old[:80]!r}, found {found}")
    return text.replace(old, new)


def swap_value(text: str, old: str, new: str) -> str:
    """Replace a string value, JSON-escaped in a JSON egg, a whole line in a YAML one."""
    if is_json(text):
        return json_swap(text, old, new)
    return swap(text, old, new)


def script(path: pathlib.Path, text: str) -> str:
    return load(path, text)["scripts"]["installation"]["script"]


def edit_script(path: pathlib.Path, text: str, change) -> str:
    """Rewrite the install script through `change(script) -> script`."""
    old = script(path, text)
    new = change(old)
    if old == new:
        raise SystemExit(f"{path.name}: script unchanged")
    if is_json(text):
        return json_swap(text, old, new)
    # YAML block scalar: every line carries the block's indent.
    indent = re.search(r"\n( +)#!/bin/bash", text).group(1)
    block = lambda s: "\n".join((indent + line) if line else "" for line in s.split("\n"))  # noqa: E731
    return swap(text, block(old), block(new))


def steam_retry(appid: str):
    """The loop every SteamCMD egg got on 2026-11-03 (dddab63): Steam can fail a
    download and still exit cleanly, so check the game arrived."""

    def change(s: str) -> str:
        nl = "\r\n" if "\r\n" in s else "\n"
        lines = s.split(nl)
        at = [i for i, line in enumerate(lines) if line.lstrip().startswith("./steamcmd.sh ")]
        if len(at) != 1:
            raise SystemExit("steamcmd line not found once")
        command = re.sub(r"\s*## other flags.*$", "", lines[at[0]].strip())
        loop = [
            "## Steam can fail a download and still exit cleanly, so check the game arrived,",
            "## and fail the install if it never does rather than hand over an empty server.",
            "for STEAM_TRY in 1 2 3; do",
            f"    {command}",
            f"    grep -Eqs '\"StateFlags\"[[:space:]]+\"4\"' \"/mnt/server/steamapps/appmanifest_${{{appid}}}.acf\" && break",
            '    if [ "${STEAM_TRY}" = "3" ]; then',
            '        echo "Steam did not finish downloading the game after 3 tries."',
            "        exit 1",
            "    fi",
            '    echo "Steam did not finish downloading the game, trying again."',
            "    sleep 15",
            "done",
        ]
        return nl.join(lines[: at[0]] + loop + lines[at[0] + 1 :])

    return change


def meta(path: pathlib.Path, text: str, slug: str) -> str:
    url = RAW + SOURCES[slug]["file"]
    text = new_uuid(text)
    if is_json(text):
        text, n = re.subn(r'("update_url": )(null|"[^"]*")', lambda m: m.group(1) + '"' + esc(text, url) + '"', text, count=1)
        text, m = re.subn(r'("author": ")[^"]*(")', lambda g: g.group(1) + AUTHOR + g.group(2), text, count=1)
    else:
        text, n = re.subn(r"^(  update_url: ).*$", lambda m: m.group(1) + f"'{url}'", text, count=1, flags=re.M)
        text, m = re.subn(r"^(author: ).*$", lambda g: g.group(1) + AUTHOR, text, count=1, flags=re.M)
    if n != 1 or m != 1:
        raise SystemExit(f"{slug}: update_url or author not found")
    return text


def var_block(text: str, env: str) -> tuple[int, int]:
    """Start and end of one variable, whatever the format."""
    if is_json(text):
        m = re.search(rf'"env_variable": "{re.escape(env)}"', text)
    else:
        m = re.search(rf"^    env_variable: {re.escape(env)}\r?$", text, flags=re.M)
    if m is None:
        raise SystemExit(f"{env} not found")
    if is_json(text):
        return text.rfind("{", 0, m.start()), text.find("}", m.end()) + 1
    start = text.rfind("\n  -", 0, m.start()) + 1
    nxt = re.search(r"\n  -|\n\S", text[m.end():])
    return start, m.end() + (nxt.start() + 1 if nxt else len(text) - m.end())


def set_field(text: str, env: str, field: str, value) -> str:
    """Set one field of one variable. `value` is a Python value."""
    start, end = var_block(text, env)
    part = text[start:end]
    if is_json(text):
        rendered = json.dumps(value, ensure_ascii=False)
        if "\\/" in text:
            rendered = rendered.replace("/", "\\/")
        pattern = rf'("{field}": )(\[[^\]]*\]|"(?:[^"\\]|\\.)*"|true|false|null|-?\d+)'
        part, n = re.subn(pattern, lambda m: m.group(1) + rendered, part, count=1)
    else:
        if isinstance(value, list):
            nl = "\r\n" if "\r\n" in text else "\n"
            rendered = nl + "".join(f"      - '{v.replace(chr(39), chr(39) * 2)}'{nl}" for v in value)
            pattern = rf"^(    {field}:)(?:\s*\[[^\]]*\]\r?\n|[^\n]*\n(?:      - [^\n]*\n)*)"
            part, n = re.subn(pattern, lambda m: m.group(1) + rendered, part, count=1, flags=re.M)
        else:
            if isinstance(value, bool):
                rendered = "true" if value else "false"
            elif isinstance(value, str):
                rendered = "'" + value.replace("'", "''") + "'"
            else:
                rendered = str(value)
            pattern = rf"^(    {field}: ).*$"
            part, n = re.subn(pattern, lambda m: m.group(1) + rendered, part, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"{env}.{field} not set")
    return text[:start] + part + text[end:]


def add_var(text: str, env: str, title: str, default: str, description: str, rules: list[str], editable: bool = True) -> str:
    text = add_variable(text, env, title, default, description, rules)
    return text if editable else lock(text, env)


def set_files(text: str, files: dict) -> str:
    """Replace config.files whole. Used where upstream's needed more than a key added."""
    if is_json(text):
        match = re.search(r'"files": ("(?:[^"\\]|\\.)*")', text)
        encoded = json.dumps(json.dumps(files, indent=4, ensure_ascii=False), ensure_ascii=False)
        return text[: match.start(1)] + encoded + text[match.end(1) :]
    raise SystemExit("set_files is for JSON eggs")


def write(path: pathlib.Path, text: str) -> None:
    load(path, text)
    path.write_bytes(text.encode("utf-8"))


# ---------------------------------------------------------------------------
# Enshrouded


ENSHROUDED_JSON = """cat > $HOME/enshrouded_server.json << ENDOFFILE
{
	"name": "Enshrouded Server",
	"saveDirectory": "./savegame",
	"logDirectory": "./logs",
	"ip": "0.0.0.0",
	"gamePort": 15636,
	"queryPort": 15637,
	"slotCount": 16,
	"gameSettingsPreset": "Default",
	"userGroups": [
		{
			"name": "Admin",
			"password": "${ADMIN_PASSWORD}",
			"canKickBan": true,
			"canAccessInventories": true,
			"canEditBase": true,
			"canExtendBase": true,
			"reservedSlots": 0
		},
		{
			"name": "Friend",
			"password": "${FRIEND_PASSWORD}",
			"canKickBan": false,
			"canAccessInventories": true,
			"canEditBase": true,
			"canExtendBase": false,
			"reservedSlots": 0
		},
		{
			"name": "Guest",
			"password": "${GUEST_PASSWORD}",
			"canKickBan": false,
			"canAccessInventories": false,
			"canEditBase": false,
			"canExtendBase": false,
			"reservedSlots": 0
		}
	]
}
ENDOFFILE"""

GROUP_HELP = "Players join by typing one of the three passwords, and the one they type decides what they may do. Made for this server when it was built and written into enshrouded_server.json then; change it in that file afterwards."


def enshrouded(path: pathlib.Path, text: str) -> str:
    def change(s: str) -> str:
        # Upstream asks Steam for ${STEAM_APPID}, a variable this egg never had.
        s = swap(s, "+app_update ${STEAM_APPID}", "+app_update ${SRCDS_APPID}")
        s = steam_retry("SRCDS_APPID")(s)
        # Upstream's default file carried the same three passwords on every server.
        old = s[s.index("  cd $HOME\n  curl -sSL -o enshrouded_server.json") :]
        old = old[: old.index("\n", old.index("curl")) ]
        body = "\n".join("  " + line if line and not line.startswith(("\t", "{", "}", "ENDOFFILE")) else line for line in ENSHROUDED_JSON.split("\n"))
        return swap(s, old, body)

    text = edit_script(path, text, change)
    # Players join on the query port; gamePort is written too, for builds that still read it.
    text = swap(text, "        queryPort: '{{server.environment.QUERY_PORT}}'", "        gamePort: '{{server.build.default.port}}'\n        queryPort: '{{server.environment.QUERY_PORT}}'")
    text = set_field(text, "MAX_PLAYERS", "default_value", "16")
    text = set_field(text, "MAX_PLAYERS", "rules", ["required", "integer", "between:1,16"])
    text = set_field(text, "QUERY_PORT", "description", "Players find and join the server on this port. Set by the panel.")
    for env, title in [("GUEST_PASSWORD", "Guest password"), ("FRIEND_PASSWORD", "Friend password"), ("ADMIN_PASSWORD", "Admin password")]:
        text = add_var(text, env, f"[SERVER] {title}", "", GROUP_HELP, ["nullable", "string", "max:32"], editable=False)
    return text


# ---------------------------------------------------------------------------
# 7 Days to Die


def seven_days(path: pathlib.Path, text: str) -> str:
    text = edit_script(path, text, steam_retry("SRCDS_APPID"))
    startup = load(path, text)["startup"]
    text = swap_value(text, startup, startup.replace("-dedicated ", '-dedicated -ServerName="${SERVER_NAME}" ', 1))
    text = add_var(text, "SERVER_NAME", "Server Name", "Tekkura 7 Days to Die Server", SERVER_LIST, NAME_RULES)
    text = set_field(text, "MAX_PLAYERS", "user_editable", True)
    text = set_field(text, "MAX_PLAYERS", "rules", "required|integer|between:1,64")
    return text


# ---------------------------------------------------------------------------
# The Isle


def the_isle(path: pathlib.Path, text: str) -> str:
    text = edit_script(path, text, steam_retry("SRCDS_APPID"))
    text = set_field(text, "RCON_PASSWORD", "rules", ["nullable", "string", "max:64"])
    text = set_field(text, "RCON_PASSWORD", "description", "Made for this server when it was built. Used by RCON tools on the RCON port.")
    text = set_field(text, "RCON_PORT", "description", "Set by the panel.")
    text = set_field(text, "QUEUE_PORT", "description", "The join queue listens here. Set by the panel.")
    # Upstream's default was the words "No password", written as the password.
    text = set_field(text, "SERVER_PASSWORD", "default_value", "")
    # Upstream's links to its author's Discord on every server.
    text = set_field(text, "DISCORD", "default_value", "")
    text = set_field(text, "DISCORD", "user_editable", True)
    text = set_field(text, "PLAYER_COUNT", "default_value", "40")
    text = set_field(text, "PLAYER_COUNT", "rules", ["required", "integer", "between:1,100"])
    # Game.ini reads it, and the egg never defined it.
    text = add_var(text, "SERVER_PASSWORD_ENABLED", "Server Password Enabled", "false", "Ask players for the server password.", ["required", "string", "in:true,false"])
    return text


# ---------------------------------------------------------------------------
# Don't Starve Together


DST_INI = """## cluster configs, written here: upstream fetched GitHub's HTML page for each
## file instead of the file. The panel keeps the values it owns up to date.
if [ ! -f /mnt/server/DoNotStarveTogether/config/server/cluster.ini ]; then
cat > /mnt/server/DoNotStarveTogether/config/server/cluster.ini << 'ENDOFFILE'
[GAMEPLAY]
game_mode = survival
max_players = 8
pvp = false
pause_when_empty = true

[NETWORK]
cluster_name = Tekkura Don't Starve Together Server
cluster_description = A Tekkura hosted server
cluster_password =
cluster_intention = social
autosaver_enabled = true
enable_vote_kick = false

[MISC]
console_enabled = true

[SHARD]
shard_enabled = true
bind_ip = 127.0.0.1
master_ip = 127.0.0.1
master_port = 11001
cluster_key = dst
ENDOFFILE
fi

## master configs
echo -e "getting master configs"
mkdir -p /mnt/server/DoNotStarveTogether/config/server/Master/
if [ ! -f /mnt/server/DoNotStarveTogether/config/server/Master/server.ini ]; then
cat > /mnt/server/DoNotStarveTogether/config/server/Master/server.ini << 'ENDOFFILE'
[ACCOUNT]
encode_user_path = true

[NETWORK]
server_port = 10999

[SHARD]
is_master = true

[STEAM]
master_server_port = 27016
authentication_port = 8766
ENDOFFILE
fi

## master worldgen override
if [ ! -z ${MASTER_WORLDGEN}  ] && [ ! -f /mnt/server/DoNotStarveTogether/config/server/Master/worldgenoverride.lua ]; then
    curl -sSL ${MASTER_WORLDGEN} -o /mnt/server/DoNotStarveTogether/config/server/Master/worldgenoverride.lua
fi

## caves configs
echo -e "getting cave configs"
mkdir -p /mnt/server/DoNotStarveTogether/config/server/Caves/
## Its own Steam ports: both shards run in one container.
if [ ! -f /mnt/server/DoNotStarveTogether/config/server/Caves/server.ini ]; then
cat > /mnt/server/DoNotStarveTogether/config/server/Caves/server.ini << 'ENDOFFILE'
[ACCOUNT]
encode_user_path = true

[NETWORK]
server_port = 11000

[SHARD]
is_master = false
name = Caves
id = 1137196188

[STEAM]
master_server_port = 27017
authentication_port = 8767
ENDOFFILE
fi

## caves worldgen: without a preset the Caves shard builds a second surface.
## Upstream's default fetched GitHub's HTML page here as well.
if [ ! -f /mnt/server/DoNotStarveTogether/config/server/Caves/worldgenoverride.lua ]; then
    if [ ! -z ${CAVES_WORLDGEN} ]; then
        curl -sSL ${CAVES_WORLDGEN} -o /mnt/server/DoNotStarveTogether/config/server/Caves/worldgenoverride.lua
    else
        echo 'return { override_enabled = true, preset = "DST_CAVE" }' > /mnt/server/DoNotStarveTogether/config/server/Caves/worldgenoverride.lua
    fi
fi"""

DST_TOKEN_HELP = (
    "Your own Klei server token. The server cannot start without one. It is free: sign in at "
    "https://accounts.klei.com/account/game/servers?game=DontStarveTogether, add a server and paste "
    "its token here, then start the server."
)

DST_NO_TOKEN = (
    'if [ -z "${SERVER_TOKEN}" ]; then echo "This server needs your Klei server token before it can start. '
    'Paste it into Settings, then start the server."; exit 0; fi; '
    'printf %s "${SERVER_TOKEN}" > DoNotStarveTogether/config/server/cluster_token.txt; '
)


def dont_starve(path: pathlib.Path, text: str) -> str:
    def change(s: str) -> str:
        s = steam_retry("SRCDS_APPID")(s)
        nl = "\r\n" if "\r\n" in s else "\n"
        start = s.index("## cluster token file")
        end = s.index('echo -e "install complete"')
        body = (
            '## The token is written at every start, from Settings.' + nl
            + 'echo -e "getting cluster configs"' + nl
            + "mkdir -p /mnt/server/DoNotStarveTogether/config/server/" + nl + nl
            + DST_INI.replace("\n", nl) + nl + nl
        )
        return s[:start] + body + s[end:]

    text = edit_script(path, text, change)
    startup = load(path, text)["startup_commands"]["Default"]
    text = swap_value(text, startup, DST_NO_TOKEN + startup.replace("-port 11000", "-port {{CAVES_PORT}}"))
    files = json.loads(load(path, text)["config"]["files"])
    files["DoNotStarveTogether/config/server/cluster.ini"]["find"]["NETWORK.cluster_name"] = "{{server.environment.SERVER_NAME}}"
    files["DoNotStarveTogether/config/server/Caves/server.ini"]["find"]["NETWORK.server_port"] = "{{server.environment.CAVES_PORT}}"
    text = set_files(text, files)
    text = set_field(text, "CLUSTER_NAME", "env_variable", "SERVER_NAME")
    text = set_field(text, "SERVER_NAME", "name", "Server Name")
    text = set_field(text, "SERVER_NAME", "description", SERVER_LIST)
    text = set_field(text, "SERVER_NAME", "default_value", "Tekkura Don't Starve Together Server")
    text = set_field(text, "SERVER_NAME", "rules", NAME_RULES)
    text = set_field(text, "SERVER_TOKEN", "rules", ["nullable", "string", "max:255"])
    text = set_field(text, "SERVER_TOKEN", "description", DST_TOKEN_HELP)
    text = set_field(text, "AUTO_UPDATE", "default_value", "1")
    text = set_field(text, "MAX_PLAYERS", "default_value", "8")
    text = set_field(text, "CLUSTER_DESC", "default_value", "A Tekkura hosted server")
    for env, world in [("MASTER_WORLDGEN", "the surface"), ("CAVES_WORLDGEN", "the caves")]:
        text = set_field(text, env, "default_value", "")
        text = set_field(text, env, "description", f"Optional. A raw link to a worldgenoverride.lua for {world}, read once when the world is first built.")
    text = add_var(text, "CAVES_PORT", "Caves Port", "11000", "Players moving into the caves connect here. Set by the panel.", ["required", "integer"], editable=False)
    return text


# ---------------------------------------------------------------------------
# Garry's Mod


def garrys_mod(path: pathlib.Path, text: str) -> str:
    text = edit_script(path, text, steam_retry("SRCDS_APPID"))
    startup = load(path, text)["startup_commands"]["Default"]
    new = startup.replace("+ip 0.0.0.0 ", '+ip 0.0.0.0 +hostname "{{SERVER_HOSTNAME}}" ', 1)
    # As CS2's (5837d3f): passed only when set, so an empty value takes no argument.
    # Not ${X:+...}: the image turns its closing }} into }, and nothing starts.
    new = new.replace("+host_workshop_collection {{WORKSHOP_ID}}", '$( [ -z "$WORKSHOP_ID" ] || printf %s "+host_workshop_collection $WORKSHOP_ID" )')
    new = new.replace("+sv_setsteamaccount {{STEAM_ACC}}", '$( [ -z "$STEAM_ACC" ] || printf %s "+sv_setsteamaccount $STEAM_ACC" )')
    old_line = re.search(r"^  Default: .*$", text, flags=re.M).group(0)
    new_line = "  Default: " + "'" + new.replace("'", "''") + "'"
    if yaml.safe_load(old_line.strip())["Default"] != startup:
        raise SystemExit("gmod startup line not where expected")
    text = swap(text, old_line, new_line)
    text = add_var(text, "SERVER_HOSTNAME", "Server Name", "Tekkura Garry's Mod Server", SERVER_LIST, NAME_RULES)
    return text


# ---------------------------------------------------------------------------
# Factorio


def factorio(path: pathlib.Path, text: str) -> str:
    text = swap(text, "        token: '{{server.environment.SERVER_TOKEN}}'", "        token: '{{server.environment.SERVER_TOKEN}}'\n        visibility.public: '{{server.environment.PUBLIC_LISTING}}'")
    text = set_field(text, "MAX_SLOTS", "user_editable", True)
    text = set_field(text, "RCON_PORT", "user_editable", False)
    text = set_field(text, "RCON_PORT", "description", "RCON tools connect here once RCON is on. Set by the panel.")
    text = set_field(text, "RCON_PASSWORD", "description", "Made for this server when it was built.")
    # Upstream's placeholders would be sent to factorio.com as a login.
    text = set_field(text, "SERVER_TOKEN", "default_value", "")
    text = set_field(text, "SERVER_TOKEN", "rules", ["nullable", "alpha_num", "max:100"])
    text = set_field(text, "SERVER_USERNAME", "default_value", "")
    text = set_field(text, "SERVER_USERNAME", "rules", ["nullable", "string", "max:40"])
    text = add_var(
        text, "PUBLIC_LISTING", "Public Listing", "false",
        "List the server in Factorio's public game browser. Needs your factorio.com username and token below. Off, players join on the address.",
        ["required", "string", "in:true,false"],
    )
    return text


# ---------------------------------------------------------------------------
# Satisfactory


def satisfactory(path: pathlib.Path, text: str) -> str:
    text = edit_script(path, text, steam_retry("SRCDS_APPID"))
    text = set_field(text, "RELIABLE_PORT", "description", "Required by Satisfactory 1.1 and later. Set by the panel.")
    return text


PLAN = {
    "enshrouded": enshrouded,
    "7-days-to-die": seven_days,
    "the-isle": the_isle,
    "dont-starve-together": dont_starve,
    "garrys-mod": garrys_mod,
    "factorio": factorio,
    "satisfactory": satisfactory,
}


def main() -> None:
    for slug, configure in PLAN.items():
        path = ROOT / SOURCES[slug]["file"]
        text = path.read_bytes().decode("utf-8")
        if AUTHOR in text:
            raise SystemExit(f"{slug}: already configured")
        text = configure(path, meta(path, text, slug))
        write(path, text)
        print("configured", slug)


if __name__ == "__main__":
    main()
