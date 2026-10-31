# Red

Store category: **Bots** (ready-made)
Upstream: [chatbots/discord/redbot/egg-red.yaml](https://github.com/pelican-eggs/chatbots/blob/774c22aab6a1982a97338ed4f807ead4b7bf0350/discord/redbot/egg-red.yaml)
Format: `PLCN_v3`
Status: **configured**

Red-DiscordBot 3.5.24 (GPL-3.0, hosted unmodified), pinned in VERSION, which customers cannot change; Python 3.11 (Red 3.5 supports up to 3.11). Upstream passed the token as --token {{TOKEN}} in the startup line, which the console prints; Red reads RED_TOKEN from the environment, so the startup sets it from printenv. Upstream's token defaulted to GET_YOUR_OWN and its Owner variable was required with no default and never used (Red takes the application owner); both fixed, Owner dropped. Installed with pip into the server's ~/.local at the pinned version (upstream took whatever was newest) and the instance config is written by the install (upstream fetched it from parkervcp/eggs, an old repository). Data, cogs included, live in data/; everything else is on the file deny list. TMPDIR is the server's .tmp, since pip and the Audio cog fill the container's small /tmp. Ready-made, but cogs a customer installs from community repositories are Python code, so the CPU watch matters here as much as on a runtime. The Audio cog runs Lavalink on Java inside the container, on localhost, so no port; it wants about 1 GB of memory on its own. Not yet tested end to end: covered by the E2E runs.

## To configure

- [x] Ports tab on the panel: no ports unless the plan sells a web port
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Python 3.11: `ghcr.io/pelican-eggs/yolks:bot_red`

## Startup

```sh
[Default] mkdir -p .tmp; export TMPDIR=/home/container/.tmp; if [ -z "$(printenv DISCORD_TOKEN)" ]; then echo "Waiting for a bot token. Add it on the Overview page and the bot starts."; exec sleep infinity; fi; RED_TOKEN="$(printenv DISCORD_TOKEN)" PATH="$PATH:/home/container/.local/bin" redbot tekkura --prefix "{{PREFIX}}" --no-prompt
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `DISCORD_TOKEN` |   | yes | nullable\|string |
| `PREFIX` | ! | yes | required\|string\|max:10 |
| `VERSION` | 3.5.24 | no | required\|string |
