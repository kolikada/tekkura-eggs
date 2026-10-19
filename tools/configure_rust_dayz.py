"""One-off: Rust and DayZ for store orders (2026-10-19).

Rust: own UUID only; its port variables are already locked upstream.
DayZ: own UUID, and the Steam login becomes the customer's (visible, editable,
optional), as with Arma 3: its installer needs a real Steam account.

    python tools/configure_rust_dayz.py
"""
import json
import pathlib
import re
import uuid

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
STRING = r'"(?:[^"\\]|\\.)*"'


def new_uuid(text: str) -> str:
    text, n = re.subn(r'("uuid": "|\nuuid: )[0-9a-f-]{36}', lambda m: m.group(1) + str(uuid.uuid4()), text, count=1)
    assert n == 1
    return text


def rw(path: pathlib.Path, edit) -> None:
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    text = edit(text)
    json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


rw(ROOT / "eggs/rust/egg-rust.yaml", new_uuid)

STEAM = {
    "STEAM_USER": ("Steam Username", "Your own Steam login, used to download DayZ and its Workshop mods. Use a separate Steam account made for this server, with Steam Guard turned off. Workshop mods only download if that account owns DayZ. Once both are filled in, the server reinstalls by itself."),
    "STEAM_PASS": ("Steam Password", "The password for that Steam account. It is stored on the panel as entered, so never use the password of the Steam account you play on."),
}


def dayz(text: str) -> str:
    text = new_uuid(text)
    for env, (name, description) in STEAM.items():
        pattern = (r'\{\s*"name": ' + STRING + r',\s*"description": ' + STRING + r',\s*"env_variable": "' + env
                   + r'",\s*"default_value": "",\s*"user_viewable": false,\s*"user_editable": false,\s*"rules": \[?\s*"required')
        m = re.search(pattern, text)
        assert m, env
        block = m.group(0)
        new = re.sub(r'"name": ' + STRING, lambda _: '"name": ' + json.dumps(name), block, count=1)
        new = re.sub(r'"description": ' + STRING, lambda _: '"description": ' + json.dumps(description), new, count=1)
        new = new.replace('"user_viewable": false', '"user_viewable": true').replace('"user_editable": false', '"user_editable": true')
        new = new[: new.rindex('"required')] + '"nullable'
        text = text.replace(block, new)
    return text


rw(ROOT / "eggs/dayz/egg-day-z.json", dayz)

for f in ["eggs/rust/egg-rust.yaml", "eggs/dayz/egg-day-z.json"]:
    t = (ROOT / f).read_text(encoding="utf-8")
    d = json.loads(t) if f.endswith("json") else yaml.safe_load(t)
    steam = [(v["env_variable"], v["user_editable"], v["rules"]) for v in d["variables"] if v["env_variable"] in STEAM]
    print(f, d["uuid"], steam)
