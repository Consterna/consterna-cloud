# 🛠️ Manual Operativo Maestro (SOP): Entrega "Llave en Mano" en Kinetic Panel
**Versión:** Octubre 2026 (Catálogo Completo de 13 Plantillas: Minecraft Todos los Motores/Proxies + 7 Juegos Principales)  
**Uso Interno:** Guía paso a paso para **Cristian y Víctor** en **Consterna Cloud**  
**Objetivo:** Entregar cualquier servidor de **Minecraft** (Paper, Purpur, Fabric, Quilt, Forge, NeoForge, Velocity Proxy), **Project Zomboid**, **Palworld**, **Rust**, **Valheim**, **Terraria (Vanilla/tModLoader)** o **Core Keeper** 100% configurado y optimizado dentro de nuestro SLA (**30 a 90 minutos**), reduciendo el trabajo manual repetitivo a menos de **5 minutos de clics efectivos**.

---

## ⏸️ Análisis Técnico Profundo: `pause-when-empty-seconds` en Minecraft (`1.21.2+`)

### La Pregunta Clave
> *"Si mientras pre-genero el mundo con Chunky puedo estar yo mismo conectado adentro (sin pausar el menú), dejando de lado Chunky, ¿es mejor tener `pause-when-empty-seconds` activado (`60`) o desactivado (`-1` / `0`)?"*

### 1. ¿Qué hace exactamente esta opción y cómo funciona en cada motor?
Introducida por Mojang en **Minecraft 1.21.2** dentro de `server.properties`:
- **En Vanilla / Fabric / Forge / NeoForge:** Viene por defecto en `pause-when-empty-seconds=60`. Cuando el último jugador se desconecta, el servidor cuenta 60 segundos, imprime en consola `Server empty for 60 seconds, pausing` y **congela por completo el bucle de ticks de los mundos (*world tick loop*)**.
- **En Paper / Purpur:** El equipo de PaperMC la desactiva deliberadamente por defecto (`pause-when-empty-seconds=-1`) porque congelar el bucle de ticks rompe numerosos plugins, tareas programadas y mecánicas de servidores multijugador.
- **Cómo se desactiva:** Poniendo cualquier valor `<= 0` (`-1` o `0`).

### 2. ¿Qué se congela exactamente cuando el servidor entra en pausa?
Mientras el servidor está pausado sin jugadores:
- **No avanzan los ticks de entidades ni bloques** (los mobs, aldeanos, tolvas, hornos y cultivos se detienen al 100%).
- **No avanza la Redstone** ni los mecanismos automatizados.
- **No avanza el tiempo del mundo** (ni el ciclo día/noche, ni el contador de días `Day X` de F3, ni las estaciones del año).

### 3. ¿Cuándo SÍ es muy recomendable ACTIVARLO (`pause-when-empty-seconds=60`)?
Una vez terminada la pre-generación con Chunky, **SÍ conviene cambiarlo a `60`** en estos casos:
1. **Servidores Survival Casuales de Amigos (por horarios):** Grupos de amigos que entran a jugar juntos por la noche y cuando se desconectan quieren que el mundo los espere exactamente como lo dejaron.
2. **Servidores con Mods de Estaciones, Clima o Contador de Días (*Serene Seasons*, *Fabric Seasons*, *Ecliptic Seasons*, *Tough As Nails*):** Si el servidor queda corriendo 24/7 sin pausa mientras los amigos duermen o trabajan en la vida real, pasarán decenas de días dentro del juego, avanzarán las estaciones (llegando el invierno y matando sus cultivos) sin que nadie haya jugado. Con `pause-when-empty-seconds=60`, el calendario estacional se congela cuando no hay nadie conectado.
3. **Ahorro puro de recursos e I/O:** Reduce en ~95% el uso de CPU y escrituras en disco NVMe mientras el grupo duerme.

### 4. ¿Cuándo es OBLIGATORIO dejarlo DESACTIVADO (`pause-when-empty-seconds=-1` o `0`)?
Debes dejarlo **desactivado (`-1` o `0`)** en estos 3 escenarios:
1. **Survival Técnico Vanilla / Fabric con Granjas en Spawn Chunks o Chunk Loaders:**
   - En Minecraft técnico, los jugadores construyen granjas de hierro, shulkers, cultivos, hornos industriales o *Mob Switches* en los *Spawn Chunks*, o usan **Chunk Loaders con portales del Nether** o **Ender Pearl Stasis Chambers** (cámaras de estasis con perlas de Ender que en 1.21.2+ cargan chunks nativamente) para que sus granjas produzcan mientras están desconectados. Si el servidor se pausa a los 60 segundos de salir el último jugador, todas las granjas y hornos se apagan.
2. **Servidores con Mods Técnicos y *Force-Loading* (*Forge / NeoForge / Fabric*):**
   - En modpacks como *All The Mods 9/10*, *Create*, *Mekanism*, *Applied Energistics 2* o *Prominence II*, los jugadores usan **FTB Chunks** (marcando chunks con `Shift + Clic Izquierdo` en el mapa para mantenerlos cargados 24/7) para que sus trenes de *Create*, mineros digitales, reactores de fisión de *Mekanism* o autocrafteos sigan procesando minerales toda la noche. Si `pause-when-empty-seconds=60` está activo, el *force-loading* de FTB Chunks se congela al salir el último jugador.
3. **Servidores con Plugins, Timers, RCON y Mapas Web (*Paper / Purpur*):**
   - Plugins de mapas web como **BlueMap**, **Dynmap** o **Squaremap** (que renderizan tiles en segundo plano), plugins con tareas síncronas (*BukkitScheduler* ligados a ticks del servidor), tiendas/subastas con tiempo de expiración, bots como **DiscordSRV** y nuestra **Fase 2 nocturna de Chunky (04:00 AM)** requieren que el bucle de ticks no esté congelado.

### 📌 Regla Práctica para Consterna Cloud
| Tipo de Servidor del Cliente | Valor Recomendado en `server.properties` |
| :--- | :--- |
| **Paper / Purpur con Plugins** (SMP, Towny, BoxPvP, Eventos) | **`pause-when-empty-seconds=-1`** *(Desactivado — evita romper plugins, timers y mapas web)* |
| **Survival Técnico (Vanilla / Fabric)** o **Modpacks Técnicos (ATM, Create, Mekanism)** | **`pause-when-empty-seconds=-1`** *(Desactivado — permite granjas 24/7, Chunk Loaders y FTB Chunks)* |
| **Survival Casual de Amigos** o **Modpacks RPG/Estaciones (Serene Seasons)** *(tras terminar Chunky)* | **`pause-when-empty-seconds=60`** *(Activado — congela días y estaciones cuando nadie juega)* |

*(Por seguridad operativa, nuestras plantillas vienen con `pause-when-empty-seconds=-1` por defecto para que Chunky y los plugins nunca fallen al instalar; si el cliente es un grupo casual con mods de estaciones y ya terminaste la Fase 1 de Chunky Contigo adentro, puedes dejarlo en `60`).*

---

## 🧭 Tabla Maestra de Todos los Motores, Modloaders y Proxies de Minecraft

| Motor / Modloader / Proxy | ¿Qué es y para qué es mejor? | Versiones Clave | ¿Qué Plantilla de Consterna Cloud usar? |
| :--- | :--- | :--- | :--- |
| **Vanilla** *(Oficial Mojang)* | Binario puro de Mojang sin optimizaciones ni soporte de plugins/mods. Consume mucha más RAM/CPU. | Todas (`1.7` a `1.21.4+`) | **Recomendación:** Ofrecer siempre **Fabric + Lithium + FerriteCore** (100% mecánicas Vanilla con el doble de TPS) usando `Plantilla-Configs-Fabric-1.21.zip`. |
| **CraftBukkit / Spigot** | Los motores clásicos de plugins. **Hoy obsoletos en producción**, ya que Paper carga sus mismos plugins con el triple de rendimiento y parches anti-exploits. | `1.8.8` a `1.21.x` | **Reemplazar siempre por Paper o Purpur.** |
| **Paper** | El estándar de oro para servidores con **Plugins** (alto rendimiento, chunks asíncronos *Moonrise*, parchea exploits, *Anti-Xray* y *Spark* nativos). | `1.21.1 – 1.21.4+`<br>`1.20.1 – 1.20.4`<br>`1.16.5 / 1.17.1 / 1.18.2` | • `Plantilla-Configs-Paper-1.21.zip`<br>• `Plantilla-Configs-Paper-1.20.1.zip`<br>• `Plantilla-Configs-Paper-Legacy-1.16.5-1.18.2.zip`<br>*(Incluyen `PLUGINS_RECOMENDADOS_PAPER*.txt`)* |
| **Pufferfish** | Fork de Paper enfocado en servidores medianos/grandes (+40 jugadores): añade spawns asíncronos (`enable-async-mob-spawning`) y DAB (*Dynamic Activation of Brain*) en `pufferfish.yml`. | `1.18.2 – 1.21.x` | • `Plantilla-Configs-Purpur.zip` *(incluye `pufferfish.yml` con entidades técnicas en `blacklisted-entities` + `PLUGINS_RECOMENDADOS_PURPUR_PUFFERFISH.txt`)* |
| **Purpur** | Fork de Pufferfish + Paper ideal para **SMPs, Towny y Comunidades en LATAM**: añade `use-alternate-keepalive: true` (anti-timeout LATAM) y `villager.lobotomize` (`wait-until-trade-locked: true`). | `1.20.1 – 1.21.4+` | • `Plantilla-Configs-Purpur.zip` *(incluye `purpur.yml` + `pufferfish.yml` + configs de Paper + `PLUGINS_RECOMENDADOS_PURPUR_PUFFERFISH.txt`)* |
| **Folia** *(Especial)* | Fork oficial de PaperMC con **multithreading por regiones del mapa**. Solo tiene sentido en **macro-eventos o servidores anárquicos de +150 a 500 jugadores dispersos**; rompe el 90% de plugins normales. | `1.20.1 – 1.21.x` | Usar configs base de Paper solo si un evento masivo de +150 jugadores lo pide expresamente con plugins compatibles (`folia-supported: true`). |
| **Fabric** | El modloader más ligero, modular y rápido. Ideal para **Survival Técnico** (100% mecánicas Vanilla sin alterar granjas), *Simple Voice Chat*, *Cobblemon*, *Prominence II* y *Better MC Fabric*. | `1.16.5` a `1.21.4+` | • `Plantilla-Configs-Fabric-1.21.zip` *(incluye matriz por versión y reemplazos de plugins en `MODS_RECOMENDADOS.txt`)* |
| **Quilt** | Fork de Fabric compatible con el ~99% de mods de Fabric añadiendo **Quilted Fabric API (QFAPI)**. Menor adopción hoy que Fabric puro; usar solo si un modpack lo pide. | `1.20.1 – 1.21.x` | • `Plantilla-Configs-Fabric-1.21.zip` *(usa exactamente las mismas rutas en `config/` que Fabric)* |
| **Forge** | El modloader clásico e indiscutible para grandes modpacks pesados en **`1.20.1` y versiones anteriores** (*RLCraft / Dregora*, *All The Mods 9*, *Create*, *Dawncraft*, *Alex's Caves*). | `1.16.5`, `1.18.2`, `1.19.2`, `1.20.1` | • `Plantilla-Configs-Forge-NeoForge.zip` *(incluye `ferritecore-mixin.toml`, `canary.properties`, `modernfix-mixins.properties` y `MODS_RECOMENDADOS_FORGE_NEOFORGE.txt`)* |
| **NeoForge** | El sucesor moderno oficial de Forge (creado por el equipo núcleo original de Forge) a partir de **`1.20.4` y `1.21.1+`** (*All The Mods 10*, *Cobblemon 1.6+ NeoForge*, *Create 6.0+*). | `1.20.4`, `1.21.1+` | • `Plantilla-Configs-Forge-NeoForge.zip` *(incluye soporte para **Lithium** oficial en NeoForge 1.21.1+)* |
| **Sponge (`SpongeForge` / `SpongeNeo`)** | API de plugins empresarial propia (*SpongeAPI*, distinta de Spigot/Bukkit) diseñada para convivir limpia y oficialmente con Forge/NeoForge (muy usada en servidores *Pixelmon* grandes). | `1.12.2`, `1.16.5`, `1.20.1`, `1.21.x` | • `Plantilla-Configs-Forge-NeoForge.zip` *(aplicando los mods de optimización de Forge/NeoForge junto a plugins exclusivos de SpongeAPI como *Nucleus*, *GriefDefender* y *LuckPerms-Sponge*)* |
| **Híbridos (*Mohist / Arclight / Magma / Banner / Ketting*)** | ⚠️ **NO RECOMENDADOS:** Intentan forzar la API de Bukkit/Spigot dentro de Forge o Fabric. | Varias | **Evitar siempre que sea posible.** Rompen mixins de mods (*Create*, *AE2*, *Mekanism*), causan duplicación y corrupción de chunks. **Solución profesional:** Usar Fabric o Forge/NeoForge puro con mods server-side nativos (*LuckPerms*, *FTB Essentials*, *FTB Ranks*, *FTB Chunks*, *Ledger*, *StyledChat*). |
| **Velocity Proxy** *(Proxy #1 Recomendado)* | El Proxy moderno oficial de PaperMC para unir varios servidores en una **Network** (*Lobby + Survival + BoxPvP*), centralizar *GeyserMC (Bedrock)* o filtrar ataques de bots (*Sonar*). Seguro por firma HMAC (`modern`). | Soporta clientes `1.7.2` a `1.21.4+` | • `Plantilla-Velocity-Proxy.zip` *(incluye `velocity.toml` v2.7, `GUIA_VINCULACION_VELOCITY.txt` y `PLUGINS_RECOMENDADOS_VELOCITY.txt`)* |
| **BungeeCord / Waterfall** *(Proxies Antiguos)* | **BungeeCord** (de SpigotMC) es el proxy antiguo original e inseguro sin *BungeeGuard*; **Waterfall** era su fork en PaperMC y fue declarado **EOL (Retirado oficialmente)**. | Legacy | **Migrar o recomendar siempre Velocity Proxy** (consume menos RAM, soporta Fabric/Forge y usa `forwarding.secret` criptográfico). |

### 🎯 Resumen Rápido: ¿Qué Recomendar según lo que Pida el Cliente?
1. *"Quiero jugar Survival Vanilla o Técnico con amigos (y ponerle Voice Chat)"* ➡️ **Fabric** (`Plantilla-Configs-Fabric-1.21.zip`).
2. *"Quiero un servidor con Plugins (Rangos, Protecciones, Economía, Tiendas, Entrada desde Bedrock)"* ➡️ **Purpur** o **Paper** (`Plantilla-Configs-Purpur.zip` o `Plantilla-Configs-Paper-1.21.zip`).
3. *"Quiero un Modpack pesado de CurseForge en 1.20.1 o anterior (RLCraft, ATM9, Create, Dawncraft)"* ➡️ **Forge** (`Plantilla-Configs-Forge-NeoForge.zip`).
4. *"Quiero un Modpack pesado moderno en 1.21.1+ (All The Mods 10, Cobblemon 1.6+)"* ➡️ **NeoForge** (`Plantilla-Configs-Forge-NeoForge.zip`).
5. *"Quiero Mods de Forge/Fabric pero también comandos como `/tpa`, `/home`, rangos y terrenos protegidos"* ➡️ **Forge / NeoForge / Fabric PURO + Mods Server-Side (`FTB Essentials + FTB Chunks + LuckPerms + Ledger`)** — **NUNCA Mohist/Arclight**.
6. *"Quiero una Network con Lobby, Survival y BoxPvP conectados"* ➡️ **Velocity Proxy** delante de servidores **Purpur / Paper / Fabric** (`Plantilla-Velocity-Proxy.zip`).

### 💡 Diferencias Clave de Mods de Optimización según la Versión (`Fabric` / `Forge` / `NeoForge`)
1. **Motor de Iluminación (*Starlight*):**
   - En **`1.16.5`, `1.18.2` y `1.19.2`** (tanto Fabric como Forge): Es **obligatorio instalar `Starlight`**, porque el motor de luz de Vanilla era extremadamente lento al generar o cargar chunks.
   - En **`1.20.1` y `1.21.1+`**: **NO hace falta `Starlight`** (de hecho fue archivado en 1.20.4+) porque Mojang reescribió por completo el motor de iluminación en el juego base inspirándose en Starlight.
2. **Arranque de DataFixerUpper (*LazyDFU*):**
   - En **`1.16.5`, `1.18.2` y `1.19.2`**: Es **obligatorio instalar `LazyDFU`** para que el servidor no congele el CPU compilando reglas de migración al encender.
   - En **`1.19.4+`, `1.20.1` y `1.21.1+`**: **NO hace falta `LazyDFU`** porque Mojang incorporó esta optimización de forma nativa.
3. **Formatos de Configuración (`.properties` vs `.toml`):**
   - **FerriteCore** usa `config/ferritecore.mixin.properties` en **Fabric/Quilt**, pero usa **`config/ferritecore-mixin.toml`** en **Forge/NeoForge**.
   - **ModernFix** usa **`config/modernfix-mixins.properties`** en **TODOS los modloaders** (Fabric, Quilt, Forge y NeoForge), ya que su *MixinPlugin* se carga antes de que Forge inicialice su sistema TOML.

---

## 📦 Catálogo y Ubicación de las 13 Plantillas Maestras en `plantillas_kinetic/`

> **🗂️ Organización Profesional del Directorio:**
> - **Paquetes `.zip` listos para subir a Kinetic Panel:** `paquetes_zip/minecraft/` (7 paquetes) y `paquetes_zip/otros_juegos/` (6 paquetes).
> - **Carpetas fuente editables y guías `.txt`:** `codigo_fuente/minecraft/` y `codigo_fuente/otros_juegos/`.
> - **Re-empaquetado automático tras editar fuentes:** `python plantillas_kinetic/scripts/empaquetar_plantillas.py`.

| # | Archivo `.zip` (`paquetes_zip/`) y Carpeta Fuente (`codigo_fuente/`) | Juego / Motor | Qué configura, optimiza e incluye de guía de Mods/Plugins |
| :--- | :--- | :--- | :--- |
| **1** | **`minecraft/Plantilla-Configs-Paper-1.21.zip`**<br>*(Fuente: `minecraft/paper-1.21-optimizado/`)* | **Minecraft Paper 1.21.1 – 1.21.4+** | `bukkit.yml`, `spigot.yml`, `server.properties`, `config/paper-global.yml` (`_version: 29` con Spark), `config/paper-world-defaults.yml` (`_version: 31`, `ALTERNATE_CURRENT`, `per-player-mob-spawns: true`, `short_grass: 300`, `Anti-Xray Mode 1`), `plugins/voicechat/voicechat-server.properties` y **`PLUGINS_RECOMENDADOS_PAPER.txt`**. |
| **2** | **`minecraft/Plantilla-Configs-Paper-1.20.1.zip`**<br>*(Fuente: `minecraft/paper-1.20.1-optimizado/`)* | **Minecraft Paper 1.20.1 – 1.20.4** | Esquema exacto de Paper 1.20.1 (`_version: 28` y `_version: 30`, `grass: 300` en lugar de `short_grass`, sin entidades de 1.21), `plugins/voicechat/voicechat-server.properties` y **`PLUGINS_RECOMENDADOS_PAPER.txt`**. |
| **3** | **`minecraft/Plantilla-Configs-Paper-Legacy-1.16.5-1.18.2.zip`**<br>*(Fuente: `minecraft/paper-legacy-1.16.5-1.18.2/`)* | **Minecraft Paper 1.16.5 / 1.17.1 / 1.18.2** | Archivo monolítico **`paper.yml`** en la raíz (`config-version: 20` auto-migrable a 24/25, `eigencraft-redstone`, `per-player-mob-spawns`, `max-auto-save-chunks-per-tick: 8`, `anti-xray`), `bukkit.yml`, `spigot.yml`, `server.properties` y **`PLUGINS_RECOMENDADOS_PAPER_LEGACY.txt`**. |
| **4** | **`minecraft/Plantilla-Configs-Purpur.zip`**<br>*(Fuente: `minecraft/purpur-optimizado/`)* | **Minecraft Purpur y Pufferfish 1.20.1 / 1.21.1+** | Incluye **`purpur.yml`** (`use-alternate-keepalive: true` anti-timeout LATAM, `villager.lobotomize.enabled: true` con `wait-until-trade-locked: true`, `use-better-mending: true`) y **`pufferfish.yml`** (`enable-async-mob-spawning: true`, DAB con `blacklisted-entities` técnicos), más configs de Paper y **`PLUGINS_RECOMENDADOS_PURPUR_PUFFERFISH.txt`**. |
| **5** | **`minecraft/Plantilla-Configs-Fabric-1.21.zip`**<br>*(Fuente: `minecraft/fabric-optimizado/`)* | **Minecraft Fabric y Quilt (1.16.5 a 1.21.4+)** | `server.properties`, `config/lithium.properties`, `config/ferritecore.mixin.properties`, `config/modernfix-mixins.properties` (`dynamic_resources=true`), `config/voicechat/voicechat-server.properties` y **`MODS_RECOMENDADOS.txt`** (con matriz por versión + reemplazos server-side de plugins). |
| **6** | **`minecraft/Plantilla-Configs-Forge-NeoForge.zip`**<br>*(Fuente: `minecraft/forge-neoforge-optimizado/`)* | **Minecraft Forge (1.16.5–1.20.1) y NeoForge (1.21.1+)** | `server.properties` (`max-tick-time=180000` anti-crash en carga de modpacks), `config/ferritecore-mixin.toml`, `config/modernfix-mixins.properties`, `config/canary.properties` (`mixin.ai.poi=false` para Create), `config/lithium.properties` (NeoForge 1.21+) y **`MODS_RECOMENDADOS_FORGE_NEOFORGE.txt`**. |
| **7** | **`minecraft/Plantilla-Velocity-Proxy.zip`**<br>*(Fuente: `minecraft/velocity-proxy-optimizado/`)* | **Minecraft Velocity Proxy 3.3+ / 3.4+** | `velocity.toml` (`config-version = "2.7"`, `player-info-forwarding-mode = "modern"`, `compression-threshold = 256`, `tcp-fast-open = true`), `GUIA_VINCULACION_VELOCITY.txt` y **`PLUGINS_RECOMENDADOS_VELOCITY.txt`**. |
| **8** | **`otros_juegos/Plantilla-Zomboid-Coop-LATAM.zip`**<br>*(Fuente: `otros_juegos/zomboid-coop-latam/`)* | **Project Zomboid (Build 41 / 42 Co-op)** | `servertest.ini`, `servertest_SandboxVars.lua` (`PingLimit=350`, `KickFastPlayers=false`, `PauseEmpty=true`, `SaveWorldEveryMinutes=15`, limpieza de basura 24h, `BloodLevel = 2`) y **`MODS_RECOMENDADOS_ZOMBOID.txt`** (con `WorkshopItems=` y `Mods=` listos para copiar y pegar). |
| **9** | **`otros_juegos/Plantilla-Palworld-Optimizado.zip`**<br>*(Fuente: `otros_juegos/palworld-optimizado/`)* | **Palworld Dedicated Server** | `Pal/Saved/Config/LinuxServer/PalWorldSettings.ini` (2 líneas estrictas), `Engine.ini` (`NetServerMaxTickRate=60`), `LEEME_PALWORLD.txt` y **`MODS_RECOMENDADOS_PALWORLD.txt`** (ajustes nativos vs `.pak` vs `UE4SS` y `REST API`). |
| **10** | **`otros_juegos/Plantilla-Rust-Optimizado.zip`**<br>*(Fuente: `otros_juegos/rust-optimizado/`)* | **Rust Dedicated Server (Vanilla / Oxide / Carbon)** | `server/rust/cfg/server.cfg` (`fps.limit 60`, `server.tickrate 30`, `gc.buffer 2048`, `server.saveinterval 300`), `LEEME_RUST.txt` y **`PLUGINS_RECOMENDADOS_RUST.txt`** (comparativa **Carbon vs Oxide/uMod** y stack de plugins `.cs`). |
| **11** | **`otros_juegos/Plantilla-Valheim-Optimizado.zip`**<br>*(Fuente: `otros_juegos/valheim-optimizado/`)* | **Valheim Dedicated Server (Vanilla / BepInEx)** | `adminlist.txt`, `permittedlist.txt`, `bannedlist.txt`, `start_server_consterna.sh`, `LEEME_VALHEIM.txt` y **`MODS_RECOMENDADOS_VALHEIM.txt`** (**BepInEx**, **BetterNetworking**, **ServerCharacters**, **WardIsLove** y mods **ServerSync**). |
| **12** | **`otros_juegos/Plantilla-Terraria-Optimizado.zip`**<br>*(Fuente: `otros_juegos/terraria-optimizado/`)* | **Terraria (Vanilla / TShock / tModLoader)** | `serverconfig.txt` (`npcstream=60`, `secure=1`, `upnp=0`), `LEEME_TERRARIA.txt` y **`MODS_Y_PLUGINS_RECOMENDADOS_TERRARIA.txt`** (plugins **TShock** + tabla de `install.txt` y `enabled.json` para **tModLoader / Calamity**). |
| **13** | **`otros_juegos/Plantilla-CoreKeeper-Optimizado.zip`**<br>*(Fuente: `otros_juegos/core-keeper-optimizado/`)* | **Core Keeper Dedicated Server** | `ServerConfig.json` (`networkSendRate: 30`, `maxNumberPacketsSentPerFrame: 2`, `maxNumberPlayers: 8`), `LEEME_CORE_KEEPER.txt` y **`MODS_RECOMENDADOS_CORE_KEEPER.txt`** (ecosistema oficial **`mod.io`** Client-Side vs Cooperativo). |



---

## ⚡ PASO 1: Cómo desplegar cada Juego en Kinetic Panel (`Unarchive`)

### 1. Minecraft (`Paper`, `Purpur`, `Fabric`, `Quilt`, `Forge`, `NeoForge` y `Velocity`)
1. Instala la versión desde **Version Installer** o el modpack desde **Modpack Installer**.
2. Inicia el servidor **una vez**, acepta el EULA y **apágalo (`Stop`)**.
3. En **Management -> File Manager** (raíz `/home/container`), arrastra el `.zip` correspondiente, haz clic en los **3 puntos (`...`) -> `Unarchive`** y luego borra el `.zip`.
4. **Simple Voice Chat (30s):** En `Network -> Ports` abre un puerto secundario (`Open Port`), copia el número y pégalo en `port=` dentro de `/config/voicechat/voicechat-server.properties` (Mods) o `/plugins/voicechat/voicechat-server.properties` (Plugins).
5. **Startup Flags:** En `Settings -> Startup`, activa **`Aikar's Flags`** (planes de 4 GB a 12 GB) o **Generational ZGC** (`-XX:+UseZGC -XX:+ZGenerational` en planes de 16 GB con Java 21+).

### 2. Project Zomboid
1. Inicia el servidor una vez hasta ver `SERVER STARTED` y **apágalo (`Stop`)**.
2. Entra a `/.cache/Server/` (o `/Zomboid/Server/`), sube **`Plantilla-Zomboid-Coop-LATAM.zip`**, haz **`Unarchive`** y borra el `.zip`.
3. Si el cliente pidió mods de Steam Workshop, pega los IDs en `Mods=` y `WorkshopItems=` dentro de `servertest.ini`.

### 3. Palworld
1. Inicia el servidor una vez y **apágalo por completo (`Stop`)** *(obligatorio: si está encendido al subir el archivo, Palworld sobrescribirá tus cambios al apagarse)*.
2. En la raíz `/home/container` del **File Manager**, sube **`Plantilla-Palworld-Optimizado.zip`**, haz clic en **`Unarchive`** y borra el `.zip`. Esto colocará automáticamente `PalWorldSettings.ini` y `Engine.ini` dentro de `/Pal/Saved/Config/LinuxServer/`.
3. Programa en `Management -> Schedules` un **Restart automático diario a las 04:30 AM** para limpiar la memoria de Unreal Engine 5.

### 4. Rust
1. Inicia el servidor o déjalo detenido tras la instalación.
2. En la raíz `/home/container` del **File Manager**, sube **`Plantilla-Rust-Optimizado.zip`**, haz **`Unarchive`** (colocará `server.cfg` en `/server/rust/cfg/server.cfg`) y borra el `.zip`.
3. En `Settings -> Startup`, ajusta `World Size` (`3000–3500` recomendado para 8–12 GB RAM), `Hostname` y activa **Oxide** o **Carbon** si el cliente pidió plugins.

### 5. Valheim
1. Sube **`Plantilla-Valheim-Optimizado.zip`**, haz **`Unarchive`** y coloca `adminlist.txt` (con el SteamID64 del cliente) en la carpeta de guardados (`/saves` o `/.config/unity3d/IronGate/Valheim/`).
2. **Tip Crítico de Latencia LATAM:** En `Settings -> Startup`, si todos los amigos del cliente juegan en **Steam PC**, deja **desactivado `-crossplay`** para que usen conexión directa Steamworks UDP (~70–85ms en Miami) en lugar del relay PlayFab de Microsoft. Activa `-crossplay` únicamente si hay jugadores de Xbox/Game Pass en el grupo.

### 6. Terraria (Vanilla / tModLoader)
1. En la raíz `/home/container`, sube **`Plantilla-Terraria-Optimizado.zip`**, haz **`Unarchive`** y borra el `.zip`.
2. Si es **tModLoader** con mods (ej. *Calamity Mod*), coloca los IDs de Steam Workshop en `/saves/Mods/install.txt` y los nombres de los mods en `/saves/Mods/enabled.json` como se detalla en `LEEME_TERRARIA.txt`.

### 7. Core Keeper
1. Con el servidor **apagado (`Stop`)**, sube **`Plantilla-CoreKeeper-Optimizado.zip`** y haz **`Unarchive`** para aplicar `ServerConfig.json`.
2. Inicia el servidor y abre el archivo **`GameID.txt`** que se genera automáticamente: ese código de **28 caracteres** es el que debes enviarle al cliente para que entren desde `Join Game -> Enter Game ID`.

---

## 🌍 PASO 2 (Minecraft): El "Truco de las 2 Fases" con Chunky

Con el plugin/mod **Chunky** instalado y el servidor encendido:

### Fase 1: Pre-generación Express de Spawn (~4 a 6 minutos antes de entregar)
Pega en la **Console** de Kinetic Panel:
```text
chunky world world
chunky shape square
chunky center 0 0
chunky radius 1500
chunky start
```
*(Genera un área de **3.000 x 3.000 bloques** en ~5 minutos gracias al Ryzen 9 9950X y NVMe PCIe).*

### Fase 2: Expansión Nocturna Automática en `Schedules` (04:00 AM)
Si quieres dejar que el mapa se expanda a `radius 3000` (6.000 x 6.000 bloques) durante la madrugada:
1. Asegúrate de que `pause-when-empty-seconds=-1` esté activo en `server.properties`.
2. En **Management -> Schedules**, crea un Schedule a las `04:00 AM` (`Minute: 0`, `Hour: 4`) con 3 tareas `Send Command`:
   - `chunky world world`
   - `chunky radius 3000`
   - `chunky start`

---

## ✅ PASO 3: Checklist Final y Mensaje de Entrega al Cliente

- [ ] ¿El servidor encendió en verde (`Online`) sin errores en consola?
- [ ] ¿Se aplicó la plantilla optimizada correspondiente al juego/motor?
- [ ] En Minecraft: ¿Está configurado el puerto secundario de *Simple Voice Chat* y completada la Fase 1 de *Chunky*?
- [ ] ¿Se creó el Sub-user del cliente en Kinetic Panel (`Users -> New User`) y se programó el Backup/Restart diario a las 04:30 AM?

### 💬 Plantilla de Mensaje de Entrega (WhatsApp / Discord)

> ¡Hola **[Nombre]**! ☁️🚀 Tu servidor de **[Juego]** en **Consterna Cloud** ya está **100% configurado, optimizado y listo para entrar a jugar**.
>
> 🎮 **Datos de Conexión al Juego:**
> • **IP / Conexión del Servidor:** `[IP_Y_PUERTO o GameID en Core Keeper]`
> • **Versión / Modpack:** `[Ej. Fabric 1.21.1 / Forge 1.20.1 / Palworld / Project Zomboid]`
> • **Chat de Voz / Puerto Extra (si aplica):** Configurado y activo en el puerto `[PUERTO_VOICE]`.
>
> 🛠️ **Lo que dejamos optimizado para tu grupo:**
> • Plantilla de alto rendimiento de Consterna Cloud aplicada para baja latencia en LATAM.
> • Optimización de memoria y guardado automático en disco NVMe PCIe.
> • **Backups diarios automáticos** activados.
>
> 🖥️ **Acceso Total a tu Panel de Control:**
> • **Enlace del Panel:** `[URL_DEL_PANEL]`
> • **Tu Correo:** `[EMAIL_CLIENTE]` *(revisa tu bandeja de entrada para activar tu contraseña si es tu primera vez)*.
>
> Recuerda que nuestra infraestructura opera **24/7** y nuestro equipo está atento por **WhatsApp y Discord (Lun–Dom de 10:00 AM a 10:00 PM)** por si tienes cualquier duda al entrar. ¡Que disfruten muchísimo la aventura! 🔥
