# Tekkura eggs

The eggs Tekkura sells, one per game in the store (plus the variants customers
actually choose between), taken from [pelican-eggs](https://github.com/pelican-eggs)
and configured here so a server built from a store order starts with **no admin
input**.

## Why they need configuring

Upstream eggs assume an admin creates each server by hand and fills in what is
missing. Tekkura builds servers from paid orders, where nobody does. Two things
go wrong:

1. **Port variables keep their fixed default.** Provisioning gives a server a
   run of consecutive ports (as many as the egg's Ports tab asks for), but it
   seeds every egg variable with the egg's own default. Only `SERVER_PORT`
   follows the allocation. A query or RCON port stays at, say, `27015` on every
   server, so the second server on a node collides with the first.
2. **Some variables are required and have no default.** The server is built,
   then cannot start, and the customer sees a broken server.

The table below lists both for every egg, generated from the files.

## When an egg counts as configured

- Every port it binds comes from the server's own allocations.
- Every required variable has a working default.
- The panel's **Ports** tab on the egg says how many ports the game needs and
  which one players connect on.
- A test order deploys it, it starts, and a player can join on the address the
  panel shows. Nobody touched the admin in between.

## Two ways to fix a port variable

Decided on the first egg we configure, then applied the same way everywhere.

- **In the egg.** The startup command runs through the yolk's entrypoint,
  which evaluates it in a shell, so `$((SERVER_PORT + 1))` works there. Simple,
  but the variable shown in the panel then no longer matches what runs.
- **In the panel.** Provisioning fills named port variables from the server's
  allocations (second allocation, third, and so on). One change covers every
  egg, and the panel shows the real port.

## Workflow, one egg at a time

1. Pick the next egg from the table and open its `NOTES.md`.
2. Edit the egg file here and commit, so the diff against upstream is the record
   of what we changed and why.
3. Run `python tools/audit.py` to refresh the notes and the table.
4. Import it on the panel, set its Ports tab, and run a test order.
5. Set its state to `done` in `status.json` and rerun the audit.

## Status

<!-- status:start -->
| Store game | Egg | Role | Fixed port variables | Required, no default | Status |
| --- | --- | --- | --- | --- | --- |
| Project Zomboid | [Project Zomboid](eggs/project-zomboid/NOTES.md) | primary | `STEAM_PORT` | `ADMIN_PASSWORD` | todo |
| Palworld | [Palworld](eggs/palworld/NOTES.md) | primary | `RCON_PORT` | `ADMIN_PASSWORD` | todo |
| Minecraft | [Paper](eggs/minecraft-paper/NOTES.md) | primary | none | `USER_AGENT` | todo |
| Minecraft | [Vanilla Minecraft](eggs/minecraft-vanilla/NOTES.md) | variant | none | none | todo |
| Minecraft | [Fabric](eggs/minecraft-fabric/NOTES.md) | variant | none | none | todo |
| Minecraft | [Forge Minecraft](eggs/minecraft-forge/NOTES.md) | variant | none | none | todo |
| Minecraft | [NeoForge](eggs/minecraft-neoforge/NOTES.md) | variant | none | none | todo |
| Minecraft | [CurseForge Generic](eggs/minecraft-curseforge/NOTES.md) | variant | none | `API_KEY`, `PROJECT_ID` | todo |
| Minecraft | [Modrinth Generic](eggs/minecraft-modrinth/NOTES.md) | variant | none | `PROJECT_ID` | todo |
| Ark: Survival | [ARK: Survival Ascended](eggs/ark-survival-ascended/NOTES.md) | decide | `RCON_PORT` | `ARK_ADMIN_PASSWORD` | decide |
| Ark: Survival | [Ark: Survival Evolved](eggs/ark-survival-evolved/NOTES.md) | decide | `RCON_PORT`, `QUERY_PORT` | none | decide |
| CS:2 | [Counter-Strike 2](eggs/cs2/NOTES.md) | primary | `TV_PORT` | `RCON_PASSWORD`, `STEAM_GSLT` | todo |
| Hytale | [Hytale](eggs/hytale/NOTES.md) | primary | none | none | todo |
| Necesse | [Necesse](eggs/necesse/NOTES.md) | primary | none | none | todo |
| Left 4 Dead 2 | [Left 4 Dead 2](eggs/left-4-dead-2/NOTES.md) | primary | none | none | todo |
| Unturned | [Unturned](eggs/unturned/NOTES.md) | primary | none | `GSLT` | todo |
| Conan Exiles | [Conan Exiles Enhanced](eggs/conan-exiles/NOTES.md) | primary | `QUERY_PORT`, `RCON_PORT` | none | todo |
| Sons Of The Forest | [Sons Of The Forest](eggs/sons-of-the-forest/NOTES.md) | primary | `QUERY_PORT`, `BLOBSYNC_PORT` | none | todo |
| Valheim | [Valheim](eggs/valheim/NOTES.md) | primary | none | none | todo |
| Valheim | [Valheim BepINex](eggs/valheim-bepinex/NOTES.md) | variant | none | none | todo |
| Terraria | [Terraria Vanilla](eggs/terraria/NOTES.md) | primary | none | none | todo |
| Terraria | [tModloader](eggs/terraria-tmodloader/NOTES.md) | variant | none | none | todo |
| Terraria | [tshock](eggs/terraria-tshock/NOTES.md) | variant | none | none | todo |
| Arma 3 Reforger | [Arma Reforger](eggs/arma-reforger/NOTES.md) | primary | none | none | todo |
| HumanitZ | [HumanitZ](eggs/humanitz/NOTES.md) | primary | `QUERY_PORT` | none | todo |
| Windrose | [Windrose](eggs/windrose/NOTES.md) | primary | `DIRECT_CONNECTION_PORT` | none | todo |
<!-- status:end -->

## Upstream and licence

Every egg was copied unchanged in the first commit, pinned to the upstream
commit recorded in `sources.json`, so `git diff` from that commit shows exactly
what Tekkura changed. The eggs are MIT licensed by Michael Parker and the
pelican-eggs contributors; the licence is kept in `LICENSE-pelican-eggs` and
travels with them.
