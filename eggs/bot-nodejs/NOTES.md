# Node.js bot

Store category: **Bots** (runtime)
Upstream: [generic/nodejs/egg-nodejs-generic.yaml](https://github.com/pelican-eggs/generic/blob/eec3d4b153ccb8b901905b486f29d4d199154f5b/nodejs/egg-nodejs-generic.yaml)
Format: `PLCN_v3`
Status: **todo**

Node.js 24 LTS by default, 26 and 22 offered; 23 and 25 dropped (end of life). Running is the entrypoint's `:/home/container$ ` line. Kind bot: no ports by default (required_ports 0 needs the panel's bot kind first, see the panel's docs/PLATFORM-PLAN.md), the web port add-on brings one. With no repository the install leaves a placeholder that prints what to do and idles, so a store order starts and reads Running. Setting GIT_ADDRESS reinstalls by itself (reinstall) and the placeholder is removed first. Checked in Docker on the real images 2026-10-26: no repo, then repo set and reinstalled.

Deploys (2026-10-29), for the panel's Deploy and Variables pages: a hidden `DEPLOY_KEY` variable the startup reads with `printenv` (Wings prints `${VAR}` expanded in the startup line, so the key is never written as one) into `/tmp/.ssh` for `GIT_SSH_COMMAND`; one `git pull` when the panel leaves a `.tekkura-deploy` marker; `.env` sourced into the environment at start. The install marks the folder git-safe (it runs as root on the server user's files), clones through a temp folder so files already there survive, switches an existing checkout to a new repository or branch, and restores the old remote if the fetch fails, so the panel retries. Checked on the local stack with Wings rc.1: checkout, pull, push webhook, `.env`, deploy key.

Deploy results (2026-10-30): after a checkout, and after the pull a deploy asks for, the egg writes `.tekkura-deploy-result` (`ok|failed <time> <sha>`), which the panel's `RecordDeployResultJob` reads, since Wings reports an install that exits 1 as successful. Checked on the local stack: a pull recorded ok, and failed with the git server stopped.

## To configure

- [ ] Ports tab on the panel: no ports unless the plan sells a web port
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Node.js 24 (LTS): `ghcr.io/pelican-eggs/yolks:nodejs_24`
- Node.js 26: `ghcr.io/pelican-eggs/yolks:nodejs_26`
- Node.js 22 (LTS): `ghcr.io/pelican-eggs/yolks:nodejs_22`

## Startup

```sh
[Default] if [ -n "$(printenv DEPLOY_KEY)" ]; then mkdir -p /tmp/.ssh && printenv DEPLOY_KEY > /tmp/.ssh/deploy_key && chmod 600 /tmp/.ssh/deploy_key && export GIT_SSH_COMMAND="ssh -i /tmp/.ssh/deploy_key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o UserKnownHostsFile=/tmp/.ssh/known_hosts"; fi; if [[ -d .git ]] && { [[ "{{AUTO_UPDATE}}" == "1" ]] || [[ -f .tekkura-deploy ]]; }; then rm -f .tekkura-deploy; if git pull; then R=ok; else R=failed; fi; printf "%s %s %s\n" "$R" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$(git rev-parse HEAD)" > .tekkura-deploy-result; fi; if [[ -f .env ]]; then set -a; . ./.env; set +a; fi; if [[ ! -z ${NODE_PACKAGES} ]]; then /usr/local/bin/npm install ${NODE_PACKAGES}; fi; if [[ ! -z ${UNNODE_PACKAGES} ]]; then /usr/local/bin/npm uninstall ${UNNODE_PACKAGES}; fi; if [ -f /home/container/package.json ]; then /usr/local/bin/npm install; fi; if [[ "${MAIN_FILE}" == "*.js" ]]; then /usr/local/bin/node "/home/container/${MAIN_FILE}" ${NODE_ARGS}; else /usr/local/bin/tsx "/home/container/${MAIN_FILE}" ${NODE_ARGS}; fi
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
| `DEPLOY_KEY` |   | no | nullable\|string |
