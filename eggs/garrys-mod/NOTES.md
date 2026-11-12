# Garrys Mod

Store category: **Garry's Mod** (primary)
Upstream: [games-steamcmd/gmod/egg-garrys-mod.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/0547150ac32eceac7a1aefb2353aae36b5d2f321/gmod/egg-garrys-mod.yaml)
Format: `PLCN_v3`
Status: **ready**

One port. The Steam token stays optional, as on CS2: Garry's Mod lists without one. Token and workshop collection go on the command line only when set (the CS2 pattern, 5837d3f). The name goes in as +hostname.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Source: `ghcr.io/pelican-eggs/games:source`

## Startup

```sh
[Default] ./srcds_run -game garrysmod -console -port {{SERVER_PORT}} +ip 0.0.0.0 +hostname "{{SERVER_HOSTNAME}}" $( [ -z "$WORKSHOP_ID" ] || printf %s "+host_workshop_collection $WORKSHOP_ID" ) +map {{SRCDS_MAP}} +gamemode {{GAMEMODE}} -strictportbind -norestart $( [ -z "$STEAM_ACC" ] || printf %s "+sv_setsteamaccount $STEAM_ACC" ) +maxplayers {{MAX_PLAYERS}}  -tickrate {{TICKRATE}}  $( [ "$LUA_REFRESH" == "1" ] || printf %s '-disableluarefresh' )
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_HOSTNAME` | Tekkura Garry's Mod Server | yes | required\|string\|max:60 |
| `SRCDS_MAP` | gm_flatgrass | yes | required\|string\|alpha_dash |
| `STEAM_ACC` |   | yes | nullable\|string\|alpha_num\|size:32 |
| `SRCDS_APPID` | 4020 | no | required\|string\|max:20 |
| `WORKSHOP_ID` |   | yes | nullable\|integer |
| `GAMEMODE` | sandbox | yes | required\|string |
| `MAX_PLAYERS` | 32 | yes | required\|integer\|max:128 |
| `TICKRATE` | 22 | yes | required\|integer\|max:100 |
| `LUA_REFRESH` | 0 | yes | boolean |
