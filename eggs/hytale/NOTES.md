# Hytale

Store category: **Hytale** (primary)
Upstream: [games-standalone/hytale/egg-hytale.yaml](https://github.com/pelican-eggs/games-standalone/blob/e1b52607397c0de9d6918d0659f1ff95721d3b49/hytale/egg-hytale.yaml)
Format: `PLCN_v3`
Status: **todo**

## To configure

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Hytale: `ghcr.io/pelican-eggs/games:hytale`

## Startup

```sh
[Default] java -Xms128M -XX:MaxRAMPercentage=95.0 -jar HytaleServer.jar --bind 0.0.0.0:{{SERVER_PORT}} --assets ../Assets.zip
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `PATCHLINE` | release | yes | required\|string\|in:release,pre-release |
| `SERVER_VERSION` | latest | yes | required\|string |
| `HYTALE_API_AUTH` | 1 | yes | boolean |
| `ENABLE_WORLD_BACKUP` | 1 | yes | boolean |
| `ENABLE_SERVER_BACKUP` | 1 | yes | boolean |
| `SERVER_BACKUP_RETENTION` | 2 | yes | integer\|required\|min:1 |
| `BACKUP_DIR` | Backups | yes | required\|string |
| `BACKUP_FREQUENCY` | 30 | yes | integer\|required |
| `BACKUP_MAX_COUNT` | 5 | yes | integer |
| `BACKUP_ARCHIVE_MAX_COUNT` | 5 | yes | integer |
| `USE_AOT_CACHE` | 1 | yes | boolean |
| `USE_COMPACT_HEADERS` | 1 | yes | boolean |
| `ALLOW_OP` | 0 | yes | boolean |
| `ACCEPT_EARLY_PLUGINS` | 0 | yes | boolean |
| `DISABLE_SENTRY` | 0 | yes | boolean |
| `IGNORE_BROKEN_MODS` | 0 | yes | boolean |
| `TRANSPORT` | QUIC | yes | required\|string\|in:QUIC,TCP |
| `HYTALE_PROFILE_UUID` |   | yes | nullable\|string |
