# Arma Reforger

Store category: **Arma 3 Reforger** (primary)
Upstream: [games-steamcmd/arma/arma_reforger/egg-arma-reforger.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/arma/arma_reforger/egg-arma-reforger.json)
Format: `PLCN_v2`
Status: **configured**

The port reaches the game through config.json. A2S and RCON are optional and off.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
sed -i 's/"true"/true/g; s/"false"/false/g' config.json; ./ArmaReforgerServer -gproj ./addons/data/ArmaReforger.gproj -config ./config.json -profile ./profile -backendlog -nothrow -listScenarios -logStats $(({{LOG_INTERVAL}}*1000)) -maxFPS {{MAX_FPS}} -addonTempDir ./tmp
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SERVER_NAME` | Arma Reforger Server | yes | required\|string\|max:255 |
| `MAX_PLAYERS` | 32 | yes | required\|integer\|between:1,256 |
| `SERVER_PASS` |   | yes | nullable\|string\|max:32 |
| `ADMIN_PASS` |   | yes | nullable\|string\|max:32 |
| `SCENARIO_ID` | {ECC61978EDCC2B5A}Missions/23_Campaign.conf | yes | required\|string |
| `VISIBLE` | true | yes | required\|string\|in:true,false |
| `BATTLEYE` | true | yes | required\|string\|in:true,false |
| `DISABLE_THIRD` | false | yes | required\|string\|in:true,false |
| `MAX_FPS` | 120 | yes | nullable\|integer\|gt:0 |
| `LOG_INTERVAL` | 0 | yes | required\|integer\|min:0 |
| `VALIDATE` |   | yes | nullable\|string |
| `SRCDS_APPID` | 1874900 | no | required\|integer |
