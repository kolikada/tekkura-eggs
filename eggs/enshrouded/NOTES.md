# Enshrouded

Store category: **Enshrouded** (primary)
Upstream: [games-steamcmd/enshrouded/egg-enshrouded.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/0547150ac32eceac7a1aefb2353aae36b5d2f321/enshrouded/egg-enshrouded.yaml)
Format: `PLCN_v3`
Status: **ready**

Players find and join on the query port, game port +1, so they connect on the 2nd; gamePort is written as the 1st for builds that still read it. Upstream's default file carried the same three group passwords on every server; now each is made per server and written by the installer. Upstream also asked Steam for ${STEAM_APPID}, a variable the egg never had. 16 players at most, the game's own limit.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `QUERY_PORT` default `` (gets port 2): Players find and join the server on this port. Set by the panel.

Required with no default (provisioning would build a server that cannot start):

- [ ] `QUERY_PORT`: Players find and join the server on this port. Set by the panel.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 2)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Steam Proton: `ghcr.io/pelican-eggs/steamcmd:proton`

## Startup

```sh
[Default] proton run ./enshrouded_server.exe & ENS_PID=$! ; tail -c0 -F ./logs/enshrouded_server.log --pid=$ENS_PID
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `ADMIN_PASSWORD` |   | no | nullable\|string\|max:32 |
| `FRIEND_PASSWORD` |   | no | nullable\|string\|max:32 |
| `GUEST_PASSWORD` |   | no | nullable\|string\|max:32 |
| `QUERY_PORT` |   | no | required\|numeric |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SRV_NAME` | My Server | yes | required\|string |
| `MAX_PLAYERS` | 16 | yes | required\|integer\|between:1,16 |
| `SAVE_NAME` | DedicatedSaveMP | yes | required\|string |
| `SRCDS_APPID` | 2278520 | no | required\|string\|in:2278520 |
| `WINDOWS_INSTALL` | 1 | no | in:1 |
| `VALIDATE` | 0 | yes | boolean |
| `DIFFICULT_PRESET` | Default | yes | required\|string\|in:Default,Relaxed,Hard,Survival,Custom |
