# tshock

Store category: **Terraria** (variant)
Upstream: [games-standalone/terraria/tshock/egg-tshock.json](https://github.com/pelican-eggs/games-standalone/blob/e1b52607397c0de9d6918d0659f1ff95721d3b49/terraria/tshock/egg-tshock.json)
Format: `PLCN_v3`
Status: **todo**

## To configure

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Dotnet 6: `ghcr.io/parkervcp/yolks:dotnet_6`
- Dotnet 9: `ghcr.io/parkervcp/yolks:dotnet_9`

## Startup

```sh
[Default] ./TShock.Server -ip 0.0.0.0 -port {{SERVER_PORT}} -maxplayers {{MAX_PLAYERS}} -world {{WORLD_NAME}}.wld -autocreate {{WORLD_SIZE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `MAX_PLAYERS` | 8 | no | required\|numeric\|digits_between:1,3 |
| `WORLD_NAME` | world | yes | required\|string\|max:20 |
| `WORLD_SIZE` | 1 | no | required\|string\|alpha_dash\|max:20 |
| `TSHOCK_VERSION` | latest | no | required\|string\|max:20 |
