# Unturned

Store category: **Unturned** (primary)
Upstream: [games-steamcmd/unturned/egg-unturned.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/unturned/egg-unturned.json)
Format: `PTDL_v2`
Status: **todo**

## To configure

Required with no default (provisioning would build a server that cannot start):

- [ ] `GSLT`:  

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
./Unturned_Headless.x86_64 -batchmode -nographics -bind 0.0.0.0 -port {{SERVER_PORT}} -GSLT {{GSLT}} -Name "{{SRV_NAME}}" -Password {{SRV_PW}} +InternetServer/{{SRV_ID}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SRV_NAME` | Unturned Server | yes | string\|max:50 |
| `SRV_PW` |   | yes | nullable\|string |
| `GSLT` |   | yes | required\|string |
| `SRV_ID` | Unturned | no | string |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SRCDS_APPID` | 1110390 | no | required\|string\|in:1110390 |
| `LD_LIBRARY_PATH` | ./Unturned_Headless_Data/Plugins/x86_64/ | no | required\|string |
