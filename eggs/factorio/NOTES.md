# Factorio

Store category: **Factorio** (primary)
Upstream: [games-standalone/factorio/factorio/egg-factorio.yaml](https://github.com/pelican-eggs/games-standalone/blob/e1b52607397c0de9d6918d0659f1ff95721d3b49/factorio/factorio/egg-factorio.yaml)
Format: `PLCN_v3`
Status: **ready**

RCON is off until the customer turns it on; its port and password are ready when they do. Public listing is off by default: it needs the customer's factorio.com login, and upstream's placeholders (unnamed, undefined) would have been sent as one. Max players unlocked.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `RCON_PORT` default `` (gets port 2): RCON tools connect here once RCON is on. Set by the panel.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/yolks:debian: `ghcr.io/parkervcp/yolks:debian`

## Startup

```sh
[Default] [ ! -f "./saves/{{SAVE_NAME}}.zip" ] && ./bin/x64/factorio --create ./saves/{{SAVE_NAME}}.zip --map-gen-settings data/map-gen-settings.json --map-settings data/map-settings.json; ./bin/x64/factorio --port {{SERVER_PORT}} --server-settings data/server-settings.json --start-server saves/{{SAVE_NAME}}.zip $( [ "$RCON_ENABLED" = "1" ] && echo "--rcon-port {{RCON_PORT}} --rcon-password {{RCON_PASSWORD}}" )
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `PUBLIC_LISTING` | false | yes | required\|string\|in:true,false |
| `FACTORIO_VERSION` | latest | yes | required\|string\|between:3,12 |
| `MAX_SLOTS` | 20 | yes | required\|numeric\|digits_between:1,3 |
| `SAVE_NAME` | gamesave | yes | alpha_dash\|between:1,100 |
| `SERVER_DESC` | Description | yes | required\|string\|max:200 |
| `SERVER_NAME` | Factorio Server | yes | required\|string\|max:100 |
| `SAVE_INTERVAL` | 10 | yes | required\|numeric\|digits_between:1,3 |
| `SAVE_SLOTS` | 5 | yes | required\|numeric\|digits_between:1,3 |
| `AFK_KICK` | 0 | yes | required\|numeric\|digits_between:1,3 |
| `SERVER_PASSWORD` |   | yes | max:40 |
| `SERVER_USERNAME` |   | yes | nullable\|string\|max:40 |
| `SERVER_TOKEN` |   | yes | nullable\|alpha_num\|max:100 |
| `RCON_ENABLED` | 0 | yes | required\|boolean |
| `RCON_PORT` |   | no | nullable\|integer |
| `RCON_PASSWORD` |   | yes | nullable\|string |
