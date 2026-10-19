"""One-off: apply the file side of the 2026-10-19 configuration pass.

Text edits rather than load-and-dump, so each egg's diff against upstream
shows only what Tekkura changed and keeps upstream's formatting.

    python tools/configure.py
"""
import json
import pathlib
import re
import uuid

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {e["slug"]: ROOT / e["file"] for e in json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))}

TOKEN_HELP = (
    "Your own Steam Game Server Login Token. Without one the server only accepts players on its "
    "local network. Create one for free at https://steamcommunity.com/dev/managegameservers"
)


def block(text: str, env: str) -> tuple[int, int]:
    """The span of the variable whose env_variable is `env`: up to the next variable."""
    m = re.search(rf'(env_variable"?: ?"?){re.escape(env)}\b', text)
    if not m:
        raise SystemExit(f"{env} not found")
    nxt = re.search(r'env_variable"?:', text[m.end():])
    end = m.end() + (nxt.start() if nxt else len(text) - m.end())
    # Back to the start of this variable: the previous "name" key.
    start = max(text.rfind('"name"', 0, m.start()), text.rfind("- name:", 0, m.start()), text.rfind("name:", 0, m.start()))
    return start, end


def in_block(text: str, env: str, pattern: str, repl) -> str:
    start, end = block(text, env)
    part, n = re.subn(pattern, repl, text[start:end], count=1)
    if n != 1:
        raise SystemExit(f"{env}: {pattern!r} not matched")
    return text[:start] + part + text[end:]


def lock(text: str, env: str) -> str:
    return in_block(text, env, r'(user_editable"?: ?)true', r"\1false")


def optional(text: str, env: str) -> str:
    # PTDL strings ("required|string") and PLCN lists ("- required").
    return in_block(text, env, r'("rules": ")required\||(\n\s*- )required\b', lambda m: (m.group(1) or m.group(2)) + ("nullable|" if m.group(1) else "nullable"))


def new_uuid(text: str) -> str:
    text, n = re.subn(r'("uuid": "|\nuuid: )[0-9a-f-]{36}', lambda m: m.group(1) + str(uuid.uuid4()), text, count=1)
    if n != 1:
        raise SystemExit("uuid not found")
    return text


def edit(slug: str, *steps) -> None:
    path = FILES[slug]
    # newline="" keeps upstream's own line endings (some files are CRLF).
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    text = new_uuid(text)
    for step in steps:
        text = step(text)
    # Parse it back, so a bad edit fails here and not on the panel.
    json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("edited", slug)


def replace(old: str, new: str):
    def step(text: str) -> str:
        if text.count(old) != 1:
            raise SystemExit(f"expected one {old!r}, found {text.count(old)}")
        return text.replace(old, new)
    return step


for slug in ["palworld", "ark-survival-ascended", "hytale", "necesse", "left-4-dead-2", "conan-exiles",
             "sons-of-the-forest", "valheim", "valheim-bepinex", "terraria", "terraria-tmodloader",
             "terraria-tshock", "arma-reforger"]:
    edit(slug)

edit("ark-survival-evolved", lambda t: lock(t, "QUERY_PORT"))
edit("humanitz", lambda t: lock(t, "QUERY_PORT"))
edit("windrose", lambda t: lock(t, "DIRECT_CONNECTION_PORT"))

# The token is the customer's own Steam credential, so it cannot be generated.
# Optional, so the server builds and starts; passed only when set, so an empty
# value does not swallow the next argument.
edit(
    "cs2",
    lambda t: optional(t, "STEAM_GSLT"),
    replace("+sv_setsteamaccount {{STEAM_GSLT}}", "${STEAM_GSLT:++sv_setsteamaccount ${STEAM_GSLT}}"),
    replace(
        "The Steam Account Token required for the server to be displayed public. The token can be acquired\n      here: https://steamcommunity.com/dev/managegameservers",
        TOKEN_HELP,
    ),
)
edit(
    "unturned",
    lambda t: optional(t, "GSLT"),
    replace("-GSLT {{GSLT}}", "${GSLT:+-GSLT ${GSLT}}"),
    lambda t: in_block(t, "GSLT", r'("description": )""', lambda m: m.group(1) + json.dumps(TOKEN_HELP)),
)
