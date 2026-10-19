# Terraria Vanilla

Store category: **Terraria** (primary)
Upstream: [games-standalone/terraria/vanilla/egg-terraria-vanilla.json](https://github.com/pelican-eggs/games-standalone/blob/e1b52607397c0de9d6918d0659f1ff95721d3b49/terraria/vanilla/egg-terraria-vanilla.json)
Format: `PTDL_v2`
Status: **configured**

The port reaches the game through serverconfig.txt.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Debian: `ghcr.io/parkervcp/yolks:debian`

## Startup

```sh
./TerrariaServer.bin.x86_64 -config serverconfig.txt
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `TERRARIA_VERSION` | latest | yes | required\|string\|max:20 |
| `WORLD_NAME` | world | yes | required\|string\|max:20 |
| `MAX_PLAYERS` | 8 | yes | required\|numeric\|max:255 |
| `WORLD_SIZE` | 1 | yes | required\|numeric\|in:1,2,3 |
| `WORLD_DIFFICULTY` | 3 | yes | required\|numeric\|in:0,1,2,3 |
| `SERVER_MOTD` | Welcome! | yes | required\|string\|max:128 |
| `WORLD_SEED` |   | yes | nullable\|string\|max:20 |
| `PASSWORD` |   | yes | nullable\|string |
| `NPCSTREAM` | 0 | yes | required\|int\|between:0,60 |
