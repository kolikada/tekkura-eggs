# SpongeForge

Store category: **Minecraft** (variant)
Upstream: [minecraft/java/spongeforge/egg-sponge-forge.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/java/spongeforge/egg-sponge-forge.json)
Format: `PTDL_v2`
Status: **skipped**

Superseded: the Sponge egg (minecraft-spongevanilla) installs SpongeVanilla, SpongeForge and SpongeNeo through SPONGE_TYPE, and supports current Java. This one stops at Java 18.

## To configure

- [ ] Ports tab on the panel: how many ports, and which one players connect on
- [ ] Test deploy from a store order with no admin input, and a player can join

## Images

- Java 8: `ghcr.io/pelican-eggs/yolks:java_8`
- Java 11: `ghcr.io/pelican-eggs/yolks:java_11`
- Java 16: `ghcr.io/pelican-eggs/yolks:java_16`
- Java 17: `ghcr.io/pelican-eggs/yolks:java_17`
- Java 18: `ghcr.io/pelican-eggs/yolks:java_18`

## Startup

```sh
java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `SERVER_JARFILE` | server.jar | yes | required\|regex:/^([\w\d._-]+)(\.jar)$/ |
| `SF_VERSION` | recommended | yes | required\|string |
| `FORGE_VERSION` |   | yes | nullable\|regex:/^[0-9\.\-]+$/ |
