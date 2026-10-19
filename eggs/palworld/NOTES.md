# Palworld

Store category: **Palworld** (primary)
Upstream: [games-steamcmd/palworld/egg-palworld.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/palworld/egg-palworld.yaml)
Format: `PLCN_v3`
Status: **todo**

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [ ] `RCON_PORT` default `25575`: Does not need to be allocated!

Required with no default (provisioning would build a server that cannot start):

- [ ] `ADMIN_PASSWORD`: If specified, players must provide this password (via the in-game chat or RCON) 

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- SteamCMD_Debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
[Default] ./PalworldServerConfigParser; (while read cmd; do rcon -s -a "localhost:$RCON_PORT" -p "$ADMIN_PASSWORD" "$cmd";done) < /dev/stdin & /home/container/Pal/Binaries/Linux/PalServer-Linux-Shipping Pal -publiclobby -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -port={{SERVER_PORT}} -publicport={{SERVER_PORT}} -servername="{{SERVER_NAME}}" -players={{MAX_PLAYERS}} $(if [ -n "$SERVER_PASSWORD" ]; then echo "-serverpassword=\"${SERVER_PASSWORD}\""; fi) -adminpassword="{{ADMIN_PASSWORD}}" -rcon
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SRCDS_APPID` | 2394010 | no | required\|string\|in:2394010 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `MAX_PLAYERS` | 32 | yes | required\|numeric\|between:1,32 |
| `ADMIN_PASSWORD` |   | yes | required\|alpha_dash\|between:1,30 |
| `PUBLIC_IP` |   | no | nullable\|string |
| `SERVER_NAME` | A Pelican hosted Palworld Server | yes | required\|string\|max:64 |
| `SERVER_PASSWORD` |   | yes | nullable\|alpha_dash\|between:1,30 |
| `RCON_PORT` | 25575 | no | required\|numeric |
| `RCON_ENABLE` | True | no | required\|string\|in:True |
| `SERVER_DESCRIPTION` |   | yes | nullable\|string\|max:128 |
| `CROSSPLAY_PLATFORMS` | Steam,Xbox,PS5,Mac | yes | nullable\|string |
