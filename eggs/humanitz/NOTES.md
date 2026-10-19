# HumanitZ

Store category: **HumanitZ** (primary)
Upstream: [games-steamcmd/humanitz/egg-humanit-z.json](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/humanitz/egg-humanit-z.json)
Format: `PTDL_v2`
Status: **imported**

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [x] `QUERY_PORT` default `27015` (gets port 2): Steam Query Port

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 2, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/parkervcp/steamcmd:debian: `ghcr.io/parkervcp/steamcmd:debian`

## Startup

```sh
./TSSGame/Binaries/Linux/TSSGameServer-Linux-Shipping TSSGame -log -port={{SERVER_PORT}} -queryport={{QUERY_PORT}} -steamservername="{{SERVER_NAME}}"
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SRCDS_APPID` | 2728330 | no | required\|string\|in:2728330 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `SRCDS_BETAID` | linuxbranch | no | required\|string\|in:linuxbranch |
| `QUERY_PORT` | 27015 | no | required\|numeric |
| `SERVER_NAME` | HumanitZ [Dedicated] | yes | required\|string |
| `PASSWORD` |   | yes | nullable\|string |
| `SAVE_NAME` | DedicatedSaveMP | yes | required\|string |
| `ADMIN_PASS` |   | yes | nullable\|string |
| `MAX_PLAYERS` | 16 | yes | required\|numeric |
| `ONLY_ALLOWED_PLAYERS` | 0 | yes | boolean |
| `SAVE_INTERVAL_SEC` | 300 | yes | required\|numeric |
| `PERMA_DEATH` | 0 | yes | required\|numeric |
| `ON_DEATH` | 2 | yes | required\|numeric |
| `PVP` | 1 | yes | boolean |
| `CLEAR_INFECTION` | 1 | yes | boolean |
| `EAGLE_EYE` | 1 | yes | boolean |
| `AIR_DROP` | 1 | yes | boolean |
| `WEAPON_BREAK` | 1 | yes | boolean |
| `MULTIPLAYER_SLEEP` | 0 | yes | boolean |
| `BUILDING_HEALTH` | 1 | yes | required\|numeric |
| `LOOT_RESPAWN` | 1 | yes | boolean |
| `LOOT_RESPAWN_TIMER` | 60 | yes | required\|numeric |
| `PICKUP_RESPAWN_TIMER` | 90 | yes | required\|numeric |
| `LOOT_RARITY` | 2 | yes | required\|numeric |
| `AIR_DROP_INTERVAL` | 1 | yes | required\|numeric |
| `ZOMBIE_DIFF_HEALTH` | 1 | yes | required\|numeric |
| `ZOMBIE_DIFF_SPEED` | 2 | yes | required\|numeric |
| `ZOMBIE_DIFF_DAMAGE` | 3 | yes | required\|numeric |
| `HUMAN_DIFFICULTY` | 3 | yes | required\|numeric |
| `ZOMBIE_AMOUNT_MULTI` | 1 | yes | required\|numeric |
| `HUMAN_AMOUNT_MULTI` | 1 | yes | required\|numeric |
| `ZOMBIE_DOG_MULTI` | 1 | yes | required\|numeric |
| `ZOMBIE_RESPAWN_TIMER` | 90 | yes | required\|numeric |
| `HUMAN_RESPAWN_TIMER` | 90 | yes | required\|numeric |
| `ANIMAL_RESPAWN_TIMER` | 90 | yes | required\|numeric |
| `STARTING_SEASON` | 1 | yes | required\|numeric |
| `DAYS_PER_SEASON` | 5 | yes | required\|numeric |
| `DAY_DUR` | 40 | yes | required\|numeric |
| `NIGHT_DUR` | 20 | yes | required\|numeric |
| `VITAL_DRAIN` | 1 | yes | required\|numeric |
| `DOG_ENABLED` | 1 | yes | boolean |
| `DOG_NUM` | 8 | yes | required\|numeric |
| `RECRUIT_DOG` | 1 | yes | boolean |
| `COMPANION_HEALTH` | 1 | yes | required\|numeric |
| `COMPANION_DMG` | 1 | yes | required\|numeric |
| `NO_DEATH_FEEDBACK` | 0 | yes | boolean |
| `ALLOW_DISMANTLE` | 1 | yes | boolean |
| `ALLOW_HOUSE_DISMANTLE` | 1 | yes | boolean |
| `TERRITORY` | 1 | yes | boolean |
| `DECAY` | 3600 | yes | required\|numeric |
| `PICKUP_CLEANUP` | 3000 | yes | required\|numeric |
| `FAKE_BUILDING_CLEANUP` | 3000 | yes | required\|numeric |
