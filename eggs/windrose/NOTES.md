# Windrose

Store category: **Windrose** (primary)
Upstream: [games-steamcmd/windrose/egg-windrose.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/windrose/egg-windrose.json)
Format: `PLCN_v3`
Status: **imported**

Invite codes work without it; DirectIP must match the game port, so it follows port 1.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `DIRECT_CONNECTION_PORT` default `7777` (gets port 1): TCP/UDP port used when Use Direct Connection is true. Must be open on both proto

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- SteamCMD Proton: `ghcr.io/parkervcp/steamcmd:proton`

## Startup

```sh
[Default] PROTON_DISABLE_XALIA=1 proton run ./R5/Binaries/Win64/WindroseServer-Win64-Shipping.exe & WS_PID=$! ; while [ ! -f ./R5/Saved/Logs/R5.log ]; do sleep 1; done; tail -c0 -F ./R5/Saved/Logs/R5.log --pid=$WS_PID
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_NAME` | Windrose Server | yes | required\|string\|max:64 |
| `INVITE_CODE` | server1 | yes | required\|alpha_num\|min:6\|max:32 |
| `USE_DIRECT_CONNECTION` | false | yes | required\|string\|in:true,false |
| `DIRECT_CONNECTION_PORT` | 7777 | no | required\|integer\|min:1024\|max:65535 |
| `IS_PASSWORD_PROTECTED` | false | yes | required\|string\|in:true,false |
| `SERVER_PASSWORD` |   | yes | nullable\|string\|max:64 |
| `MAX_PLAYERS` | 4 | yes | required\|integer\|min:1\|max:10 |
| `SERVER_REGION` |   | yes | nullable\|string\|in:,SEA,CIS,EU |
| `WORLD_NAME` | Windrose World | yes | required\|string\|max:64 |
| `WORLD_PRESET_TYPE` | Medium | yes | required\|string\|in:Easy,Medium,Hard |
| `SRCDS_APPID` | 4129620 | no | required\|string\|in:4129620 |
| `SRCDS_BETAID` |   | yes | nullable\|string |
| `SRCDS_BETAPASS` |   | yes | nullable\|string |
| `WINDOWS_INSTALL` | 1 | no | boolean\|in:1 |
| `AUTO_UPDATE` | 1 | yes | boolean |
