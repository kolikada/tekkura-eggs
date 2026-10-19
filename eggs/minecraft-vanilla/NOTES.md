# Vanilla Minecraft

Store category: **Minecraft** (variant)
Upstream: [minecraft/java/vanilla/egg-vanilla-minecraft.yaml](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/java/vanilla/egg-vanilla-minecraft.yaml)
Format: `PLCN_v3`
Status: **last**

## To configure

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
[Default] java -Xms128M -XX:MaxRAMPercentage=95.0 -jar {{SERVER_JARFILE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_JARFILE` | server.jar | yes | required\|regex:/^([\w\d._-]+)(\.jar)$/ |
| `VANILLA_VERSION` | latest | yes | required\|string\|between:3,15 |
