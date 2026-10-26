# Python bot

Store category: **Bots** (runtime)
Upstream: [generic/python/egg-python-generic.yaml](https://github.com/pelican-eggs/generic/blob/eec3d4b153ccb8b901905b486f29d4d199154f5b/python/egg-python-generic.yaml)
Format: `PLCN_v3`
Status: **todo**

Python 3.13 by default, 3.10 to 3.14 offered; 3.7 to 3.9 dropped (end of life). Running is the entrypoint's `container~ ` line. Upstream's install checked for requirements.txt while installing REQUIREMENTS_FILE; fixed. Kind bot: no ports by default (required_ports 0 needs the panel's bot kind first, see the panel's docs/PLATFORM-PLAN.md), the web port add-on brings one. With no repository the install leaves a placeholder that prints what to do and idles, so a store order starts and reads Running. Setting GIT_ADDRESS reinstalls by itself (reinstall) and the placeholder is removed first. Checked in Docker on the real images 2026-10-26: no repo, then repo set and reinstalled. Not on the panel yet.

## To configure

- [ ] Ports tab on the panel: no ports unless the plan sells a web port
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Python 3.13: `ghcr.io/pelican-eggs/yolks:python_3.13`
- Python 3.14: `ghcr.io/pelican-eggs/yolks:python_3.14`
- Python 3.12: `ghcr.io/pelican-eggs/yolks:python_3.12`
- Python 3.11: `ghcr.io/pelican-eggs/yolks:python_3.11`
- Python 3.10: `ghcr.io/pelican-eggs/yolks:python_3.10`

## Startup

```sh
[Default] if [[ -d .git ]] && [[ "{{AUTO_UPDATE}}" == "1" ]]; then git pull; fi; if [[ ! -z "{{PY_PACKAGES}}" ]]; then pip install -U --prefix .local {{PY_PACKAGES}}; fi; if [[ -f /home/container/${REQUIREMENTS_FILE} ]]; then pip install -U --prefix .local -r ${REQUIREMENTS_FILE}; fi; /usr/local/bin/python /home/container/{{PY_FILE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `GIT_ADDRESS` |   | yes | nullable\|string |
| `BRANCH` |   | yes | nullable\|string |
| `USER_UPLOAD` | 0 | yes | required\|boolean |
| `AUTO_UPDATE` | 0 | yes | required\|boolean |
| `PY_FILE` | app.py | yes | required\|string\|max:64\|regex:/^[A-Za-z0-9_.\/-]+$/ |
| `PY_PACKAGES` |   | yes | nullable\|string |
| `USERNAME` |   | yes | nullable\|string |
| `ACCESS_TOKEN` |   | yes | nullable\|string |
| `REQUIREMENTS_FILE` | requirements.txt | yes | required\|string |
