# Sons Of The Forest

Store category: **Sons Of The Forest** (primary)
Upstream: [games-steamcmd/sonsoftheforest/egg-sons-of-the-forest.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/sonsoftheforest/egg-sons-of-the-forest.json)
Format: `PTDL_v2`
Status: **configured**

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `QUERY_PORT` default `27016` (gets port 2): UDP port used by Steam to list the server and enable the discovery services.
- [x] `BLOBSYNC_PORT` default `9700` (gets port 3): BlobSyncPort UDP port used by the BlobSync system to initialize game systems and

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 3, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/yolks:wine_latest: `ghcr.io/parkervcp/yolks:wine_latest`

## Startup

```sh
wine ./SonsOfTheForestDS.exe -userdatapath "/home/container/serverconfig" -dedicatedserver.IpAddress "0.0.0.0" -dedicatedserver.GamePort "{{SERVER_PORT}}" -dedicatedserver.QueryPort "{{QUERY_PORT}}" -dedicatedserver.BlobSyncPort "{{BLOBSYNC_PORT}}" -dedicatedserver.MaxPlayers "{{MAX_PLAYERS}}" -dedicatedserver.Password "{{SRV_PW}}" -dedicatedserver.GameMode "{{GAME_MODE}}" -dedicatedserver.SkipNetworkAccessibilityTest "{{SKIP_TESTS}}" -dedicatedserver.SaveSlot "{{SAVE_SLOT}}" -dedicatedserver.LogFilesEnabled "true" -dedicatedserver.TimestampLogFilenames "true"
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `QUERY_PORT` | 27016 | no | required\|integer\|between:1024,65536 |
| `BLOBSYNC_PORT` | 9700 | no | required\|integer\|between:1024,65536 |
| `SRV_NAME` | Sons Of The Forest Server | yes | required\|string\|max:60 |
| `MAX_PLAYERS` | 4 | yes | required\|integer\|between:1,8 |
| `SRV_PW` | changeme | yes | nullable\|string |
| `GAME_MODE` | normal | yes | string\|in:normal,hard,hardsurvival,peaceful,custom |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SRCDS_APPID` | 2465200 | no | required\|string\|max:20 |
| `WINEDEBUG` | -all | no | required\|string\|max:20 |
| `WINEARCH` | win64 | no | required\|string\|max:20 |
| `WINEPATH` | /home/container | no | required\|string\|max:20 |
| `WINETRICKS_RUN` | mono vcrun2019 | no | required\|string |
| `WINDOWS_INSTALL` | 1 | no | required\|string\|in:1 |
| `SKIP_TESTS` | false | yes | required\|string\|in:true,false |
| `SAVE_SLOT` | 0000000001 | yes | required\|numeric\|max:30 |
