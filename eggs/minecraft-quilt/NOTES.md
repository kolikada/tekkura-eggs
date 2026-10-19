# Quilt

Store category: **Minecraft** (variant)
Upstream: [minecraft/java/quilt/egg-quilt.yaml](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/java/quilt/egg-quilt.yaml)
Format: `PLCN_v3`
Status: **configured**

Upstream shipped no features; given eula, java_version and pid_limit like the other Java eggs.

## To configure

- [x] Ports tab on the panel: how many ports, and which one players connect on (needs 1, connect on port 1)
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Java 8: `ghcr.io/pelican-eggs/yolks:java_8`
- Java 11: `ghcr.io/pelican-eggs/yolks:java_11`
- Java 16: `ghcr.io/pelican-eggs/yolks:java_16`
- Java 17: `ghcr.io/pelican-eggs/yolks:java_17`
- Java 21: `ghcr.io/pelican-eggs/yolks:java_21`
- Java 25: `ghcr.io/pelican-eggs/yolks:java_25`

## Startup

```sh
[Default] java -Xms128M -XX:MaxRAMPercentage=95.0 -jar {{SERVER_JARFILE}} nogui
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `MC_VERSION` | 1.20.2 | yes | required\|string\|between:3,15 |
| `SERVER_JARFILE` | server.jar | yes | required\|regex:/^([\w\d._-]+)(\.jar)$/ |
