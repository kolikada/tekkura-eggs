# Project Zomboid

Store category: **Project Zomboid** (primary)
Upstream: [games-steamcmd/project_zomboid/egg-project-zomboid.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/project_zomboid/egg-project-zomboid.json)
Format: `PLCN_v1`
Status: **in progress**

Imported as a new egg next to the old live one, which stays for the customer server already on it. The three PZ plans point at the new egg.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `STEAM_PORT` default `16262` (gets port 2): Sets the UDPPort option

Required with no default (provisioning would build a server that cannot start):

- [x] `ADMIN_PASSWORD` (generated per server): Password for the admin account

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
export PATH="./jre64/bin:$PATH" ; export LD_LIBRARY_PATH="./linux64:./natives:.:./jre64/lib/amd64:${LD_LIBRARY_PATH}" ; JSIG="libjsig.so" ; LD_PRELOAD="${LD_PRELOAD}:${JSIG}" ./ProjectZomboid64  -port {{SERVER_PORT}} -udpport {{STEAM_PORT}} -cachedir=/home/container/.cache -servername "{{SERVER_NAME}}" -adminusername {{ADMIN_USER}} -adminpassword "{{ADMIN_PASSWORD}}"
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_NAME` | Pelican | yes | required\|alpha_num\|max:64 |
| `ADMIN_USER` | admin | yes | required\|string\|max:20 |
| `ADMIN_PASSWORD` |   | yes | required\|string\|max:32 |
| `STEAM_PORT` | 16262 | no | required\|string\|max:20 |
| `MAX_PLAYERS` | 10 | no | required\|string\|max:20 |
| `SRCDS_APPID` | 380870 | no | required\|string\|max:20 |
| `SRCDS_BETAID` |   | yes | nullable\|string\|max:64 |
| `AUTO_UPDATE` | 0 | yes | required\|string\|max:20 |
