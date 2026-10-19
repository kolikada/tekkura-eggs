# Left 4 Dead 2

Store category: **Left 4 Dead 2** (primary)
Upstream: [games-steamcmd/left4dead_2/egg-left4-dead2.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/left4dead_2/egg-left4-dead2.json)
Format: `PLCN_v1`
Status: **todo**

## To configure

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/games:source: `ghcr.io/parkervcp/games:source`

## Startup

```sh
./srcds_run -console -port {{SERVER_PORT}} +map {{SRCDS_MAP}} +ip 0.0.0.0 -strictportbind -norestart
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SRCDS_APPID` | 222860 | no | required\|in:222860 |
| `SRCDS_MAP` | c1m1_hotel | yes | required\|string\|max:40 |
| `AUTO_UPDATE` | 1 | yes | boolean |
