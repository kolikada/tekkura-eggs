# Modrinth Generic

Store category: **Minecraft** (variant)
Upstream: [minecraft/java/modrinth/egg-modrinth-generic.json](https://github.com/pelican-eggs/minecraft/blob/c6f2262eb351054d1be44d3f6a3a605ae163d682/java/modrinth/egg-modrinth-generic.json)
Format: `PLCN_v3`
Status: **last**

## To configure

Required with no default (provisioning would build a server that cannot start):

- [ ] `PROJECT_ID`: This is the modpack project ID from the Modrinth site.  For example, the proje

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
[Default] java $([[ -f user_jvm_args.txt ]] && printf %s "@user_jvm_args.txt") -Xms128M -Xmx{{SERVER_MEMORY}}M -Dterminal.jline=false -Dterminal.ansi=true $([[ ! -f unix_args.txt ]] && printf %s "-jar `cat .serverjar`" || printf %s "@unix_args.txt")
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `PROJECT_ID` |   | yes | required\|string\|max:8 |
| `VERSION_ID` | latest | yes | string\|max:8 |
