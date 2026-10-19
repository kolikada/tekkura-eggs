# DayZ

Store category: **DayZ** (primary)
Upstream: [games-steamcmd/dayz/egg-day-z.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/dayz/egg-day-z.json)
Format: `PTDL_v2`
Status: **configured**

Query is needed for the server list. Like Arma 3, it installs only with a real Steam login, which the customer supplies; the server reinstalls itself once both are filled.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `QUERY_PORT` default `27016` (gets port 2): UDP port for Steam server list features. Helps the server be visible in the clie
- [x] `RCON_PORT` default `2305` (internal: only used inside the container): Used by Tools or Battlemetrics to manage servers from outside. RCON Port is reco

Required with no default (provisioning would build a server that cannot start):

- [x] `RCON_PASSWORD` (generated per server): This password is used to authenticate third parties to access server controls vi

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/games:dayz: `ghcr.io/parkervcp/games:dayz`

## Startup

```sh
./{{SERVER_BINARY}} -port={{SERVER_PORT}} -profiles=profiles -bepath=./ -config=serverDZ.cfg -mod={{CLIENT_MODS}} -serverMod={{SERVERMODS}} {{STARTUP_PARAMS}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `QUERY_PORT` | 27016 | no | required\|integer\|between:1024,65536 |
| `STEAM_USER` |   | yes | nullable\|string\|not_in:anonymous |
| `STEAM_PASS` |   | yes | nullable\|string |
| `DISABLE_MOD_UPDATES` | 0 | no | boolean |
| `STEAMCMD_ATTEMPTS` | 3 | no | required\|integer |
| `SKIP_INSTALL` | 0 | no | boolean |
| `UPDATE_SERVER` | 1 | yes | boolean |
| `SERVER_HOSTNAME` | DayZ Server | yes | required\|string |
| `MAX_PLAYERS` | 64 | yes | required\|integer\|gt:0 |
| `SERVER_PASSWORD` |   | yes | nullable\|string |
| `ADMIN_PASSWORD` |   | yes | nullable\|string |
| `RCON_PORT` | 2305 | no | required\|integer\|between:1024,65536 |
| `RCON_PASSWORD` |   | yes | required\|string\|max:20 |
| `MOD_FILE` | modlist.html | yes | nullable\|string |
| `MODIFICATIONS` |   | yes | nullable\|string |
| `VERIFY_SIGNATURES` | 2 | yes | required\|string\|in:0,2 |
| `ENFORCE_BUILD` | 1 | yes | boolean |
| `DISABLE_VON` | 0 | yes | boolean |
| `VON_QUALITY` | 20 | yes | required\|integer\|between:0,30 |
| `DISABLE_THIRD` | 0 | yes | boolean |
| `DISABLE_CROSSHAIR` | 0 | yes | boolean |
| `DISABLE_PERSONAL_LIGHT` | 1 | yes | boolean |
| `LIGHTING_CONFIG` | 0 | yes | boolean |
| `PERSISTENT_TIME` | 0 | yes | boolean |
| `TIME_MULT` | 12 | yes | required\|integer\|between:0,24 |
| `NIGHT_MULT` | 1 | yes | required\|numeric\|between:0.1,64 |
| `MODS_LOWERCASE` | 0 | yes | boolean |
| `VALIDATE_SERVER` | 0 | yes | boolean |
| `SERVERMODS` |   | yes | nullable\|string |
| `STARTUP_PARAMS` | -dologs -adminlog -netlog -freezecheck | yes | nullable\|string |
| `SERVER_BINARY` | DayZServer | no | required\|string\|in:DayZServer |
| `STEAMCMD_APPID` | 223350 | no | required\|integer\|in:223350,1042420 |
