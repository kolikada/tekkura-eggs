# Rust

Store category: **Rust** (primary)
Upstream: [games-steamcmd/rust/vanilla/egg-rust.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/rust/vanilla/egg-rust.yaml)
Format: `PLCN_v3`
Status: **configured**

Query, web RCON (admin tools) and the Rust+ companion app all need to be reachable, so each gets a port; one spare. RCON password generated.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `APP_PORT` default `28082` (gets port 4): Port for the Rust+ App. -1 to disable.
- [x] `QUERY_PORT` default `27017` (gets port 2): Server Query Port. Can't be the same as Game's primary port.
- [x] `RCON_PORT` default `28016` (gets port 3): Port for RCON connections.

Required with no default (provisioning would build a server that cannot start):

- [x] `RCON_PASS` (generated per server): RCON access password.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 5, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Rust: `ghcr.io/pelican-eggs/games:rust`

## Startup

```sh
[Default] ./RustDedicated -batchmode +server.port {{SERVER_PORT}} +server.queryport {{QUERY_PORT}} +server.identity "rust" +rcon.port {{RCON_PORT}} +rcon.web true +server.maxplayers {{MAX_PLAYERS}} +rcon.password "{{RCON_PASS}}" +server.saveinterval {{SAVEINTERVAL}} +app.port {{APP_PORT}} {{ADDITIONAL_ARGS}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_HOSTNAME` | A Rust Server | yes | required\|string\|max:60 |
| `FRAMEWORK` | vanilla | yes | required\|in:vanilla,oxide,carbon |
| `LEVEL` | Procedural Map | yes | required\|string\|max:20 |
| `DESCRIPTION` | Powered by Panel | yes | required\|string |
| `SERVER_URL` | http://example.com | yes | nullable\|url |
| `WORLD_SIZE` | 3000 | yes | required\|integer |
| `WORLD_SEED` |   | yes | nullable\|string |
| `MAX_PLAYERS` | 40 | no | required\|integer |
| `SERVER_IMG` |   | yes | nullable\|url |
| `QUERY_PORT` | 27017 | no | required\|integer |
| `RCON_PORT` | 28016 | no | required\|integer |
| `RCON_PASS` |   | yes | required\|regex:/^[\w.-]*$/\|max:64 |
| `SAVEINTERVAL` | 60 | yes | required\|integer |
| `ADDITIONAL_ARGS` |   | yes | nullable\|string |
| `APP_PORT` | 28082 | no | required\|integer |
| `SERVER_LOGO` |   | yes | nullable\|url |
| `MAP_URL` |   | yes | nullable\|url |
| `SRCDS_APPID` | 258550 | no | required\|string\|in:258550 |
| `SERVER_TAGS` |   | yes | nullable\|string\|max:128 |
