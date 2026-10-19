# ARK: Survival Ascended

Store category: **Ark: Survival** (decide)
Upstream: [games-steamcmd/ark_survival_ascended/egg-a-r-k--survival-ascended.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/ark_survival_ascended/egg-a-r-k--survival-ascended.json)
Format: `PLCN_v1`
Status: **decide**

The store category is "Ark: Survival". Pick Ascended or Evolved (or sell both) before configuring.

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [ ] `RCON_PORT` default `37015`: required for console commands and proper server shutdown (saveworld/exit), doesn

Required with no default (provisioning would build a server that cannot start):

- [ ] `ARK_ADMIN_PASSWORD`: Used for RCON (remote and in-browser console) as well as in-game EnableCheats

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Proton: `ghcr.io/parkervcp/steamcmd:proton`

## Startup

```sh
rmv() { echo "stopping server"; rcon -t rcon -a 127.0.0.1:${RCON_PORT} -p ${ARK_ADMIN_PASSWORD} KeepAlive && rcon -t rcon -a 127.0.0.1:${RCON_PORT} -p ${ARK_ADMIN_PASSWORD} DoExit && wait ${ARK_PID}; echo "Server Closed"; exit; }; trap rmv 15 2; proton run ./ShooterGame/Binaries/Win64/ArkAscendedServer.exe {{SERVER_MAP}}?listen?MaxPlayers={{MAX_PLAYERS}}?SessionName=\"{{SESSION_NAME}}\"?Port={{SERVER_PORT}}?RCONPort={{RCON_PORT}}?RCONEnabled=True$( [  "$SERVER_PVE" == "0" ] || printf %s '?ServerPVE=True' )?ServerPassword="{{SERVER_PASSWORD}}"{{ARGS_PARAMS}}?ServerAdminPassword="{{ARK_ADMIN_PASSWORD}}" -WinLiveMaxPlayers={{MAX_PLAYERS}} -oldconsole -servergamelog $( [ -z "$MOD_IDS" ] || printf %s ' -mods=' $MOD_IDS )$( [ "$BATTLE_EYE" == "1" ] || printf %s ' -NoBattlEye' ) -Port={{SERVER_PORT}} {{ARGS_FLAGS}} & ARK_PID=$! ; tail -c0 -F ./ShooterGame/Saved/Logs/ShooterGame.log --pid=$ARK_PID & until echo "waiting for rcon connection..."; (rcon -t rcon -a 127.0.0.1:${RCON_PORT} -p ${ARK_ADMIN_PASSWORD})<&0 & wait $!; do sleep 5; done
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_MAP` | TheIsland_WP | yes | required\|string\|max:64 |
| `SESSION_NAME` | My ARK Server | yes | required\|string\|max:256 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `BATTLE_EYE` | 1 | yes | boolean |
| `SRCDS_APPID` | 2430930 | no | required\|integer\|in:2430930 |
| `ARGS_PARAMS` |   | yes | nullable\|string\|max:1024 |
| `MAX_PLAYERS` | 70 | yes | required\|integer\|min:1\|max:200 |
| `ARK_ADMIN_PASSWORD` |   | yes | required\|alpha_dash\|max:128 |
| `ARGS_FLAGS` |   | yes | nullable\|string\|max:1024 |
| `SERVER_PVE` | 1 | yes | required\|boolean |
| `SERVER_PASSWORD` |   | yes | nullable\|alpha_dash\|max:128 |
| `RCON_PORT` | 37015 | no | required\|integer\|min:1025\|max:65535 |
| `MOD_IDS` |   | yes | nullable\|string\|max:512 |
