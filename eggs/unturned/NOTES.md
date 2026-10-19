# Unturned

Store category: **Unturned** (primary)
Upstream: [games-steamcmd/unturned/egg-unturned.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/unturned/egg-unturned.json)
Format: `PTDL_v2`
Status: **configured**

Game +1 is required. Steam token made optional and passed only when set.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
./Unturned_Headless.x86_64 -batchmode -nographics -bind 0.0.0.0 -port {{SERVER_PORT}} ${GSLT:+-GSLT ${GSLT}} -Name "{{SRV_NAME}}" -Password {{SRV_PW}} +InternetServer/{{SRV_ID}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SRV_NAME` | Unturned Server | yes | string\|max:50 |
| `SRV_PW` |   | yes | nullable\|string |
| `GSLT` |   | yes | nullable\|string |
| `SRV_ID` | Unturned | no | string |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SRCDS_APPID` | 1110390 | no | required\|string\|in:1110390 |
| `LD_LIBRARY_PATH` | ./Unturned_Headless_Data/Plugins/x86_64/ | no | required\|string |
