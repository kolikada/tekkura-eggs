# Discord Tickets

Store category: **Bots** (ready-made)
Upstream: [discord-tickets/bot/eggs/pelican.json](https://github.com/discord-tickets/bot/blob/fe7e6579ae554d95d94f49ec55103a85cf3f2a2d/eggs/pelican.json)
Format: `PLCN_v3`
Status: **configured**

Discord Tickets 4.0.52 (GPL-3.0, hosted unmodified), from the project's own Pelican egg, rewritten as PLCN_v3. Runs the project's image pinned to 4.0.52 (upstream offered the moving 4.0, latest and main tags); its start script copies the program into app/ at every start, so app/ is on the file deny list and the image decides what runs. Its one port is the web portal (HTTP_PORT); Wings writes the port and HTTP_EXTERNAL (the server's address) into .env at every start, where upstream wrote the address once at install. Upstream's SUPER (bot owners with power over every server) defaulted to the upstream developer's own Discord ID; now empty. Its install appended a fresh ENCRYPTION_KEY at every reinstall, which makes all encrypted data unreadable; it now writes one only when none is there. Database: sqlite by default, in user/, so it needs nothing; mysql works with a database from the Databases tab (Postgres dropped, Tekkura has no Postgres host). Known gap: the image runs its own start script, so the startup cannot wait for a token the way Muse does; without one it exits, Wings gives up after the second quick exit, and the server reads Offline until the token and secret are in and it is started. Not yet tested end to end: covered by the E2E runs.

## To configure

- [x] Ports tab on the panel: one port, the web portal
- [ ] Test deploy from a store order with no admin input: it installs, starts and reads Running

## Images

- Discord Tickets 4.0.52: `ghcr.io/discord-tickets/bot:4.0.52`

## Startup

```sh
[Default] /app/scripts/start.sh
```

## Variables

| Env | Default | Editable | Rules |
| --- | --- | --- | --- |
| `DISCORD_TOKEN` |   | yes | nullable\|string\|max:100 |
| `DISCORD_SECRET` |   | yes | nullable\|string\|max:75 |
| `SUPER` |   | yes | nullable\|string\|max:200 |
| `DB_PROVIDER` | sqlite | yes | required\|string\|in:sqlite,mysql |
| `DB_CONNECTION_URL` |   | yes | nullable\|string\|max:250 |
| `PUBLISH_COMMANDS` | true | yes | required\|string\|in:true,false |
| `OVERRIDE_ARCHIVE` |   | yes | nullable\|string\|max:20 |
| `PTERODACTYL` | true | no | required\|string |
| `HTTP_TRUST_PROXY` | false | no | required\|string\|in:true,false |
