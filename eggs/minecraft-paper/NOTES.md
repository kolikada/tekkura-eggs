# Paper

Store category: **Minecraft** (primary)
Upstream: [minecraft/java/paper/egg-paper.yaml](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/java/paper/egg-paper.yaml)
Format: `PLCN_v3`
Status: **todo**

## To configure

Required with no default (provisioning would build a server that cannot start):

- [ ] `USER_AGENT`: Required to use the paper fill API. See https://docs.papermc.io/misc/downloads-s

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Java 25: `ghcr.io/pelican-eggs/yolks:java_25`
- Java 21: `ghcr.io/pelican-eggs/yolks:java_21`
- Java 17: `ghcr.io/pelican-eggs/yolks:java_17`
- Java 16: `ghcr.io/pelican-eggs/yolks:java_16`
- Java 11: `ghcr.io/pelican-eggs/yolks:java_11`
- Java 8: `ghcr.io/pelican-eggs/yolks:java_8`

## Startup

```sh
[Default] java -Xms128M -XX:MaxRAMPercentage=95.0 -Dterminal.jline=false -Dterminal.ansi=true -jar {{SERVER_JARFILE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `MINECRAFT_VERSION` | latest | yes | nullable\|string\|max:20 |
| `SERVER_JARFILE` | server.jar | yes | required\|regex:/^([\w\d._-]+)(\.jar)$/ |
| `DL_PATH` |   | no | nullable\|string |
| `BUILD_NUMBER` | latest | yes | required\|string\|max:20 |
| `USER_AGENT` |   | no | required |
| `PROJECT` | paper | no | {} |
