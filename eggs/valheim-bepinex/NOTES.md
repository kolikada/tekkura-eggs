# Valheim BepINex

Store category: **Valheim** (variant)
Upstream: [games-steamcmd/valheim/valheim_bepinex/egg-valheim-bep-i-nex.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/valheim/valheim_bepinex/egg-valheim-bep-i-nex.yaml)
Format: `PLCN_v3`
Status: **imported**

Query is always game +1. The join password defaulted to "secret" on every server; now generated.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/games:valheim: `ghcr.io/parkervcp/games:valheim`

## Startup

```sh
[Default] export DOORSTOP_ENABLED=1; export DOORSTOP_TARGET_ASSEMBLY=./BepInEx/core/BepInEx.Preloader.dll; export LD_LIBRARY_PATH="./doorstop_libs:./linux64:$LD_LIBRARY_PATH"; export LD_PRELOAD="libdoorstop_x64.so:$LD_PRELOAD"; export LD_LIBRARY_PATH="./linux64:$LD_LIBRARY_PATH"; export SteamAppId=892970; ./valheim_server.x86_64 -nographics -batchmode -name "{{SERVER_NAME}}" -port {{SERVER_PORT}} -world "{{WORLD}}" -password "{{PASSWORD}}" -public {{PUBLIC_SERVER}} -saveinterval {{BACKUP_INTERVAL}} -backups {{BACKUP_COUNT}} -backupshort {{BACKUP_SHORTTIME}} -backuplong {{BACKUP_LONGTIME}} $( [[ {{ENABLE_CROSSPLAY}} -eq 1 ]] && echo " -crossplay ") > >(sed -uE "{{CONSOLE_FILTER}}")
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_NAME` | My Server | yes | required\|string\|max:60 |
| `PASSWORD` | secret | yes | required\|string\|min:5\|max:20 |
| `WORLD` | Dedicated | yes | required\|string\|max:20 |
| `PUBLIC_SERVER` | 1 | yes | boolean |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `ENABLE_CROSSPLAY` | 0 | yes | boolean |
| `SRCDS_BETAID` |   | yes | max:30 |
| `SRCDS_BETAPASS` |   | yes | max:30 |
| `BACKUP_INTERVAL` | 1800 | yes | required\|numeric\|min:0 |
| `BACKUP_COUNT` | 4 | yes | required\|numeric\|min:0 |
| `BACKUP_SHORTTIME` | 7200 | yes | required\|numeric\|min:0 |
| `BACKUP_LONGTIME` | 43200 | yes | required\|numeric\|min:0 |
| `V_MODPACK` |   | yes | string\|nullable |
| `CONSOLE_FILTER` | /^\(Filename:.*Line:[[:space:]]+[[:digit:]]+\)$/d; /^([[:space:]]+)?$/d | no | string |
| `SRCDS_APPID` | 896660 | no | nullable\|numeric |
| `LD_LIBRARY_PATH` | ./linux64 | no | required\|string |
| `BEPINEX_URL` | https://thunderstore.io/api/experimental/package/denikson/BepInExPack_Valheim/ | no | required\|url |
