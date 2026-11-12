# The Isle

Store category: **The Isle** (primary)
Upstream: [games-steamcmd/the_isle/evrima/egg-the-isle.json](https://github.com/pelican-eggs/games-steamcmd/blob/0547150ac32eceac7a1aefb2353aae36b5d2f321/the_isle/evrima/egg-the-isle.json)
Format: `PLCN_v3`
Status: **ready**

RCON and the join queue both defaulted to 44000 on every server; now the 2nd and 3rd ports. Upstream wrote the words "No password" as the server password, linked its author's Discord on every server, and read SERVER_PASSWORD_ENABLED without defining it. 40 players by default.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `QUEUE_PORT` default `44000` (gets port 3): The join queue listens here. Set by the panel.
- [x] `RCON_PORT` default `44000` (gets port 2): Set by the panel.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 3, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
[Default] /home/container/TheIsle/Binaries/Linux/TheIsleServer-Linux-Shipping -Port=$SERVER_PORT -ini:Engine:[EpicOnlineServices]:DedicatedServerClientId=xyza7891gk5PRo3J7G9puCJGFJjmEguW -ini:Engine:[EpicOnlineServices]:DedicatedServerClientSecret=pKWl6t5i9NJK8gTpVlAxzENZ65P8hYzodV8Dqe5Rlc8
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_PASSWORD_ENABLED` | false | yes | required\|string\|in:true,false |
| `SERVER_NAME` | The Isle server | yes | required\|string\|max:70 |
| `PLAYER_COUNT` | 40 | yes | required\|integer\|between:1,100 |
| `ALLOW_REPLAY` | false | yes | required\|string\|in:true,false |
| `HUMANS` | false | yes | required\|string\|in:true,false |
| `DYNAMIC_WEATHER` | true | yes | required\|string\|in:true,false |
| `RCON` | false | yes | required\|string\|in:true,false |
| `RCON_PORT` | 44000 | no | required\|numeric |
| `RCON_PASSWORD` |   | yes | nullable\|string\|max:64 |
| `ENABLE_QUEUE` | true | yes | required\|string\|in:true,false |
| `QUEUE_PORT` | 44000 | no | required\|numeric |
| `DISCORD` |   | yes | nullable\|string\|max:20 |
| `SERVER_PASSWORD` |   | yes | nullable\|string\|max:20 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SRCDS_BETAID` | evrima | no | required\|string\|max:20 |
| `SRCDS_APPID` | 412680 | no | required\|string\|in:412680 |
