# Conan Exiles Enhanced

Store category: **Conan Exiles** (primary)
Upstream: [games-steamcmd/conan_exiles/egg-conan-exiles-enhanced.yaml](https://github.com/pelican-eggs/games-steamcmd/blob/68aa3847dda477c9e5cb0522295b212042f746af/conan_exiles/egg-conan-exiles-enhanced.yaml)
Format: `PLCN_v3`
Status: **todo**

## To configure

Port variables that keep a fixed default on every server (collide on a shared node):

- [ ] `QUERY_PORT` default `27015`: Server Query Port
- [ ] `RCON_PORT` default `25575`: Remote administrative access

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- SteamCMD: `ghcr.io/pelican-eggs/steamcmd:debian`

## Startup

```sh
[Default] ./ConanSandbox/Binaries/Linux/ConanSandboxServer-Linux-Shipping ConanSandbox -Port={{SERVER_PORT}} -QueryPort={{QUERY_PORT}} -RconPort={{RCON_PORT}} -ServerName=\"{{SRV_NAME}}\" -ServerPassword=\"{{SRV_PW}}\" -console -log
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SRCDS_APPID` | 443030 | no | required\|string\|in:443030 |
| `AUTO_UPDATE` | 1 | yes | boolean |
| `QUERY_PORT` | 27015 | no | required\|numeric\|max:65535 |
| `SRV_NAME` | Pelican hosted Server | yes | required\|string\|max:40 |
| `SRV_PW` |   | yes | nullable\|string |
| `RCON_PORT` | 25575 | no | required\|numeric |
