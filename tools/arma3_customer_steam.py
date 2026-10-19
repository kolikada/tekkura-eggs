"""One-off: let the Arma 3 customer supply the Steam login (2026-10-19).

STEAM_USER and STEAM_PASS become visible, editable and optional. Text edits
on the variable blocks, so the diff stays readable; parsed back before writing.

    python tools/arma3_customer_steam.py
"""
import json
import pathlib
import re

PATH = pathlib.Path(__file__).resolve().parent.parent / "eggs" / "arma-3" / "egg-arma3.json"

CHANGES = {
    "STEAM_USER": (
        "Steam Username",
        "Your own Steam login, used to download Arma 3 and its Workshop mods. Use a separate Steam account "
        "made for this server, with Steam Guard turned off. Workshop mods only download if that account owns "
        "Arma 3. After entering it, reinstall the server from Settings.",
    ),
    "STEAM_PASS": (
        "Steam Password",
        "The password for that Steam account. It is stored on the panel as entered, so never use the "
        "password of the Steam account you play on.",
    ),
}

STRING = r'"(?:[^"\\]|\\.)*"'

with open(PATH, encoding="utf-8", newline="") as f:
    text = f.read()

for env, (name, description) in CHANGES.items():
    pattern = (
        r'\{\s*"name": ' + STRING + r',\s*"description": ' + STRING
        + r',\s*"env_variable": "' + env + r'",\s*"default_value": "",'
        + r'\s*"user_viewable": false,\s*"user_editable": false,\s*"rules": \[\s*"required",'
    )
    match = re.search(pattern, text)
    if match is None:
        raise SystemExit(f"{env} block not found")

    block = match.group(0)
    new = re.sub(r'"name": ' + STRING, lambda _: '"name": ' + json.dumps(name), block, count=1)
    new = re.sub(r'"description": ' + STRING, lambda _: '"description": ' + json.dumps(description), new, count=1)
    new = (new.replace('"user_viewable": false', '"user_viewable": true')
              .replace('"user_editable": false', '"user_editable": true')
              .replace('"required",', '"nullable",'))
    text = text.replace(block, new)

egg = json.loads(text)
for variable in egg["variables"]:
    if variable["env_variable"] in CHANGES:
        assert variable["user_viewable"] and variable["user_editable"] and variable["rules"][0] == "nullable", variable
        print(variable["env_variable"], variable["name"], variable["rules"])

with open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(text)
