# Don't Starve Together

Store category: **Don't Starve Together** (primary)
Upstream: [games-steamcmd/dont_starve/egg-don-t-starve-together.json](https://github.com/pelican-eggs/games-steamcmd/blob/0547150ac32eceac7a1aefb2353aae36b5d2f321/dont_starve/egg-don-t-starve-together.json)
Format: `PLCN_v3`
Status: **ready**

Two shards in one container: the surface on the 1st port, the caves on the 2nd, which players connect to when they go down, so it must be reachable. The caves get their own Steam ports. Needs the customer's own Klei server token: optional in the egg, written to cluster_token.txt at every start, and the server says so and stops while it is empty. Upstream's installer saved GitHub's HTML pages as its config and worldgen files, and auto update was off, which leaves a server unjoinable after every game update.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `CAVES_PORT` default `11000` (gets port 2): Players moving into the caves connect here. Set by the panel.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Steamcmd Debian: `ghcr.io/pelican-eggs/steamcmd:debian`

## Startup

```sh
[Default] if [ -z "${SERVER_TOKEN}" ]; then echo "This server needs your Klei server token before it can start. Paste it into Settings, then start the server."; exit 0; fi; printf %s "${SERVER_TOKEN}" > DoNotStarveTogether/config/server/cluster_token.txt; cd bin64 && coproc caves ( ./dontstarve_dedicated_server_nullrenderer_x64 -bind_ip 0.0.0.0 -port {{CAVES_PORT}} -persistent_storage_root /home/container/DoNotStarveTogether -conf_dir config -cluster server -players {{MAX_PLAYERS}} -shard Caves ); ./dontstarve_dedicated_server_nullrenderer_x64 -bind_ip 0.0.0.0 -port {{SERVER_PORT}} -persistent_storage_root /home/container/DoNotStarveTogether -conf_dir config -cluster server -players {{MAX_PLAYERS}} -shard Master && echo 'c_shutdown()' >&"${caves[1]}"
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `CAVES_PORT` | 11000 | no | required\|integer |
| `MAX_PLAYERS` | 8 | yes | required\|integer\|between:1,31 |
| `SERVER_TOKEN` |   | yes | nullable\|string\|max:255 |
| `SRCDS_APPID` | 343050 | no | required\|string\|max:20 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `GAME_MODE` | survival | yes | required\|string |
| `SERVER_NAME` | Tekkura Don't Starve Together Server | yes | required\|string\|max:60 |
| `CLUSTER_DESC` | A Tekkura hosted server | yes | required\|string |
| `MASTER_WORLDGEN` |   | no | nullable\|string |
| `CAVES_WORLDGEN` |   | no | nullable\|string |
