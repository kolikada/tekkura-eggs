# Python bot

Store category: **Bots** (runtime)
Upstream: [generic/python/egg-python-generic.yaml](https://github.com/pelican-eggs/generic/blob/eec3d4b153ccb8b901905b486f29d4d199154f5b/python/egg-python-generic.yaml)
Format: `PLCN_v3`
Status: **todo**

Python 3.13 by default, 3.10 to 3.14 offered; 3.7 to 3.9 dropped (end of life). Running is the entrypoint's `container~ ` line. Upstream's install checked for requirements.txt while installing REQUIREMENTS_FILE; fixed. Kind bot: no ports by default (required_ports 0 needs the panel's bot kind first, see the panel's docs/PLATFORM-PLAN.md), the web port add-on brings one. With no repository the install leaves a placeholder that prints what to do and idles, so a store order starts and reads Running. Setting GIT_ADDRESS reinstalls by itself (reinstall) and the placeholder is removed first. Checked in Docker on the real images 2026-10-26: no repo, then repo set and reinstalled.

Deploys (2026-10-29), for the panel's Deploy and Variables pages: a hidden `DEPLOY_KEY` variable the startup reads with `printenv` (Wings prints `${VAR}` expanded in the startup line, so the key is never written as one) into `/tmp/.ssh` for `GIT_SSH_COMMAND`; one `git pull` when the panel leaves a `.tekkura-deploy` marker; `.env` sourced into the environment at start. The install marks the folder git-safe (it runs as root on the server user's files), clones through a temp folder so files already there survive, switches an existing checkout to a new repository or branch, and restores the old remote if the fetch fails, so the panel retries. Checked on the local stack with Wings rc.1: checkout, pull, push webhook, `.env`, deploy key.

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
[Default] if [ -n "$(printenv DEPLOY_KEY)" ]; then mkdir -p /tmp/.ssh && printenv DEPLOY_KEY > /tmp/.ssh/deploy_key && chmod 600 /tmp/.ssh/deploy_key && export GIT_SSH_COMMAND="ssh -i /tmp/.ssh/deploy_key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o UserKnownHostsFile=/tmp/.ssh/known_hosts"; fi; if [[ -d .git ]] && { [[ "{{AUTO_UPDATE}}" == "1" ]] || [[ -f .tekkura-deploy ]]; }; then rm -f .tekkura-deploy; git pull; fi; if [[ -f .env ]]; then set -a; . ./.env; set +a; fi; if [[ ! -z "{{PY_PACKAGES}}" ]]; then pip install -U --prefix .local {{PY_PACKAGES}}; fi; if [[ -f /home/container/${REQUIREMENTS_FILE} ]]; then pip install -U --prefix .local -r ${REQUIREMENTS_FILE}; fi; /usr/local/bin/python /home/container/{{PY_FILE}}
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
| `DEPLOY_KEY` |   | no | nullable\|string |
