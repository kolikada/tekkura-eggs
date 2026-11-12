# Satisfactory

Store category: **Satisfactory** (primary)
Upstream: [games-steamcmd/satisfactory/egg-satisfactory.json](https://github.com/pelican-eggs/games-steamcmd/blob/0547150ac32eceac7a1aefb2353aae36b5d2f321/satisfactory/egg-satisfactory.json)
Format: `PLCN_v1`
Status: **ready**

Reliable messaging defaulted to 8888 on every server; now the 2nd port. The name, admin password and session are set in the game's own Server Manager, so the first player to join claims the server: the customer should join first.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `RELIABLE_PORT` default `8888` (gets port 2): Required by Satisfactory 1.1 and later. Set by the panel.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
./Engine/Binaries/Linux/*-Linux-Shipping FactoryGame -Port={{SERVER_PORT}} -ReliablePort={{RELIABLE_PORT}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `RELIABLE_PORT` | 8888 | no | required\|integer\|min:0\|max:65535 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `NUM_AUTOSAVES` | 3 | yes | required\|integer\|min:0 |
| `MAX_PLAYERS` | 4 | yes | required\|integer\|min:1 |
| `INIT_CONNECT_TIMEOUT` | 30 | yes | required\|numeric\|min:1 |
| `CONNECT_TIMEOUT` | 20 | yes | required\|numeric\|min:1 |
| `SRCDS_BETAID` |   | yes | string\|nullable\|in:public,experimental |
| `VALIDATE` |   | yes | string\|nullable |
| `SRCDS_APPID` | 1690800 | no | required\|integer\|in:1690800 |
