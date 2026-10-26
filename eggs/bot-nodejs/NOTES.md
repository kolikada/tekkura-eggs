# Node.js bot

Store category: **Bots** (runtime)
Upstream: [generic/nodejs/egg-nodejs-generic.yaml](https://github.com/pelican-eggs/generic/blob/eec3d4b153ccb8b901905b486f29d4d199154f5b/nodejs/egg-nodejs-generic.yaml)
Format: `PLCN_v3`
Status: **todo**

Node.js 24 LTS by default, 26 and 22 offered; 23 and 25 dropped (end of life). Running is the entrypoint's `:/home/container$ ` line. Kind bot: no ports by default (required_ports 0 needs the panel's bot kind first, see the panel's docs/PLATFORM-PLAN.md), the web port add-on brings one. With no repository the install leaves a placeholder that prints what to do and idles, so a store order starts and reads Running. Setting GIT_ADDRESS reinstalls by itself (reinstall) and the placeholder is removed first. Checked in Docker on the real images 2026-10-26: no repo, then repo set and reinstalled. Not on the panel yet.

## To configure

- [ ] Ports tab on the panel: no ports unless the plan sells a web port
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Node.js 24 (LTS): `ghcr.io/pelican-eggs/yolks:nodejs_24`
- Node.js 26: `ghcr.io/pelican-eggs/yolks:nodejs_26`
- Node.js 22 (LTS): `ghcr.io/pelican-eggs/yolks:nodejs_22`

## Startup

```sh
[Default] if [[ -d .git ]] && [[ {{AUTO_UPDATE}} == "1" ]]; then git pull; fi; if [[ ! -z ${NODE_PACKAGES} ]]; then /usr/local/bin/npm install ${NODE_PACKAGES}; fi; if [[ ! -z ${UNNODE_PACKAGES} ]]; then /usr/local/bin/npm uninstall ${UNNODE_PACKAGES}; fi; if [ -f /home/container/package.json ]; then /usr/local/bin/npm install; fi; if [[ "${MAIN_FILE}" == "*.js" ]]; then /usr/local/bin/node "/home/container/${MAIN_FILE}" ${NODE_ARGS}; else /usr/local/bin/tsx "/home/container/${MAIN_FILE}" ${NODE_ARGS}; fi
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `MAIN_FILE` | index.js | yes | required\|string\|max:64\|regex:/^[A-Za-z0-9_.\/-]+$/ |
| `AUTO_UPDATE` | 0 | yes | required\|boolean |
| `GIT_ADDRESS` |   | yes | nullable\|string |
| `BRANCH` |   | yes | nullable\|string |
| `USERNAME` |   | yes | nullable\|string |
| `ACCESS_TOKEN` |   | yes | nullable\|string |
| `USER_UPLOAD` | 0 | yes | required\|boolean |
| `NODE_PACKAGES` |   | yes | nullable\|string |
| `UNNODE_PACKAGES` |   | yes | nullable\|string |
| `NODE_ARGS` |   | yes | nullable\|string\|max:64 |
