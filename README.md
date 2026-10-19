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

## How a port variable is fixed

**In the panel** (decided 2026-10-19). The egg's Ports tab has a **Port
variables** list: "`STEAM_PORT` gets the 2nd port". Provisioning writes each
server's real port number into those variables, so the egg file itself needs
no port arithmetic and the panel shows the port that actually runs.

That setting lives in the panel database, not in the egg file, so record it in
the egg's `status.json` entry (`ports`) when you set it. Then the repo says how
every egg is configured even though the file does not.

**Only ports reachable from outside need an allocation.** Every server runs in
its own container with its own network, so a port the game only uses inside
it (Palworld's console talks to its own RCON on localhost, ARK shuts down
through RCON) cannot clash with the same number on another server. Those are
marked `internal` in `status.json` and keep their default. A port players or
the Steam server browser must reach (query ports, Sons of the Forest's blob
sync) gets an allocation and a port variable.

Also make each mapped variable non-editable in the egg file
(`user_editable: false`), so a customer cannot change it and drift off their
own port.

## Order of work

1. Every game except Minecraft, one egg at a time, starting with Project
   Zomboid because it is live and selling.
2. **ARK** ships as two games: Ascended and Evolved each get their own
   subcategory under "Ark: Survival", with their own products. Both eggs get
   configured.
3. **Minecraft last.** It has the most eggs (Paper, Vanilla, Fabric, Forge,
   NeoForge, modpack installers) and needs its own plan for how the store
   presents the choice.

## Workflow, one egg at a time

1. Pick the next egg from the table and open its `NOTES.md`. **Give it a new
   `uuid` first.** The panel's importer matches eggs by UUID, so an egg that
   still carries upstream's UUID overwrites any copy already on the panel,
   rewriting the startup of every server on it and deleting their variables.
   Production's original Zomboid egg had exactly that UUID.
2. Edit the egg file here and commit, so the diff against upstream is the record
   of what we changed and why.
3. Run `python tools/audit.py` to refresh the notes and the table.
4. Import it on the panel, set its Ports tab, and run a test order.
5. Set its state to `done` in `status.json` and rerun the audit.

States: `configured` means the file is edited, the egg is on the panel (its id
is `panel_egg_id`) and its Ports and Secrets tabs match `status.json`, checked
by reading them back. `done` additionally needs a real order that a player
joined. No egg is `done` yet.

## Status

<!-- status:start -->
| Store game | Egg | Role | Fixed port variables | Required, no default | Status |
| --- | --- | --- | --- | --- | --- |
| Project Zomboid | [Project Zomboid](eggs/project-zomboid/NOTES.md) | primary | `STEAM_PORT` ✓ | `ADMIN_PASSWORD` ✓ | configured |
| Palworld | [Palworld](eggs/palworld/NOTES.md) | primary | `RCON_PORT` (internal) | `ADMIN_PASSWORD` ✓ | configured |
| Minecraft | [Paper](eggs/minecraft-paper/NOTES.md) | primary | none | `USER_AGENT` | last |
| Minecraft | [Vanilla Minecraft](eggs/minecraft-vanilla/NOTES.md) | variant | none | none | last |
| Minecraft | [Fabric](eggs/minecraft-fabric/NOTES.md) | variant | none | none | last |
| Minecraft | [Forge Minecraft](eggs/minecraft-forge/NOTES.md) | variant | none | none | last |
| Minecraft | [NeoForge](eggs/minecraft-neoforge/NOTES.md) | variant | none | none | last |
| Minecraft | [CurseForge Generic](eggs/minecraft-curseforge/NOTES.md) | variant | none | `API_KEY`, `PROJECT_ID` | last |
| Minecraft | [Modrinth Generic](eggs/minecraft-modrinth/NOTES.md) | variant | none | `PROJECT_ID` | last |
| Ark: Survival | [ARK: Survival Ascended](eggs/ark-survival-ascended/NOTES.md) | primary | `RCON_PORT` (internal) | `ARK_ADMIN_PASSWORD` ✓ | configured |
| Ark: Survival | [Ark: Survival Evolved](eggs/ark-survival-evolved/NOTES.md) | primary | `RCON_PORT` (internal), `QUERY_PORT` ✓ | none | configured |
| CS:2 | [Counter-Strike 2](eggs/cs2/NOTES.md) | primary | `TV_PORT` (internal) | `RCON_PASSWORD` ✓ | configured |
| Hytale | [Hytale](eggs/hytale/NOTES.md) | primary | none | none | configured |
| Necesse | [Necesse](eggs/necesse/NOTES.md) | primary | none | none | configured |
| Left 4 Dead 2 | [Left 4 Dead 2](eggs/left-4-dead-2/NOTES.md) | primary | none | none | configured |
| Unturned | [Unturned](eggs/unturned/NOTES.md) | primary | none | none | configured |
| Conan Exiles | [Conan Exiles Enhanced](eggs/conan-exiles/NOTES.md) | primary | `QUERY_PORT` ✓, `RCON_PORT` (internal) | none | configured |
| Sons Of The Forest | [Sons Of The Forest](eggs/sons-of-the-forest/NOTES.md) | primary | `QUERY_PORT` ✓, `BLOBSYNC_PORT` ✓ | none | configured |
| Valheim | [Valheim](eggs/valheim/NOTES.md) | primary | none | none | configured |
| Valheim | [Valheim BepINex](eggs/valheim-bepinex/NOTES.md) | variant | none | none | configured |
| Terraria | [Terraria Vanilla](eggs/terraria/NOTES.md) | primary | none | none | configured |
| Terraria | [tModloader](eggs/terraria-tmodloader/NOTES.md) | variant | none | none | configured |
| Terraria | [tshock](eggs/terraria-tshock/NOTES.md) | variant | none | none | configured |
| Arma 3 Reforger | [Arma 3](eggs/arma-3/NOTES.md) | primary | `RCON_PORT` ✓ | `STEAM_USER`, `STEAM_PASS`, `RCON_PORT` | configured |
| Arma 3 Reforger | [Arma Reforger](eggs/arma-reforger/NOTES.md) | primary | none | none | configured |
| HumanitZ | [HumanitZ](eggs/humanitz/NOTES.md) | primary | `QUERY_PORT` ✓ | none | configured |
| Windrose | [Windrose](eggs/windrose/NOTES.md) | primary | `DIRECT_CONNECTION_PORT` ✓ | none | configured |
<!-- status:end -->

## Upstream and licence

Every egg was copied unchanged in the first commit, pinned to the upstream
commit recorded in `sources.json`, so `git diff` from that commit shows exactly
what Tekkura changed. The eggs are MIT licensed by Michael Parker and the
pelican-eggs contributors; the licence is kept in `LICENSE-pelican-eggs` and
travels with them.
