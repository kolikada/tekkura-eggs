# 7 Days to Die

Store category: **7 Days to Die** (primary)
Upstream: [games-steamcmd/7_days_to_die/egg-7-days-to-die.json](https://github.com/pelican-eggs/games-steamcmd/blob/0547150ac32eceac7a1aefb2353aae36b5d2f321/7_days_to_die/egg-7-days-to-die.json)
Format: `PTDL_v2`
Status: **ready**

The game takes its port and the next two by itself, so a run of 3 and no port variables. Telnet is how the console talks to the game, inside the container only. The name goes in as -ServerName, which the game reads like any serverconfig.xml property. Max players unlocked, 1 to 64.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `TELNET_PORT` default `8081` (internal: only used inside the container):  

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 3, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
./7DaysToDieServer.x86_64 -configfile=serverconfig.xml -quit -batchmode -nographics -dedicated -ServerName="${SERVER_NAME}" -ServerPort=${SERVER_PORT} -ServerDisabledNetworkProtocols=${SERVER_DISABLED_NETWORK_PROTOCOLS} -ServerMaxPlayerCount=${MAX_PLAYERS} -GameDifficulty=${GAME_DIFFICULTY} -ControlPanelEnabled=false -TelnetEnabled=true -TelnetPort=${TELNET_PORT} -TelnetPassword=${PASSWORD} -logfile logs/latest.log & echo -e "Checking on telnet connection" && until nc -z -v -w5 127.0.0.1 ${TELNET_PORT}; do echo "Waiting for telnet connection..."; sleep 5; done && $( [[ -z ${PASSWORD} ]] && printf %s "telnet -E 127.0.0.1 ${TELNET_PORT}" || printf %s "rcon -t telnet -a 127.0.0.1:${TELNET_PORT} -p {{PASSWORD}}" )
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_NAME` | Tekkura 7 Days to Die Server | yes | required\|string\|max:60 |
| `MAX_PLAYERS` | 8 | yes | required\|integer\|between:1,64 |
| `GAME_DIFFICULTY` | 2 | yes | required\|integer\|between:0,5 |
| `SRCDS_APPID` | 294420 | no | required\|string\|max:20 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `LD_LIBRARY_PATH` | . | no | required\|string\|max:20 |
| `SRCDS_BETAID` |   | yes | nullable\|string\|max:20 |
| `PASSWORD` |   | yes | nullable\|string\|max:30 |
| `TELNET_PORT` | 8081 | yes | required\|string\|max:20 |
| `SERVER_DISABLED_NETWORK_PROTOCOLS` |   | yes | nullable\|string\|max:20 |
