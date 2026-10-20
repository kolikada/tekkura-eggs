# Project Zomboid

Store category: **Project Zomboid** (primary)
Upstream: [games-steamcmd/project_zomboid/egg-project-zomboid.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/project_zomboid/egg-project-zomboid.json)
Format: `PLCN_v1`
Status: **configured**

Production egg #3 (Tekkura UUID). The three PZ plans point at it. Egg #1, renamed "Project Zomboid (old)", stays for the customer server already on it.

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
if [ "${SERVER_MEMORY:-0}" -gt 0 ]; then sed -i -E "s/-Xmx[0-9]+[kKmMgG]?/-Xmx$(( SERVER_MEMORY - SERVER_MEMORY / 4 ))m/" ProjectZomboid64.json; fi ; export PATH="./jre64/bin:$PATH" ; export LD_LIBRARY_PATH="./linux64:./natives:.:./jre64/lib/amd64:${LD_LIBRARY_PATH}" ; JSIG="libjsig.so" ; LD_PRELOAD="${LD_PRELOAD}:${JSIG}" ./ProjectZomboid64  -port {{SERVER_PORT}} -udpport {{STEAM_PORT}} -cachedir=/home/container/.cache -servername "{{SERVER_NAME}}" -adminusername {{ADMIN_USER}} -adminpassword "{{ADMIN_PASSWORD}}"
```

### The heap follows the plan (2026-10-21)

The game launches through `ProjectZomboid64`, which reads its JVM flags from
`ProjectZomboid64.json`, and that file ships `-Xmx8g`. On an 8 GB plan an 8 GiB
heap plus the JVM's own memory is over the container limit, so Wings killed the
server mid world load (exit 137, out of memory) every minute or so: found on
the first store-built ATHLETIC server. The startup now rewrites `-Xmx` to three
quarters of `SERVER_MEMORY` before launching (6 GB on 8, 9 GB on 12, 12 GB on
16), every start, so a Steam update restoring the file changes nothing.
Unlimited memory (0) leaves the file alone.

Written for the steamcmd image's entrypoint, which runs the command through an
unquoted `echo` and `eval`: a lone `*` there expands to file names, which is why
the arithmetic is `SERVER_MEMORY - SERVER_MEMORY / 4` and not `* 75 / 100`.

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_NAME` | Tekkura | yes | required\|alpha_num\|max:64 |
| `ADMIN_USER` | admin | yes | required\|string\|max:20 |
| `ADMIN_PASSWORD` |   | yes | required\|string\|max:32 |
| `STEAM_PORT` | 16262 | no | required\|string\|max:20 |
| `MAX_PLAYERS` | 10 | no | required\|string\|max:20 |
| `SRCDS_APPID` | 380870 | no | required\|string\|max:20 |
| `SRCDS_BETAID` |   | yes | nullable\|string\|max:64 |
| `AUTO_UPDATE` | 0 | yes | required\|string\|max:20 |
