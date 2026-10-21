# tModloader

Store category: **Terraria** (variant)
Upstream: [games-standalone/terraria/tmodloader/egg-t-modloader.json](https://github.com/pelican-eggs/games-standalone/blob/e1b52607397c0de9d6918d0659f1ff95721d3b49/terraria/tmodloader/egg-t-modloader.json)
Format: `PTDL_v2`
Status: **configured**

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Dotnet 8: `ghcr.io/parkervcp/yolks:dotnet_8`
- Dotnet 6: `ghcr.io/parkervcp/yolks:dotnet_6`

## Startup

```sh
./tModLoaderServer -ip 0.0.0.0 -port {{SERVER_PORT}} -maxplayers {{MAX_PLAYERS}} -password "{{SERVER_PASSWORD}}" -motd "{{MOTD}}" -lang {{LANGUAGE}} -world ~/saves/Worlds/{{WORLD_NAME}}.wld -worldname {{WORLD_NAME}} -autocreate {{WORLD_SIZE}} -config serverconfig.txt -savedirectory ~/ -tmlsavedirectory ~/saves -modpath ~/mods
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `WORLD_NAME` | world | yes | required\|string\|max:20 |
| `MAX_PLAYERS` | 8 | yes | required\|integer\|between:1,255 |
| `WORLD_SIZE` | 1 | yes | required\|string\|in:1,2,3 |
| `VERSION` | latest | yes | required\|string\|max:20 |
| `GITHUB_USER` |   | no | string\|nullable |
| `GITHUB_OAUTH_TOKEN` |   | no | string\|nullable |
| `DIFFICULTY` | 0 | yes | required\|string\|in:0,1,2,3 |
| `SERVER_PASSWORD` |   | yes | nullable\|string\|max:20 |
| `MOTD` | Please don’t cut the purple trees! | yes | required\|string\|max:40 |
| `LANGUAGE` | 1 | yes | required\|string\|in:1,2,3,4,5 |
