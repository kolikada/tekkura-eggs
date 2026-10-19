# Ark: Survival Evolved

Store category: **Ark: Survival** (primary)
Upstream: [games-steamcmd/ark_survival_evolved/egg-ark--survival-evolved.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/ark_survival_evolved/egg-ark--survival-evolved.json)
Format: `PLCN_v3`
Status: **configured**

Raw UDP is always game +1, query is the 3rd port. The egg default admin password was PleaseChangeMe. Its subcategory exists under "Ark: Survival" (hidden until it has products).

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `RCON_PORT` default `27020` (internal: only used inside the container): ARK rcon port used by rcon tools.
- [x] `QUERY_PORT` default `27015` (gets port 3): ARK query port used by steam server browser and ark client server browser.

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 3, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Steamcmd Debian: `ghcr.io/pelican-eggs/steamcmd:debian`

## Startup

```sh
[Default] rmv() { echo  "stopping server"; rcon -t rcon -a 127.0.0.1:${RCON_PORT} -p ${ARK_ADMIN_PASSWORD} saveworld &&rcon -t rcon -a 127.0.0.1:${RCON_PORT} -p ${ARK_ADMIN_PASSWORD} DoExit && wait ${ARK_PID}; echo "Server Closed"; exit; }; trap rmv 15 2; cd ShooterGame/Binaries/Linux && ./ShooterGameServer {{SERVER_MAP}}?listen?SessionName="{{SESSION_NAME}}"?ServerPassword={{ARK_PASSWORD}}?ServerAdminPassword={{ARK_ADMIN_PASSWORD}}?Port={{SERVER_PORT}}?RCONPort={{RCON_PORT}}?QueryPort={{QUERY_PORT}}?RCONEnabled=True?MaxPlayers={{MAX_PLAYERS}}?GameModIds={{MOD_ID}}$( [ "$BATTLE_EYE" == "1" ] || printf %s ' -NoBattlEye' ) -server -automanagedmods {{ARGS}} -log & ARK_PID=$! ; until echo "waiting for rcon connection..."; (rcon -t rcon -a 127.0.0.1:${RCON_PORT} -p ${ARK_ADMIN_PASSWORD})<&0 & wait $!; do sleep 5; done
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `ARK_PASSWORD` |   | yes | nullable\|alpha_dash\|between:1,100 |
| `ARK_ADMIN_PASSWORD` | PleaseChangeMe | yes | required\|alpha_dash\|between:1,100 |
| `SERVER_MAP` | TheIsland | yes | required\|string\|max:20 |
| `SESSION_NAME` | My ARK Server | yes | required\|string\|max:128 |
| `RCON_PORT` | 27020 | yes | required\|numeric |
| `QUERY_PORT` | 27015 | no | required\|numeric |
| `AUTO_UPDATE` | 0 | yes | boolean |
| `BATTLE_EYE` | 1 | yes | required\|boolean |
| `SRCDS_APPID` | 376030 | no | numeric\|in:376030 |
| `ARGS` |   | yes | nullable\|string |
| `MOD_ID` |   | yes | nullable\|string |
| `MAX_PLAYERS` | 12 | yes | numeric |
| `SRCDS_BETAID` |   | no | nullable |
| `SRCDS_BETAPASS` |   | no | nullable |
