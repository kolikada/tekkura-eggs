"""One-off: the file side of configuring the Minecraft eggs (2026-10-19).

Same rules as configure.py: text edits, upstream formatting and line endings
kept, every file parsed back before it is written.

    python tools/configure_minecraft.py
"""
import json
import pathlib
import re
import uuid

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {e["slug"]: ROOT / e["file"] for e in json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))}

# PaperMC's download API refuses requests without an identifying user agent.
USER_AGENT = "Tekkura (https://www.tekkura.cloud)"

# Tags are what the Modrinth browser reads to know the loader; the plugins or
# mods feature decides which of its two pages a server gets. Bedrock carries no
# "minecraft" tag on purpose: that tag is what offers Java content.
PLAN = {
    "minecraft-paper": (["minecraft", "paper"], ["plugins"]),
    "minecraft-vanilla": (["minecraft", "vanilla"], []),
    "minecraft-fabric": (["minecraft", "fabric"], ["mods"]),
    "minecraft-forge": (["minecraft", "forge"], ["mods"]),
    "minecraft-neoforge": (["minecraft", "neoforge"], ["mods"]),
    "minecraft-curseforge": (["minecraft", "modpack"], []),
    "minecraft-modrinth": (["minecraft", "modpack"], []),
    "minecraft-purpur": (["minecraft", "purpur", "paper"], ["plugins"]),
    # Upstream Quilt ships no features at all, so it also gets the standard Java set.
    "minecraft-quilt": (["minecraft", "quilt", "fabric"], ["eula", "java_version", "pid_limit", "mods"]),
    "minecraft-spigot": (["minecraft", "spigot"], ["plugins"]),
    "minecraft-spongevanilla": (["minecraft", "sponge"], ["plugins"]),
    "minecraft-purpur-geyser": (["minecraft", "purpur", "paper", "crossplay"], ["plugins"]),
    "minecraft-velocity": (["minecraft", "proxy", "velocity"], ["plugins"]),
    "minecraft-bungeecord": (["minecraft", "proxy", "bungeecord"], ["plugins"]),
    "minecraft-bedrock": (["bedrock"], []),
    "minecraft-pocketmine": (["bedrock", "pocketmine"], ["plugins"]),
}


def eol(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def set_list(text: str, key: str, items: list[str]) -> str:
    """Replace a top-level list (tags, features), in whichever format the file uses."""
    nl = eol(text)
    if text.lstrip().startswith("{"):
        body = f",{nl}".join(f'        "{i}"' for i in items)
        new = f'"{key}": [{nl}{body}{nl}    ]' if items else f'"{key}": []'
        text, n = re.subn(rf'"{key}": \[[^\]]*\]', lambda _: new, text, count=1)
    else:
        body = "".join(f"  - {i}{nl}" for i in items)
        text, n = re.subn(rf"^{key}:(?: \[\]| null)?\r?\n(?:  - .*\r?\n)*", lambda _: f"{key}:{nl}{body}", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"{key} not found")
    return text


def current_list(egg: dict, key: str) -> list[str]:
    return list(egg.get(key) or [])


def default_for(text: str, env: str, value: str) -> str:
    """Set a variable's default_value, JSON or YAML."""
    m = re.search(rf'(env_variable"?: ?"?){re.escape(env)}\b', text)
    if not m:
        raise SystemExit(f"{env} not found")
    tail = text[m.end():]
    tail, n = re.subn(r'(default_value"?: ?)(""|\'\')', lambda d: d.group(1) + json.dumps(value), tail, count=1)
    if n != 1:
        raise SystemExit(f"{env}: empty default not found")
    return text[: m.end()] + tail


def new_uuid(text: str) -> str:
    text, n = re.subn(r'("uuid": "|\nuuid: )[0-9a-f-]{36}', lambda m: m.group(1) + str(uuid.uuid4()), text, count=1)
    if n != 1:
        raise SystemExit("uuid not found")
    return text


def geyser_port(text: str) -> str:
    """Point Geyser's Bedrock listener at the server's own port (UDP side).

    Geyser defaults to 19132 whatever the server's port is, so without this a
    Bedrock player could not reach it. Wings writes the key before every start.
    The egg keeps its config files as a JSON string inside the JSON, so the inner
    value is decoded, extended and encoded back in place.
    """
    old = json.loads(text)["config"]["files"]
    raw_old = json.dumps(old)[1:-1]
    if text.count(raw_old) != 1:
        raise SystemExit("geyser config block not found")
    inner = json.loads(old)
    inner["plugins/Geyser-Spigot/config.yml"] = {
        "parser": "yaml",
        "find": {"bedrock.port": "{{server.allocations.default.port}}"},
    }
    new = json.dumps(inner, indent=4).replace("\n", "\r\n")
    return text.replace(raw_old, json.dumps(new)[1:-1])


for slug, (tags, extra_features) in PLAN.items():
    path = FILES[slug]
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    egg = json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)

    text = new_uuid(text)
    text = set_list(text, "tags", tags)
    features = current_list(egg, "features")
    text = set_list(text, "features", features + [x for x in extra_features if x not in features])
    if slug in ("minecraft-paper", "minecraft-velocity"):
        text = default_for(text, "USER_AGENT", USER_AGENT)
    if slug == "minecraft-purpur-geyser":
        text = geyser_port(text)

    parsed = json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)
    assert parsed["tags"] == tags, (slug, parsed["tags"])
    if slug == "minecraft-purpur-geyser":
        assert "plugins/Geyser-Spigot/config.yml" in json.loads(parsed["config"]["files"])
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("edited", slug, parsed["tags"], parsed["features"])
