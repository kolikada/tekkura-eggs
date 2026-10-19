# PocketmineMP

Store category: **Minecraft** (variant)
Upstream: [minecraft/bedrock/pocketmine_mp/egg-pocketmine-m-p.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/bedrock/pocketmine_mp/egg-pocketmine-m-p.json)
Format: `PLCN_v3`
Status: **configured**

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/pelican-eggs/yolks:debian: `ghcr.io/pelican-eggs/yolks:debian`

## Startup

```sh
[Default] ./bin/php7/bin/php ./PocketMine-MP.phar --no-wizard
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `VERSION` | PM5PHP83 | yes | required\|string\|in:PM5,PM5PHP83,PM5PHP84,PM4 |
