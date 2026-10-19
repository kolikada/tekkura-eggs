# Necesse

Store category: **Necesse** (primary)
Upstream: [games-steamcmd/necesse/egg-necesse.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/necesse/egg-necesse.json)
Format: `PTDL_v2`
Status: **imported**

The port reaches the game through cfg/server.cfg.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
./jre/bin/java -Xms128M -Xmx{{SERVER_MEMORY}}M -Dterminal.jline=false -Dterminal.ansi=true -jar Server.jar -localdir -nogui -world {{SAVE_NAME}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SAVE_NAME` | Save1 | yes | required\|string\|max:20 |
| `SERVER_SLOTS` | 10 | yes | required\|numeric\|max:99 |
| `SERVER_PASSWORD` |   | yes | nullable\|string\|max:32 |
| `SRCDS_APPID` | 1169370 | no | required\|string\|in:1169370 |
| `AUTO_UPDATE` | 0 | yes | boolean |
| `SRCDS_BETAID` |   | yes | nullable\|string\|max:64 |
