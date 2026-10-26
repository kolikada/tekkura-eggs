# Muse

Store category: **Bots** (ready-made)
Upstream: [chatbots/discord/muse/egg-muse.yaml](https://github.com/pelican-eggs/chatbots/blob/7019bbaf35883b27c52532bc29bc1f090659a074/discord/muse/egg-muse.yaml)
Format: `PLCN_v3`
Status: **todo**

Muse v2.11.8 (MIT), pinned in VERSION, which customers cannot change. Upstream bugs fixed: .env read BOT_TOKEN, which does not exist, so the token was always empty; the Spotify secret was written to the client id line; `yarn install --prod` left out prisma, which Muse runs at every start. Token and YouTube key are optional in the egg (core refuses to build a server with a required variable empty) and listed in the panel's setup_variables, which the bot's overview asks for; until the token is set the startup waits instead of crash looping. Kind bot, ready-made: the egg decides what runs. The program folder is on the file deny list ('*' except data/), so Files and SFTP cannot open or change it; Wings still lists the names. No secret is ever in the startup line: the yolk entrypoint prints that line to the console after Wings fills in ${VARIABLES}, so the token reaches the bot through .env (Wings config file) instead. Checked on the local Docker stack 2026-10-26: bought through the store, built by billing, installed and started on Wings rc.1.

## To configure

- [ ] Ports tab on the panel: no ports unless the plan sells a web port
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Node.js 22: `ghcr.io/pelican-eggs/yolks:nodejs_22`

## Startup

```sh
[Default] if ! grep -qE "^DISCORD_TOKEN=." .env 2>/dev/null; then echo "Waiting for a bot token. Add it on the Overview page and the bot starts."; exec sleep infinity; fi; yarn start
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `DISCORD_TOKEN` |   | yes | nullable\|string |
| `YOUTUBE_API_KEY` |   | yes | nullable\|string |
| `SPOTIFY_CLIENT_ID` |   | yes | nullable\|string |
| `SPOTIFY_CLIENT_SECRET` |   | yes | nullable\|string |
| `VERSION` | v2.11.8 | no | required\|string |
| `CI` | True | no | required\|string\|in:true |
