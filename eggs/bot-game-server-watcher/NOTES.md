# Game Server Watcher

Store category: **Bots** (ready-made)
Upstream: [chatbots/discord/game-server-watcher/egg-game-server-watcher.yaml](https://github.com/pelican-eggs/chatbots/blob/7019bbaf35883b27c52532bc29bc1f090659a074/discord/game-server-watcher/egg-game-server-watcher.yaml)
Format: `PLCN_v3`
Status: **todo**

a-sync/game-server-watcher v3.1.25 (AGPL-3.0, hosted unmodified), pinned in VERSION. Needs its one port: the setup page where customers add the game servers to watch listens on SERVER_PORT. SECRET (that page's admin password) is generated per server. Upstream cloned the moving main branch, ran Node 20 (end of life) and had stop '^^C'. Kind bot, ready-made: the egg decides what runs. The program folder is on the file deny list ('*' except data/), so Files and SFTP cannot open or change it; Wings still lists the names. No secret is ever in the startup line: the yolk entrypoint prints that line to the console after Wings fills in ${VARIABLES}, so the token reaches the bot through .env (Wings config file) instead. Checked on the local Docker stack 2026-10-26: bought through the store, built by billing, installed and started on Wings rc.1.

## To configure

Required with no default (provisioning would build a server that cannot start):

- [x] `SECRET` (generated per server): Signs you in to the setup page, where you add the game servers to watch. Generat

- [ ] Ports tab on the panel: no ports unless the plan sells a web port
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Node.js 22: `ghcr.io/pelican-eggs/yolks:nodejs_22`

## Startup

```sh
[Default] env PORT=${SERVER_PORT} /usr/local/bin/node /home/container/dist/server.js
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `DISCORD_TOKEN` |   | yes | nullable\|string |
| `SECRET` |   | yes | required\|string\|min:8\|max:255 |
| `REFRESH_TIME_MINUTES` | 2 | yes | required\|integer\|min:1\|max:60 |
| `TELEGRAM_BOT_TOKEN` |   | yes | nullable\|string |
| `SLACK_BOT_TOKEN` |   | yes | nullable\|string |
| `SLACK_APP_TOKEN` |   | yes | nullable\|string |
| `STEAM_WEB_API_KEY` |   | yes | nullable\|string |
| `DBG` | 0 | yes | required\|boolean |
| `DATA_PATH` | ./data/ | no | required\|string |
| `VERSION` | v3.1.25 | no | required\|string |
