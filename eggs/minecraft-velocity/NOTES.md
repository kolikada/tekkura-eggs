# Velocity

Store category: **Minecraft** (variant)
Upstream: [minecraft/proxy/java/velocity/egg-velocity.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/proxy/java/velocity/egg-velocity.json)
Format: `PLCN_v3`
Status: **configured**

USER_AGENT defaults to Tekkura's; PaperMC's API refuses downloads without one.

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
[Default] java -Xms128M -Xmx{{SERVER_MEMORY}}M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar {{SERVER_JARFILE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `VELOCITY_VERSION` | latest | no | required\|string\|max:20 |
| `SERVER_JARFILE` | velocity.jar | no | required\|string\|max:32\|regex:/^([\w\d._-]+)(\.jar)$/ |
| `DL_PATH` |   | no | nullable\|string |
| `BUILD_NUMBER` | latest | yes | required\|string\|max:20 |
| `USER_AGENT` | Tekkura (https://www.tekkura.cloud) | no | required |
| `PROJECT` | velocity | no |   |
