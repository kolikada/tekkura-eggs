# Counter-Strike 2

Store category: **CS:2** (primary)
Upstream: [games-steamcmd/counter_strike/counter_strike_2/egg-counter--strike2.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/counter_strike/counter_strike_2/egg-counter--strike2.yaml)
Format: `PLCN_v3`
Status: **todo**

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [ ] `TV_PORT` default `27020`: SourceTV port used for connections to spectates games on your server.

Required with no default (provisioning would build a server that cannot start):

- [ ] `RCON_PASSWORD`: To gain access to administrator commands on the server.
- [ ] `STEAM_GSLT`: The Steam Account Token required for the server to be displayed public. The toke

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:sniper: `ghcr.io/parkervcp/steamcmd:sniper`

## Startup

```sh
[Default] LD_LIBRARY_PATH=$HOME/game/bin/linuxsteamrt64:$LD_LIBRARY_PATH ./game/bin/linuxsteamrt64/cs2 -dedicated $( [ "$VAC_ENABLED" == "1" ] || printf %s ' -insecure' ) -ip 0.0.0.0 -port {{SERVER_PORT}} -tv_port {{TV_PORT}} -maxplayers {{MAX_PLAYERS}} $( [ "$RCON_ENABLED" == "0" ] || printf %s ' -usercon' ) +game_mode {{GAME_MODE}} +game_type {{GAME_TYPE}} +map {{SRCDS_MAP}} +hostname "{{SERVER_NAME}}" +sv_password "{{SERVER_PASSWORD}}" +rcon_password "{{RCON_PASSWORD}}" +sv_setsteamaccount {{STEAM_GSLT}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `RCON_ENABLED` | 0 | yes | boolean |
| `VAC_ENABLED` | 1 | yes | boolean |
| `GAME_MODE` | 1 | yes | required\|string |
| `GAME_TYPE` | 0 | yes | required\|string |
| `SRCDS_MAP` | de_dust2 | yes | required\|string |
| `MAX_PLAYERS` | 12 | yes | required\|numeric\|between:1,64 |
| `RCON_PASSWORD` |   | yes | required\|alpha_dash\|between:1,30 |
| `SERVER_NAME` | My CS2 Server | yes | required\|string\|max:64 |
| `SERVER_PASSWORD` |   | yes | nullable\|alpha_dash\|between:1,30 |
| `SRCDS_APPID` | 730 | no | required\|string\|in:730 |
| `TV_PORT` | 27020 | no | required\|integer\|between:1025,65535 |
| `STEAM_GSLT` |   | yes | required\|string\|alpha_num\|size:32 |
