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

### Update URLs point here, never at upstream

Every egg's `meta.update_url` is its own raw file in this repository
(`https://raw.githubusercontent.com/kolikada/tekkura-eggs/main/eggs/<slug>/<file>`),
which is why the repository is public. The panel compares each egg with its
update URL every day (`p:egg:check-updates`) and offers an **Update** button
when they differ; that button imports the URL over the egg. Pointed at
pelican-eggs, as ten production eggs were until 2026-10-26, one click put
back upstream's variables and undid our configuration. Pointed here, the
button appears only when this repository has changed, and it brings our
version. An update keeps the egg's Ports and Secrets tabs, which live in the
panel database, not the file. The same URLs work for Import from URL.

So: push here first, then press Update on the panel. A new egg file gets its
own URL before it is imported. An egg changed in the panel's admin needs the
same change here, or the next Update undoes it.

**One exception: CurseForge Generic.** On production its `API_KEY` variable
has a CurseForge API key as its default. This repository is public, so the
key is never committed and the file here keeps it blank. Production's copy of
that egg therefore has **no update URL**: an update would wipe the key. If it
is ever updated anyway, re-enter the key in the panel afterwards.

Production and this repository were compared egg by egg on 2026-10-26 (all
38 shared eggs, through the panel's own importer) and match, apart from that
key.

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
| Minecraft | [Paper](eggs/minecraft-paper/NOTES.md) | primary | none | none | configured |
| Minecraft | [Vanilla Minecraft](eggs/minecraft-vanilla/NOTES.md) | variant | none | none | configured |
| Minecraft | [Fabric](eggs/minecraft-fabric/NOTES.md) | variant | none | none | configured |
| Minecraft | [Forge Minecraft](eggs/minecraft-forge/NOTES.md) | variant | none | none | configured |
| Minecraft | [NeoForge](eggs/minecraft-neoforge/NOTES.md) | variant | none | none | configured |
| Minecraft | [CurseForge Generic](eggs/minecraft-curseforge/NOTES.md) | variant | none | `API_KEY`, `PROJECT_ID` | configured |
| Minecraft | [Modrinth Generic](eggs/minecraft-modrinth/NOTES.md) | variant | none | `PROJECT_ID` | configured |
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
| Arma 3 Reforger | [Arma 3](eggs/arma-3/NOTES.md) | primary | `RCON_PORT` ✓ | `RCON_PORT` | configured |
| Arma 3 Reforger | [Arma Reforger](eggs/arma-reforger/NOTES.md) | primary | none | none | configured |
| HumanitZ | [HumanitZ](eggs/humanitz/NOTES.md) | primary | `QUERY_PORT` ✓ | none | configured |
| Windrose | [Windrose](eggs/windrose/NOTES.md) | primary | `DIRECT_CONNECTION_PORT` ✓ | none | configured |
| Minecraft | [Purpur](eggs/minecraft-purpur/NOTES.md) | variant | none | none | configured |
| Minecraft | [Quilt](eggs/minecraft-quilt/NOTES.md) | variant | none | none | configured |
| Minecraft | [Spigot](eggs/minecraft-spigot/NOTES.md) | variant | none | none | configured |
| Minecraft | [SpongeForge](eggs/minecraft-spongeforge/NOTES.md) | variant | none | none | skipped |
| Minecraft | [Sponge](eggs/minecraft-spongevanilla/NOTES.md) | variant | none | none | configured |
| Minecraft | [Purpur-Geyser-Floodgate](eggs/minecraft-purpur-geyser/NOTES.md) | variant | none | none | configured |
| Minecraft | [Velocity](eggs/minecraft-velocity/NOTES.md) | variant | none | none | configured |
| Minecraft | [Bungeecord](eggs/minecraft-bungeecord/NOTES.md) | variant | none | none | configured |
| Minecraft | [Vanilla Bedrock](eggs/minecraft-bedrock/NOTES.md) | variant | none | none | configured |
| Minecraft | [PocketmineMP](eggs/minecraft-pocketmine/NOTES.md) | variant | none | none | configured |
| Rust | [Rust](eggs/rust/NOTES.md) | primary | `APP_PORT` ✓, `QUERY_PORT` ✓, `RCON_PORT` ✓ | `RCON_PASS` ✓ | configured |
| DayZ | [DayZ](eggs/dayz/NOTES.md) | primary | `QUERY_PORT` ✓, `RCON_PORT` (internal) | `RCON_PASSWORD` ✓ | configured |
| Bots | [Node.js bot](eggs/bot-nodejs/NOTES.md) | runtime | none | none | configured |
| Bots | [Python bot](eggs/bot-python/NOTES.md) | runtime | none | none | configured |
| Bots | [Muse](eggs/bot-muse/NOTES.md) | ready-made | none | none | configured |
| Bots | [Game Server Watcher](eggs/bot-game-server-watcher/NOTES.md) | ready-made | none | `SECRET` ✓ | configured |
| Bots | [Red](eggs/bot-red/NOTES.md) | ready-made | none | none | configured |
| Bots | [Discord Tickets](eggs/bot-discord-tickets/NOTES.md) | ready-made | none | none | configured |
<!-- status:end -->

## Bots

`bot-nodejs` and `bot-python` are upstream's generic runtimes, configured for a
store order the same way the games are, with three differences:

- **No ports.** A bot talks out to Discord and listens on nothing, so its Ports
  tab needs no port at all (`required_ports` 0, which needs the panel's bot
  `kind` first). A plan that sells the web port add-on gives it one, and the
  bot reads it from `SERVER_PORT`.
- **Running means the process started.** Their Start Configuration is the line
  each image prints just before it launches the bot (`:/home/container$ ` for
  Node.js, `container~ ` for Python). Upstream ships `change this text`, which
  leaves a working bot at Starting for ever; `tools/audit.py` now refuses it in
  any egg.
- **No repository is a normal state.** A store order has none yet, so the
  install leaves a placeholder that prints what to do and waits, and setting
  `GIT_ADDRESS` later reinstalls from it (the panel's reinstall variables).

These are for customers' own code, the product miners buy, so their limits
live in the billing plans and on the node, not here. See "Custom scripts:
strict by default" in the panel's `docs/PLATFORM-PLAN.md`.

**Ready-made bots** (`bot-muse`, `bot-game-server-watcher`) get one egg each,
pinned to a release in a `VERSION` variable customers cannot change. Three
rules every bot egg keeps:

- **Never put a secret in the startup line.** The yolk images print that line
  to the console after Wings has filled in `${VARIABLES}`, so a token there
  lands in the logs, which subusers read and anyone can download. Pass it in a
  file the program loads instead (`config.files`, usually `.env`).
- **What the customer supplies after buying is optional in the egg** and listed
  in the panel's Secrets tab under "Customer sets up after buying"
  (`setup_variables`, recorded as `setup` in `status.json`). Core refuses to
  build a server with a required variable empty, and a store order has no
  token yet. The bot's overview asks for each one, and the startup waits
  rather than crash looping until it is there.
- **The program folder is on the file deny list** (`*` except `data/`), so the
  customer cannot swap the program for something else. Wings still lists the
  names; opening or writing one is refused.

## Upstream and licence

Every egg was copied unchanged in the first commit, pinned to the upstream
commit recorded in `sources.json`, so `git diff` from that commit shows exactly
what Tekkura changed. The eggs are MIT licensed by Michael Parker and the
pelican-eggs contributors; the licence is kept in `LICENSE-pelican-eggs` and
travels with them.
