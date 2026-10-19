# Arma 3

Store category: **Arma 3 Reforger** (primary)
Upstream: [games-steamcmd/arma/arma3/egg-arma3.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/arma/arma3/egg-arma3.json)
Format: `PLCN_v1`
Status: **configured**

Game, +1 query, +2 Steam, +3 VON and +4 BattlEye are fixed offsets, hence a run of 5; RCON (required, no default upstream) gets the 6th. Install needs a real Steam account (not anonymous) set as the egg's default STEAM_USER and STEAM_PASS on the panel; Kenneth sets those, they are credentials.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `RCON_PORT` default `` (gets port 6): BattlEye's RCon port for remote connections with an Arma 3 compliant RCon client

Required with no default (provisioning would build a server that cannot start):

- [ ] `STEAM_USER`: Used for installation and updates. Account does not need to own Arma 3, but MUST
- [ ] `STEAM_PASS`: Used for installation and updates. Steam Guard MUST be completely TURNED OFF for
- [ ] `RCON_PORT`: BattlEye's RCon port for remote connections with an Arma 3 compliant RCon client

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 6, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/games:arma3: `ghcr.io/parkervcp/games:arma3`

## Startup

```sh
./{{SERVER_BINARY}} -par=startup_params_server.txt
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `STEAM_USER` |   | no | required\|string |
| `STEAM_PASS` |   | no | required\|string |
| `STEAMCMD_ATTEMPTS` | 3 | no | required\|integer |
| `RCON_PORT` |   | no | required\|integer\|between:0,65536 |
| `UPDATE_SERVER` | 1 | yes | boolean |
| `STEAMCMD_BETAID` | public | yes | required\|string\|in:public,creatordlc,profiling |
| `SERVER_BINARY` | arma3server_x64 | yes | required\|string\|in:arma3server,arma3server_x64,arma3serverprofiling,arma3serve |
| `MAX_PLAYERS` | 32 | yes | required\|integer\|gt:0 |
| `SERVER_PASSWORD` |   | yes | nullable\|string |
| `MOD_FILE` | modlist.html | yes | nullable\|string |
| `MODIFICATIONS` |   | yes | nullable\|string |
| `PARAM_NOLOGS` | 1 | yes | boolean |
| `PARAM_LOADMISSIONTOMEMORY` | 1 | yes | boolean |
| `PARAM_AUTOINIT` | 0 | yes | boolean |
| `RCON_PASSWORD` |   | yes | nullable\|alpha_num |
| `SERVERMODS` |   | yes | nullable\|string |
| `OPTIONALMODS` |   | yes | nullable\|string |
| `PARAM_FILEPATCHING` | 0 | yes | boolean |
| `PARAM_LIMITFPS` | 50 | yes | required\|integer\|between:5,1000 |
| `HC_NUM` | 0 | yes | required\|integer\|between:0,5 |
| `HC_HIDE` | 1 | yes | boolean |
| `MODS_LOWERCASE` | 0 | yes | boolean |
| `VALIDATE_SERVER` | 0 | yes | boolean |
| `STEAMCMD_APPID` | 233780 | no | required\|integer |
| `BASIC_CFG_URL` | https://raw.githubusercontent.com/pelican-eggs/games-steamcmd/main/arma/arma3/eg | no | required\|url |
