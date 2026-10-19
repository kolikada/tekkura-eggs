# Vanilla Bedrock

Store category: **Minecraft** (variant)
Upstream: [minecraft/bedrock/bedrock/egg-vanilla-bedrock.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/bedrock/bedrock/egg-vanilla-bedrock.json)
Format: `PLCN_v1`
Status: **configured**

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- ghcr.io/pelican-eggs/yolks:debian: `ghcr.io/pelican-eggs/yolks:debian`

## Startup

```sh
./bedrock_server
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `BEDROCK_VERSION` | latest | yes | required\|string\|max:20 |
| `LD_LIBRARY_PATH` | . | no | required\|string\|max:20 |
| `SERVERNAME` | Bedrock Dedicated Server | yes | required\|string\|max:50 |
| `GAMEMODE` | survival | yes | required\|string\|in:survival,creative,adventure |
| `DIFFICULTY` | easy | yes | required\|string\|in:peaceful,easy,normal,hard |
| `CHEATS` | false | yes | required\|string\|in:true,false |
| `WORLDNAME` | default | yes | required\|string\|max:100 |
