"""Writes eggs/<slug>/NOTES.md and the status table in README.md.

Reads each egg as it stands, so rerun it after editing one: the notes then
show what is still left to configure rather than what upstream shipped.

    python tools/audit.py
"""
import json
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
STATUS = json.loads((ROOT / "status.json").read_text(encoding="utf-8"))

# SERVER_PORT is the one variable the daemon fills from the primary allocation.
# Any other port variable keeps the egg's default on every server built from
# it, so two servers on one node collide on it.
PORTISH = re.compile(r"(^|_)PORT(_|$)", re.I)


def load(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)


def startup(egg: dict) -> str:
    if "startup_commands" in egg:
        return "\n".join(f"[{k}] {v}" for k, v in egg["startup_commands"].items())
    return egg.get("startup", "")


def rules(var: dict) -> str:
    r = var.get("rules", "")
    return "|".join(r) if isinstance(r, list) else str(r)


def blank(value) -> bool:
    return value is None or str(value).strip() == ""


def audit(egg: dict) -> dict:
    variables = egg.get("variables") or []
    text = startup(egg)
    port_vars = [
        v for v in variables
        if PORTISH.search(v["env_variable"]) and v["env_variable"] != "SERVER_PORT"
    ]
    needs_input = [v for v in variables if "required" in rules(v) and blank(v.get("default_value"))]
    return {
        "port_vars": port_vars,
        "needs_input": needs_input,
        "startup_ports": sorted(set(re.findall(r"\{\{(\w*PORT\w*)\}\}|\$\{?(\w*PORT\w*)", text)) - {("", "")}),
        "variables": variables,
        "startup": text,
    }


def cell(text) -> str:
    text = "" if text is None else str(text)
    return text.replace("|", "\\|").replace("\n", " ")[:80] or " "


def notes(entry: dict, egg: dict, found: dict, status: dict) -> str:
    lines = [
        f"# {egg['name']}",
        "",
        f"Store category: **{entry['store_category']}** ({entry['role']})",
        f"Upstream: [{entry['repo']}/{entry['path']}]({entry['upstream']})",
        f"Format: `{egg.get('meta', {}).get('version')}`",
        f"Status: **{status.get('state', 'todo')}**",
        "",
    ]
    if status.get("note"):
        lines += [status["note"], ""]

    mapped = (status.get("ports") or {}).get("port_variables", {})
    secrets = set(status.get("secrets") or [])
    tick = lambda done: "x" if done else " "

    lines += ["## To configure", ""]
    if found["port_vars"]:
        lines.append("Port variables that keep a fixed default on every server (collide on a shared node):")
        lines.append("")
        for v in found["port_vars"]:
            env = v["env_variable"]
            how = f" (gets port {mapped[env]})" if env in mapped else ""
            lines.append(f"- [{tick(env in mapped)}] `{env}` default `{v.get('default_value')}`{how}: {cell(v.get('description'))}")
        lines.append("")
    if found["needs_input"]:
        lines.append("Required with no default (provisioning would build a server that cannot start):")
        lines.append("")
        for v in found["needs_input"]:
            env = v["env_variable"]
            how = " (generated per server)" if env in secrets else ""
            lines.append(f"- [{tick(env in secrets)}] `{env}`{how}: {cell(v.get('description'))}")
        lines.append("")
    ports = status.get("ports")
    lines += [
        f"- [{tick(ports)}] Ports tab on the panel: how many ports, and which one players connect on"
        + (f" (needs {ports['required_ports']}, connect on port {ports['connect_port_index']})" if ports else ""),
        "- [ ] Test deploy from a store order with no admin input, and a player can join",
        "",
        "## Images",
        "",
    ]
    lines += [f"- {k}: `{v}`" for k, v in (egg.get("docker_images") or {}).items()]
    lines += ["", "## Startup", "", "```sh", found["startup"], "```", "", "## Variables", "",
              "| Env | Default | Editable | Rules |", "| --- | --- | --- | --- |"]
    for v in sorted(found["variables"], key=lambda v: v.get("sort") or 0):
        lines.append(
            f"| `{v['env_variable']}` | {cell(v.get('default_value'))} | "
            f"{'yes' if v.get('user_editable') else 'no'} | {cell(rules(v))} |"
        )
    return "\n".join(lines) + "\n"


rows = []
for entry in MANIFEST:
    path = ROOT / entry["file"]
    egg = load(path)
    found = audit(egg)
    status = STATUS.get(entry["slug"], {})
    (path.parent / "NOTES.md").write_text(notes(entry, egg, found, status), encoding="utf-8")
    mapped = (status.get("ports") or {}).get("port_variables", {})
    secrets = set(status.get("secrets") or [])
    ports = ", ".join(
        f"`{v['env_variable']}`" + (" ✓" if v["env_variable"] in mapped else "") for v in found["port_vars"]
    ) or "none"
    inputs = ", ".join(
        f"`{v['env_variable']}`" + (" ✓" if v["env_variable"] in secrets else "") for v in found["needs_input"]
    ) or "none"
    rows.append(
        f"| {entry['store_category']} | [{egg['name']}](eggs/{entry['slug']}/NOTES.md) | {entry['role']} "
        f"| {ports} | {inputs} | {status.get('state', 'todo')} |"
    )

table = "\n".join([
    "| Store game | Egg | Role | Fixed port variables | Required, no default | Status |",
    "| --- | --- | --- | --- | --- | --- |",
    *rows,
])

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
start, end = "<!-- status:start -->", "<!-- status:end -->"
before, rest = text.split(start, 1)
_, after = rest.split(end, 1)
readme.write_text(f"{before}{start}\n{table}\n{end}{after}", encoding="utf-8")
print(f"{len(rows)} eggs audited")
