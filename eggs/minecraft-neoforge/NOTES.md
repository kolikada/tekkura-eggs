# NeoForge

Store category: **Minecraft** (variant)
Upstream: [minecraft/java/neoforge/egg-neo-forge.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/java/neoforge/egg-neo-forge.json)
Format: `PLCN_v3`
Status: **last**

## To configure

- [ ] Ports tab on the panel: how many ports, and which one players connect on
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
[Default] java -Xms128M -XX:MaxRAMPercentage=95.0 -Dterminal.jline=false -Dterminal.ansi=true @unix_args.txt
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `MC_VERSION` | latest | yes | required\|string\|max:9 |
| `NEOFORGE_VERSION` |   | yes | nullable\|regex:/^[0-9\.\-]+$/ |
