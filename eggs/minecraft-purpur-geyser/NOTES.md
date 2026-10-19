# Purpur-Geyser-Floodgate

Store category: **Minecraft** (variant)
Upstream: [minecraft/crossplay/purpur-geysermc-floodgate/egg-purpur--geyser--floodgate.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/crossplay/purpur-geysermc-floodgate/egg-purpur--geyser--floodgate.json)
Format: `PTDL_v2`
Status: **configured**

Geyser's Bedrock listener is pointed at the server's own port (UDP side) through plugins/Geyser-Spigot/config.yml; Bedrock players use the same address.

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
java -Xms128M -Xmx{{SERVER_MEMORY}}M -Dterminal.jline=false -Dterminal.ansi=true --add-modules=jdk.incubator.vector -jar {{SERVER_JARFILE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `MINECRAFT_VERSION` | latest | yes | required\|string\|max:20 |
| `SERVER_JARFILE` | server.jar | yes | required\|regex:/^([\w\d._-]+)(\.jar)$/\|max:80 |
| `BUILD_NUMBER` | latest | yes | required\|string\|max:20 |
