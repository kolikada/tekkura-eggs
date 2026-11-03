"""One-off: give every game a variable for the name players see (2026-11-03).

The panel fills that variable with the server's own name (App\\Support\\GameServerName),
so a customer who never opens Settings is not left on the game's default. Games
that already have one need nothing here. Terraria and Necesse have no server list
to show a name in, so they are left alone.

Same rules as configure.py: text edits, formatting and line endings kept, every
file parsed back before it is written.

    python tools/configure_names.py
"""
import json
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {e["slug"]: ROOT / e["file"] for e in json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))}

NAME = "{{server.environment.SERVER_NAME}}"
PROPERTIES = {"server.properties": {"motd": NAME}}

JAVA = [
    "minecraft-vanilla", "minecraft-paper", "minecraft-fabric", "minecraft-forge", "minecraft-neoforge",
    "minecraft-curseforge", "minecraft-modrinth", "minecraft-purpur", "minecraft-quilt", "minecraft-spigot",
    "minecraft-spongevanilla", "minecraft-spongeforge", "minecraft-purpur-geyser", "minecraft-pocketmine",
]

SERVER_LIST = "The name players see in their server list. Written at every start, so change it here."

# slug: (default, description, {file: {find: replace}}, parser for a new file)
PLAN = {
    **{slug: ("A Minecraft Server", SERVER_LIST, PROPERTIES, None) for slug in JAVA},
    "minecraft-bungeecord": ("A Minecraft Server", SERVER_LIST, {"config.yml": {"listeners[0].motd": NAME}}, None),
    "minecraft-velocity": ("A Velocity Server", SERVER_LIST, {"velocity.toml": {"motd = ": f'motd = "{NAME}"'}}, None),
    "left-4-dead-2": (
        "Tekkura Left 4 Dead 2 Server", SERVER_LIST,
        {"left4dead2/cfg/server.cfg": {"hostname ": f'hostname "{NAME}"'}}, "file",
    ),
    "hytale": ("Hytale Server", SERVER_LIST, {"Server/config.json": {"ServerName": NAME}}, "json"),
    "arma-3": ("Arma 3 Server", SERVER_LIST, {"server.cfg": {"hostname =": f'hostname = "{NAME}";'}}, None),
}

# Project Zomboid's SERVER_NAME is its save and its .ini; the public name is a line
# inside that .ini, and the startup writes it the way it writes MaxPlayers. So no
# `/ & " $` or backtick, which would break that line.
ZOMBOID_RULES = ["required", "string", "max:64", 'not_regex:/[\\/&"$`\\\\]/']
# Raw JSON text, where `/` is written `\/` and `"` is written `\"`.
ZOMBOID_FIND = r'MaxPlayers=${MAX_PLAYERS}\/\" \".cache\/Server\/${SERVER_NAME}.ini\"; fi'
ZOMBOID_NEW = (
    r'MaxPlayers=${MAX_PLAYERS}\/\" \".cache\/Server\/${SERVER_NAME}.ini\"; '
    r'sed -i -E \"s\/^PublicName=.*\/PublicName=${PUBLIC_NAME}\/\" \".cache\/Server\/${SERVER_NAME}.ini\"; fi'
)


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def add_variable(text: str, env: str, title: str, default: str, description: str, rules: list[str]) -> str:
    nl = "\r\n" if "\r\n" in text else "\n"
    if text.lstrip().startswith("{"):
        block = json.dumps(
            {"name": title, "description": description, "env_variable": env, "default_value": default,
             "user_viewable": True, "user_editable": True, "rules": rules, "sort": 0},
            indent=4, ensure_ascii=False,
        )
        block = nl.join("        " + line for line in block.split("\n"))
        text, n = re.subn(r'("variables": \[\r?\n)', lambda m: f"{m.group(1)}{block},{nl}", text, count=1)
    else:
        lines = [
            "  -", f"    name: {yaml_quote(title)}", f"    description: {yaml_quote(description)}",
            f"    env_variable: {env}", f"    default_value: {yaml_quote(default)}",
            "    user_viewable: true", "    user_editable: true", "    rules:",
            *[f"      - {yaml_quote(rule)}" for rule in rules], "    sort: 0",
        ]
        block = "".join(line + nl for line in lines)
        text, n = re.subn(r"^(variables:\r?\n)", lambda m: m.group(1) + block, text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"variables not found for {env}")
    return text


def add_config(text: str, config: dict, parser: str | None) -> str:
    if text.lstrip().startswith("{"):
        # The whole of config.files is one JSON string on one line.
        match = re.search(r'"files": ("(?:[^"\\]|\\.)*")', text)
        if match is None:
            raise SystemExit("config.files not found")
        files = json.loads(json.loads(match.group(1)) or "{}")
        for name, find in config.items():
            entry = files.setdefault(name, {"parser": parser, "find": {}})
            entry["find"] = {**find, **entry["find"]}
        encoded = json.dumps(json.dumps(files, indent=4, ensure_ascii=False), ensure_ascii=False)
        return text[:match.start(1)] + encoded + text[match.end(1):]

    nl = "\r\n" if "\r\n" in text else "\n"
    for name, find in config.items():
        lines = "".join(f"        {yaml_quote(k)}: {yaml_quote(v)}{nl}" for k, v in find.items())
        pattern = rf"(    {re.escape(name)}:\r?\n      parser: \w+\r?\n      find:\r?\n)"
        text, n = re.subn(pattern, lambda m: m.group(1) + lines, text, count=1)
        if n == 1:
            continue
        # A file the egg did not look after until now.
        new = f"  files:{nl}    {yaml_quote(name)}:{nl}      parser: {parser}{nl}      find:{nl}{lines}"
        text, n = re.subn(r"^  files: \{\}\r?\n", lambda _: new, text, count=1, flags=re.M)
        if n != 1:
            raise SystemExit(f"config not found for {name}")
    return text


def load(path: pathlib.Path, text: str) -> dict:
    return json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)


def write(path: pathlib.Path, text: str) -> None:
    load(path, text)
    path.write_bytes(text.encode("utf-8"))


def files_of(egg: dict) -> dict:
    files = egg["config"]["files"]
    return json.loads(files) if isinstance(files, str) else files


def main() -> None:
    for slug, (default, description, config, parser) in PLAN.items():
        path = FILES[slug]
        text = path.read_bytes().decode("utf-8")
        if any(v["env_variable"] == "SERVER_NAME" for v in load(path, text)["variables"]):
            print("already done", slug)
            continue
        text = add_variable(text, "SERVER_NAME", "Server Name", default, description, ["required", "string", "max:60"])
        text = add_config(text, config, parser)
        write(path, text)

        egg = load(path, text)
        for name, find in config.items():
            missing = set(find) - set(files_of(egg)[name]["find"])
            if missing:
                raise SystemExit(f"{slug}: {missing} did not land in {name}")
        print("done", slug)

    path = FILES["project-zomboid"]
    text = path.read_bytes().decode("utf-8")
    if any(v["env_variable"] == "PUBLIC_NAME" for v in load(path, text)["variables"]):
        print("already done project-zomboid")
        return
    if text.count(ZOMBOID_FIND) != 1:
        raise SystemExit("project-zomboid: startup line not found")
    text = text.replace(ZOMBOID_FIND, ZOMBOID_NEW)
    text = add_variable(text, "PUBLIC_NAME", "Public Name", "My PZ Server", SERVER_LIST, ZOMBOID_RULES)
    write(path, text)
    print("done project-zomboid")


if __name__ == "__main__":
    main()
