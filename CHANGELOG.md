# Registro de Cambios (Changelog)

Todas las modificaciones importantes de este proyecto serán documentadas en este archivo.

## [1.9.3] - 2026-10-16 - Reestructuración SEO Integral, Pruning de Textos Repetitivos y Expansión a 10 Preguntas Frecuentes
### Cambios y Mejoras
- **Reestructuración de Metadatos y SEO On-Page (`index.html`):**
  - **`<title>` & Meta Tags:** Se optimizó el título a *"Hosting de Minecraft y Servidores Gaming en Colombia | Consterna"*, junto con descripciones y palabras clave comerciales enfocadas en Ryzen 9 9950X, ping ~70ms y pagos con Nequi/PayPal.
  - **Schema.org (JSON-LD):** Se implementó `@graph` unificado conteniendo entidad `Product` (valoración 4.9/5 sobre 142 reseñas, rango de precios $8.50 a $32.00 USD) y `FAQPage` enriquecida con las 10 preguntas y respuestas oficiales para capturar fragmentos enriquecidos (Rich Snippets).
- **Navbar Limpia y Drawer Móvil:**
  - Se compactó la navegación desktop y el menú móvil a 6 enlaces estratégicos esenciales (*Planes*, *Cotizador*, *Add-ons*, *Optimización*, *Pagos*, *FAQ*), manteniendo los accesos directos a Discord y WhatsApp.
- **Hero Section Comercial y Reaseguros Clave:**
  - H1 optimizado para intención de búsqueda transaccional y micro-badge de pago local en COP (`~$34.000 COP`).
  - Tres insignias de confianza destacadas: *Entrega Llave en Mano (30–90 min)*, *Garantía de Satisfacción 48h* y *Soporte Humano Real (WhatsApp / Discord)*.
  - Corrección de espaciado en micro-badge local a `mt-2` y normalización de IDs en tabs de optimización (`tab-btn-Project-Zomboid`, `tab-btn-Core-Keeper`) para cumplimiento estricto de HTML5 y `aria-labelledby` accesible.
  - Idempotencia en navegación por enlaces internos y hash para acordeón de FAQs (`openFaq` y `checkFaqHash`).
- **Fusión de Pilares de Valor (`#beneficios`):**
  - Se eliminó la duplicidad entre la antigua barra de confianza y los beneficios, consolidando una cuadrícula de 4 pilares: *Ping Miami ~70–85ms*, *AMD Ryzen 9 9950X a 5.7 GHz*, *Entrega Llave en Mano* y *Backups Diarios + Protección Anti-DDoS*.
- **Catálogo de Planes (`#planes`):**
  - Se integró una franja superior de beneficios universales incluidos (Chunky, Voice Chat, anti-DDoS, backups, panel 24/7).
  - Se reestructuraron las 5 tarjetas de planes (`4GB` a `16GB`) con 4 viñetas progresivas de capacidad real y pie de tarjeta conciso, preservando rigurosamente los IDs dinámicos de cotización TRM (`price-cop`, `price-cop-6`, `price-cop-8`, `price-cop-12`, `price-cop-16`).
- **Cotizador (`#cotizador`) y Vitrina de Optimización (`#optimizacion`):**
  - Se agregó micro-reaseguro de entrega y garantía bajo el botón principal de cotización por WhatsApp.
  - Se limpió el objeto JavaScript `OPTIMIZATION_SHOWCASE`, reemplazando nombres crudos de archivos `.zip` y configuraciones internas por descripciones orientadas a beneficios reales para jugadores en los 7 títulos.
- **Métodos de Pago (`#pagos`):**
  - Se sustituyeron bloques de texto denso por badges visuales destacados para Colombia (Nequi, Nu Colombia, Bre-B, Bancolombia) e Internacional (PayPal, Tarjetas de Crédito/Débito) acompañados de franja de reaseguro de prepago mes a mes sin débitos automáticos.
- **Expansión a 10 Preguntas Frecuentes (`#faq`):**
  - Se añadieron 4 nuevas preguntas con sus respuestas completas en el acordeón accesible:
    7. *¿Tienen garantía de satisfacción o devolución de dinero?* (Garantía 48h con 100% reembolso).
    8. *¿Pueden migrar mi mundo actual desde Aternos, otro hosting o mi PC?* (Migración 100% gratuita).
    9. *¿El chat de voz (Simple Voice Chat) y los puertos UDP tienen costo adicional?* (Puerto UDP dedicado incluido sin costo).
    10. *¿Pueden entrar jugadores de Bedrock (celular/consola) y usuarios No-Premium?* (GeyserMC/Floodgate crossplay y autenticación segura No-Premium).

## [1.9.2] - 2026-10-16 - Clarificación de Escalera de 3 Niveles y Desaturación Visual de la Landing Page
### Cambios y Mejoras
- **Clarificación de la Escalera de 3 Niveles de Servicio (`index.html`):**
  - **Tarjeta Add-on #1 (`#addons`):** Se actualizó a *"Ensamble de Modpacks y Torneos a Medida"* ($5.00 USD / ~$20.000 COP • Pago Único), explicitando que el plan base ya incluye cualquier modpack público (CurseForge/Modrinth) y Voice Chat, y que este Add-on cubre el armado propio desde cero o la configuración previa de torneos estándar (FFA/border/vidas) sin staff en vivo.
  - **Banner Dedicado de Nivel 3 (`#addons`):** Se incorporó un bloque destacado para *"Nivel 3 • Series Gigantescas y Eventos Extremos (Cotización Especial)"*, separando visualmente los torneos con streamers, clúster multi-server y árbitro técnico en vivo para evitar confusiones de alcance con el Add-on #1.
  - **Cotizador Interactivo (`#cotizador`):** Se homologaron las etiquetas, fila de pago único y mensajes dinámicos de WhatsApp para reflejar el ensamble a medida.
- **Desaturación Visual y Enfoque Comercial Directo (`index.html`):**
  - **Limpieza de Ruido Técnico en Cotizador (`GAME_MATRIX`):** Se reemplazaron nombres crudos de archivos `.zip`, scripts y variables de motor (`DoLuaChecksum`, `servertest.ini`, `NetServerMaxTickRate=60`) por resúmenes comerciales orientados a beneficios del jugador.
  - **Vitrina de Optimización (`#optimizacion`):** Se sustituyó el bloque de código de archivos de configuración crudos (`opt-files`) por un panel de entrega optimizada limpio y elegante con enlace directo hacia el FAQ técnico.
  - **Barra de Confianza y Beneficios (`#beneficios`):** Se eliminó jerga innecesaria sobre intermediarios y partners en pantalla principal, enfocando el mensaje en procesadores Ryzen 9 9950X a 5.7 GHz, NVMe PCIe y entrega lista para jugar.
  - **Nota al pie de Planes (`#planes`):** Se compactó el texto y se crearon enlaces directos e interactivos hacia las guías de niveles (`#faq-btn-2`) y memoria RAM (`#faq-btn-3`).
- **Expansión y Traslado Técnico a Preguntas Frecuentes (`#faq`):**
  - Se estructuraron 6 preguntas frecuentes en acordeón dinámico con accesibilidad ARIA completa y soporte de apertura por hash/función `openFaq(id)`:
    1. *¿Cómo y cuándo me entregan el servidor?* (Llave en Mano personalizada en 30-90 min).
    2. *¿Qué incluye mi mensualidad y cuándo necesito el Add-on de $5 USD o una cotización de evento grande?* (Desglose transparente de los 3 niveles con tarjetas visuales).
    3. *¿Cómo sé cuánta memoria RAM necesita mi servidor y qué pasa si nos quedamos cortos?* (Guía por juego/mods/jugadores y escalabilidad inmediata sin perder datos).
    4. *¿Qué optimizaciones aplican internamente y por qué no tengo lag?* (Desglose multijuego con configuraciones de Minecraft, Zomboid, Palworld, Rust, Valheim, Terraria y Core Keeper).
    5. *¿Puedo cambiar de juego, instalar mis propios mods o descargar mis mapas?* (Panel 24/7, SFTP, cambio de plantillas y Sysadmin Dedicado mensual).
    6. *¿Cómo funcionan los pagos y renovaciones? ¿Hay cobros automáticos a mi tarjeta?* (Cero débitos sorpresa, aviso previo de 4 días, Nequi/Nu Bre-B en Colombia a cero comisión y PayPal internacional).

## [1.9.1] - 2026-10-15 - Correcciones Responsive en index.html
### Correcciones
- **Navbar:** el menu horizontal completo se muestra solo desde el breakpoint `xl:` para evitar desbordes en pantallas medianas.
- **Mobile-menu:** ahora con scroll interno y fondo opaco para mantener legibilidad.
- **Cotizador interactivo:** se agrego `flex-wrap` para que los controles no se desborden en moviles.
- **Vitrina:** se aplico `break-all` a textos largos (direcciones/IPs) para evitar overflow horizontal.

## [1.9.0] - 2026-10-15 - 4-Pillar Full-Stack Operational Upgrade: CRM Sync, /admin Panel, Interactive Configurator & Showcase
### Cambios y Mejoras
- **Pilar 1 — Robustez del Backend, Base de Datos, Migraciones y Sincronización con Excel CRM:**
  - **Aislamiento de Pytest y Persistencia Segura (`backend/app/core/db.py` y `backend/tests/conftest.py`):** Se configuró Pytest para utilizar un motor SQLite en memoria aislado (`sqlite://` con `StaticPool` y `app.dependency_overrides[get_db]`), impidiendo que la ejecución de pruebas borre los datos reales de `backend/consterna.db`. Se añadió `@event.listens_for(Engine, "connect")` para activar `PRAGMA foreign_keys=ON` en SQLite, `SQLModel.metadata.create_all(session.get_bind())` e inspección/auto-migración de columnas en `init_db`.
  - **Enriquecimiento de Modelos CRM (`backend/app/models.py`) y Migración Inicial Real (`backend/app/alembic/versions/0794bc9fbf9f_initial_schema.py`):** Se ampliaron `Client` (`external_id`) y `Server` (`game`, `extra_service`, `currency`, `monthly_price`, `one_time_fee`, `host_cost_usd`, `payment_method`, `start_date`, `voice_port`, `notes`) con valores por defecto retrocompatibles y se reemplazaron los `pass` vacíos de la revisión inicial de Alembic por las operaciones reales `op.create_table` y `op.drop_table`.
  - **Sincronización Idempotente (`Upsert`) y Homologación del Excel CRM (`backend/scripts/import_data.py` y `Control_Clientes_Consterna_V7_ENTERPRISE.xlsx`):** Se actualizaron mediante `openpyxl` las tablas de `'⚙️ Configuración'` y las fórmulas universales `VLOOKUP` de `'👥 Clientes Activos'` en el Excel local con los 5 planes (`4GB` a `16GB`), 3 Add-ons y 7 juegos oficiales, y se refactorizó `import_data.py` para realizar *upsert* idempotente con soporte multiserver por cliente, extracción de puerto de voz y repoblación segura de `backend/consterna.db`.
  - **Infraestructura y API (`backend/app/api/routes/clients.py`, `backend/pyproject.toml`, `backend/Dockerfile`, `compose.yml`):** Se corrigió la validación de email duplicado en `POST /api/v1/clients/` para devolver `409 Conflict`, se declararon `pandas>=2.2.0` y `openpyxl>=3.1.2` en `pyproject.toml`, se corrigió `backend/Dockerfile` para copiar `./backend/scripts` a `/app/scripts` y `/app/backend/scripts`, y se añadió el servicio `frontend` (`nginx:alpine` en `8080:80`) en `compose.yml`.
- **Pilar 2 — Automatización Operativa Diaria, Panel Web `/admin`, Pruebas y Monitoreo:**
  - **Endpoints Operativos (`backend/app/api/routes/servers.py` y `backend/app/api/routes/utils.py`):**
    - `GET /api/v1/servers/expiring?days=4`: Lista servidores próximos a vencer o vencidos con días restantes, semáforo (`🟢 Al Día`, `🟡 Cobrar Pronto`, `🔴 Vencido`) y enlace `wa.me` pre-llenado con normalización internacional de teléfonos (código 57).
    - `GET /api/v1/servers/summary`: Resumen financiero de ingresos brutos USD/COP, costos de host USD, ganancia neta total y reparto societario **50/50 (Cristian & Víctor)**.
    - `GET /api/v1/servers/{id}/delivery-message`: Generador automático del mensaje de entrega *"Llave en Mano"* con IP:Puerto, puerto de voz, panel Pterodactyl y optimizaciones aplicadas según el juego.
    - `POST /api/v1/utils/sync-excel`: Sincronización bajo demanda con el Excel CRM desde la API.
  - **Panel Web Operativo `/admin` (`backend/app/api/routes/admin_ui.py` y `backend/app/main.py`):** Interfaz web oscura (*glassmorphism*) autocontenida con login JWT, tarjetas KPI en vivo, tabla de clientes/servidores con semáforo de cobros, recordatorio WhatsApp a 1 clic, modal de acta de entrega *"Llave en Mano"* con copia robusta al portapapeles y botón de sincronización con Excel.
  - **Cobertura Completa de Tests (`backend/tests/api/routes/test_clients.py` y `test_servers.py`):** Se añadieron 15 pruebas nuevas cubriendo CRUD de clientes/servidores, cascada `ON DELETE CASCADE`, `409 Conflict`, `/expiring`, `/summary`, `/delivery-message`, normalización telefónica, extracción de puertos de voz, `/sync-excel`, upsert multiserver y `/admin`, alcanzando **62 pruebas pasando al 100%**.
- **Pilar 3 — Conversión Interactiva en la Landing Page (`index.html`):**
  - **Recomendador de RAM + Cotizador "Arma tu Servidor" en Vivo (`#cotizador`):** Selector interactivo de los 7 juegos del catálogo, slider de jugadores (`2` a `30+`), nivel de mods y checkboxes de Add-ons con cálculo en tiempo real en USD y COP dinámico (`aria-live="polite"`, 100% ES5) y CTA directo a WhatsApp con el resumen exacto.
  - **Vitrina Técnica Interactiva de Optimización "Llave en Mano" (`#optimizacion`):** Pestañas accesibles por juego mostrando las configuraciones reales del kit `plantillas_kinetic/` aplicadas en cada servidor frente a un hosting genérico sin configurar.

## [1.8.2] - 2026-10-12 - Professional Repository, Templates & Backend Directory Organization
### Cambios y Mejoras
- **Reorganización Profesional de `plantillas_kinetic/`:**
  - Se separaron los paquetes listos para producción de las carpetas fuente editables y se clasificaron por ecosistema para eliminar la mezcla de 27 elementos en un mismo nivel:
    - **`paquetes_zip/minecraft/`**: Los 7 archivos `.zip` de Minecraft (`Paper 1.21`, `Paper 1.20.1`, `Paper Legacy 1.16.5-1.18.2`, `Purpur`, `Fabric`, `Forge/NeoForge`, `Velocity Proxy`) listos para subir con `Unarchive` en Kinetic Panel.
    - **`paquetes_zip/otros_juegos/`**: Los 6 archivos `.zip` del resto del catálogo (`Project Zomboid`, `Palworld`, `Rust`, `Valheim`, `Terraria`, `Core Keeper`).
    - **`codigo_fuente/minecraft/` y `codigo_fuente/otros_juegos/`**: Las 13 carpetas fuente desempaquetadas con sus configuraciones y catálogos `MODS_RECOMENDADOS_*.txt` / `PLUGINS_RECOMENDADOS_*.txt`.
    - **`scripts/empaquetar_plantillas.py`**: Script automatizado con `logging` UTF-8 que empaqueta y verifica la integridad de los 13 archivos `.zip`, garantizando rutas POSIX (`/`) en la raíz del contenedor `/home/container` y normalización/validación estricta de saltos de línea `LF` en scripts `.sh`.
    - **`plantillas_kinetic/README.md` y `GUIA_RAPIDA_KINETIC_SOP.md`**: Índice de navegación rápida y actualización de rutas en el Manual Operativo Maestro.
- **Estandarización y Limpieza de `backend/`:**
  - **Restauración UTF-8 de `backend/README.md`:** Se reparó la corrupción de caracteres UTF-16 (mojibake) en el archivo `backend/README.md`, documentando en español la arquitectura, comandos de desarrollo en Windows, migraciones Alembic y suite de pruebas.
  - **Centralización en `backend/scripts/`:** Se trasladaron los scripts operativos sueltos (`import_data.py` y `fix_emails.py`) desde la raíz de `backend/` hacia `backend/scripts/`, refactorizándolos con tipado estricto (`mypy`), `logging` estándar con salida UTF-8 (cumpliendo la regla `T201` de `ruff`) y resolución dinámica de rutas (`pathlib.Path`).
  - **Resolución Robusta de `.env` y SQLite (`backend/app/core/config.py` y `backend/pyproject.toml`):** Se actualizó `Settings` para resolver tanto `.env` como las rutas relativas de SQLite (`sqlite:///./consterna.db`) respecto al directorio `backend/`, evitando la creación de bases de datos huérfanas al ejecutar comandos desde otros directorios (`C:\dev`), y se configuró `[tool.ruff.lint.isort]` (`known-first-party`) y `[tool.pytest.ini_options]`, pasando `ruff check`, `ruff format --check` y `mypy` en los 36 archivos Python del repositorio.
  - **Saltos de Línea LF en Scripts y Docker (`Dockerfile`, `compose.yml`, `backend/scripts/*.sh`):** Se normalizaron los saltos de línea a formato Unix (`LF`) conforme a `AGENTS.md`.
- **Organización de la Raíz del Proyecto (`consterna-cloud/`):**
  - Se trasladó y renombró el activo gráfico suelto `consterna_discord_icon_1790741212921.jpg` hacia **`assets/brand/consterna-discord-icon.jpg`**, preservando intactos en la raíz los activos requeridos por **Cloudflare Pages** (`index.html`, `banner_whatsapp.jpg`, `robots.txt`, `sitemap.xml`).
  - Se añadió la plantilla segura **`.env.example`** documentando las variables de entorno del proyecto y se actualizó **`.gitignore`** con soporte recursivo `!plantillas_kinetic/**/*.zip` y exclusión global de `*.db` y `*.pyc`.

## [1.8.1] - 2026-10-12 - Verified Recommended Mods & Plugins Guides Across All 13 Game & Loader Templates
### Cambios y Mejoras
- **Guías de Plugins y Mods Recomendados en las 7 Plantillas de Minecraft (`codigo_fuente/minecraft/` y paquetes `.zip`):**
  - Se crearon `PLUGINS_RECOMENDADOS_PAPER.txt` (`paper-1.21-optimizado/` y `paper-1.20.1-optimizado/`), `PLUGINS_RECOMENDADOS_PAPER_LEGACY.txt` (`paper-legacy-1.16.5-1.18.2/`), `PLUGINS_RECOMENDADOS_PURPUR_PUFFERFISH.txt` (`purpur-optimizado/`) y `PLUGINS_RECOMENDADOS_VELOCITY.txt` (`velocity-proxy-optimizado/`).
  - Se ampliaron `MODS_RECOMENDADOS.txt` (Fabric/Quilt) y `MODS_RECOMENDADOS_FORGE_NEOFORGE.txt` (Forge/NeoForge) con la tabla de reemplazos server-side de plugins (*LuckPerms*, *FTB Essentials/Chunks/Ranks*, *Ledger*, *StyledChat*, *Universal Graves*) y el Paso 4 de vinculación con Velocity mediante *Proxy Compatible Forge (PCF)* y *CrossStitch*.
- **Guías de Mods y Plugins Verificados en los 6 Juegos Restantes del Catálogo (`codigo_fuente/otros_juegos/` y paquetes `.zip`):**
  - **`MODS_RECOMENDADOS_ZOMBOID.txt` (`zomboid-coop-latam/`):** IDs exactos `WorkshopItems=` y `Mods=` verificados contra Steam Workshop listos para copiar y pegar (optimización anti-lag *Rain Cleans Blood* `2956146279`, *Udderly Up To Date* `2844315442`, *Clean Dirt* `2711057211`; pack QoL con *Skill Recovery Journal* `2503622437`, *Common Sense* `2875848298`, *Weapon Condition Indicator* `2619072426` / `TheStar`, *Has Been Read* `2544353492` / `P4HasBeenRead`, *Minimal Display Bars* `2004998206`, *Proximity Inventory* `2847184718`, *Generator Time Remaining* `2883397918`, *More Description for Traits* `2685168362` con sufijos B41 `MoreDescriptionForTraits4166` y B42 `MoreDescriptionForTraits42`, *True Actions* `2487022075` / `TMC_TrueActions`, *Filibuster Rhymes' Used Cars* `1510950729`, *Autotsar Trailers* `2282429356`, *RV Interior* `2822286426` y comparativa de RAM entre *Vanilla Firearms Expansion* vs *Brita's Weapon Pack*).
  - **`MODS_RECOMENDADOS_PALWORLD.txt` (`palworld-optimizado/`):** Diferenciación técnica entre ajustes nativos crossplay (`PalWorldSettings.ini`), mods `.pak`, mods `UE4SS`, mods Client-Side y administración vía REST API oficial.
  - **`PLUGINS_RECOMENDADOS_RUST.txt` (`rust-optimizado/`):** Comparativa técnica **Carbon Framework vs Oxide/uMod** y catálogo de plugins `.cs` (*Vanish*, *Admin Radar*, *Gather Manager*, *Stack Size Controller*, *Quick Smelt*, *Furnace Splitter*, *Clans*, *NTeleportation*, *No Escape*, *Remover Tool*, *Kits* y *Better Chat*).
  - **`MODS_RECOMENDADOS_VALHEIM.txt` (`valheim-optimizado/`):** Guía de **BepInExPack**, optimización de red con **BetterNetworking**, seguridad anti-cheats con **ServerCharacters** y **WardIsLove**, y mods con **ServerSync** (*AzuCraftyBoxes*, *AzuExtendedPlayerInventory*, *CLLC + EpicLoot* y *Grantapher ValheimPlus*).
  - **`MODS_Y_PLUGINS_RECOMENDADOS_TERRARIA.txt` (`terraria-optimizado/`):** Ecosistema de plugins **TShock** (*Server-Side Characters*, *WorldEdit*, *History*) y tabla lista para copiar de `install.txt` + `enabled.json` en **tModLoader 1.4.4+** incluyendo dependencias obligatorias de librerías (`SerousCommonLib` `2908170107` para *Magic Storage* y `SubworldLibrary` `2785100219` / `Luminance` `3222496602` para *Infernum* y *Wrath of the Gods*).
  - **`MODS_RECOMENDADOS_CORE_KEEPER.txt` (`core-keeper-optimizado/`):** Integración oficial **`mod.io`** y **BepInEx**, diferenciando mods Client-Side (*PlacementPlus*, *AutoFish*, *AutoDoors*) de mods cooperativos (*InstantPortalCharge*, *Infinite Ore Boulder*).

## [1.8.0] - 2026-10-12 - Complete 13-Template Kinetic Catalog (All Minecraft Loaders/Versions/Proxies + All 7 Flagship Games)
### Cambios y Mejoras
- **Análisis Técnico y Documentación de `pause-when-empty-seconds` (`Minecraft 1.21.2+`):**
  - Se documentó en `server.properties` y en `GUIA_RAPIDA_KINETIC_SOP.md` el impacto exacto de congelar el *world tick loop* (`pause-when-empty-seconds`), estableciendo una matriz clara de cuándo mantenerlo desactivado (`-1` o `0`: servidores con plugins, timers, mapas web *BlueMap/Dynmap*, granjas en *Spawn Chunks*, *Ender Pearl Stasis Chambers*, *Nether Portal Chunk Loaders*, mods técnicos como *Create/Mekanism/AE2* con *FTB Chunks force-loading* y tareas nocturnas de *Chunky*) y cuándo activarlo (`60`: servidores casuales de amigos por horario o modpacks con estaciones como *Serene Seasons* / *Fabric Seasons* tras finalizar *Chunky*).
- **Cobertura Total de Motores, Modloaders, Versiones y Proxies de Minecraft en `plantillas_kinetic/`:**
  - **`paper-legacy-1.16.5-1.18.2/` (`Plantilla-Configs-Paper-Legacy-1.16.5-1.18.2.zip` — NUEVA):** Plantilla específica para servidores `1.16.5`, `1.17.1` y `1.18.2` con el archivo monolítico **`paper.yml`** en la raíz (`config-version: 20` auto-migrable a `24`/`25`, `eigencraft-redstone`, `per-player-mob-spawns: true`, `max-auto-save-chunks-per-tick: 8`, `delay-chunk-unloads-by: 10s`, `optimize-explosions: true`, `anti-xray` modo 1), `bukkit.yml`, `spigot.yml`, `server.properties` y `plugins/voicechat/voicechat-server.properties`.
  - **`purpur-optimizado/` (`Plantilla-Configs-Purpur.zip` — NUEVA):** Incluye **`purpur.yml`** verificado contra `PurpurConfig.java` y `PurpurWorldConfig.java` (`settings.use-alternate-keepalive: true` para evitar desconexiones por micro-pérdida de paquetes en LATAM, `world-settings.default.mobs.villager.lobotomize.enabled: true` con `wait-until-trade-locked: true` para aldeanos en trading halls 1x1 sin romper granjas de hierro ni rerolls de atriles, `gameplay-mechanics.use-better-mending: true` y `gameplay-mechanics.player.teleport-if-outside-border: true`) y **`pufferfish.yml`** (`enable-async-mob-spawning: true`, `enable-suffocation-optimization: true` y `dab.enabled: true` con `minecraft:villager`, `minecraft:iron_golem` y `minecraft:zombified_piglin` en `blacklisted-entities`), más todo el stack de Paper y Simple Voice Chat.
  - **`velocity-proxy-optimizado/` (`Plantilla-Velocity-Proxy.zip` — NUEVA):** Configuración `velocity.toml` (`config-version = "2.7"`, `player-info-forwarding-mode = "modern"`, `compression-threshold = 256`, `tcp-fast-open = true`, `login-ratelimit = 3000`, `failover-on-unexpected-server-disconnect = true`) junto a `GUIA_VINCULACION_VELOCITY.txt` paso a paso para enlazar Velocity con Paper/Purpur (`config/paper-global.yml` + `network-compression-threshold=-1`), Fabric/Quilt (*FabricProxy-Lite*) y Forge/NeoForge (*Proxy Compatible Forge / PCF* + *CrossStitch*).
  - **Matriz por Versión en `fabric-optimizado/` y `forge-neoforge-optimizado/`:** Se ampliaron `MODS_RECOMENDADOS.txt` y `MODS_RECOMENDADOS_FORGE_NEOFORGE.txt` detallando el stack exacto para `1.21.1+`, `1.20.1`, `1.18.2 / 1.19.2` y `1.16.5` (cuándo usar *Starlight* y *LazyDFU* en versiones pre-1.20 vs iluminación nativa de Mojang en 1.20+, soporte de **Quilt** con *QFAPI*, *RoadRunner* en Forge 1.16.5, *Canary/Radium* en Forge 1.18–1.20.1 y *Lithium* oficial en NeoForge 1.21.1+, además de documentar por qué *ModernFix* usa siempre `config/modernfix-mixins.properties` en todos los loaders mientras *FerriteCore* usa `config/ferritecore-mixin.toml` en Forge/NeoForge).
  - **Tabla Maestra de Motores, Modloaders, Híbridos y Proxies en `GUIA_RAPIDA_KINETIC_SOP.md`:** Comparativa técnica exhaustiva de Vanilla, CraftBukkit/Spigot, Paper, Pufferfish, Purpur, Folia, Fabric, Quilt, Forge, NeoForge, Sponge (`SpongeForge`/`SpongeNeo`), Proxies (**Velocity**, **BungeeCord**, **Waterfall**) y advertencia técnica sobre por qué evitar motores híbridos inestables (*Mohist/Arclight/Magma/Banner/Ketting*) usando en su lugar mods server-side nativos (*LuckPerms*, *FTB Essentials/Chunks/Ranks*, *Ledger*, *StyledChat*, *Universal Graves*) o *Sinytra Connector*.
- **Nuevas Plantillas Optimizadas para los 5 Juegos Principales Restantes de Consterna Cloud:**
  - **`palworld-optimizado/` (`Plantilla-Palworld-Optimizado.zip`):** Incluye `Pal/Saved/Config/LinuxServer/PalWorldSettings.ini` (respetando la regla estricta de 2 líneas sin saltos: `ServerReplicatePawnCullDistance=12000.000000`, `bAutoResetGuildNoOnlinePlayers=True`, `AutoResetGuildTimeNoOnlinePlayers=72.000000`, `bBuildAreaLimit=True`, `DropItemMaxNum=1500`), `Pal/Saved/Config/LinuxServer/Engine.ini` (`NetServerMaxTickRate=60`) y `LEEME_PALWORLD.txt`.
  - **`rust-optimizado/` (`Plantilla-Rust-Optimizado.zip`):** Incluye `server/rust/cfg/server.cfg` (`fps.limit 60`, `server.tickrate 30`, `gc.buffer 2048`, `server.saveinterval 300`, `ai.think true`) y `LEEME_RUST.txt`.
  - **`valheim-optimizado/` (`Plantilla-Valheim-Optimizado.zip`):** Incluye `adminlist.txt`, `permittedlist.txt`, `bannedlist.txt`, `start_server_consterna.sh` y `LEEME_VALHEIM.txt` (Direct UDP vs `-crossplay` PlayFab en LATAM y modificadores nativos).
  - **`terraria-optimizado/` (`Plantilla-Terraria-Optimizado.zip`):** Incluye `serverconfig.txt` (`npcstream=60`, `secure=1`, `upnp=0`, `priority=1`, `autocreate=2`) y `LEEME_TERRARIA.txt`.
  - **`core-keeper-optimizado/` (`Plantilla-CoreKeeper-Optimizado.zip`):** Incluye `ServerConfig.json` (`networkSendRate: 30`, `maxNumberPacketsSentPerFrame: 2`, `maxNumberPlayers: 8`, `worldMode: 0`, `seasonOverride: -1`) y `LEEME_CORE_KEEPER.txt`.


## [1.7.0] - 2026-10-12 - Realistic Delivery SLAs, Discord Consultation Hub & Kinetic Templates
### Cambios y Mejoras
- **Alineación Realista de Tiempos de Entrega ("Llave en Mano" vs. Instantáneo Vacío):**
  - Se actualizaron las metaetiquetas `og:description` y `twitter:description` eliminando la promesa irreal *"¡listo para jugar en minutos!"* por *"Te entregamos tu servidor 100% configurado y optimizado (modpacks, Voice Chat y mapa pre-generado)..."*.
  - Se reemplazó el primer Trust Badge del Hero (*"Entrega Lista para Jugar"* con ícono de rayo) por **"Entregado 100% Configurado"** con ícono de verificación (`check-circle` verde).
  - En la sección de Pagos Colombia (`#pagos`), se ajustó *"Confirmación al instante sin recargos"* por **"Verificación inmediata de tu pago sin recargos"** para evitar confusiones con el tiempo de preparación técnica.
  - En el **FAQ 1 (`¿Cómo y cuándo me entregan el servidor?`)**, se detalló explícitamente tanto el *cuándo* como el *cómo*: a diferencia de los hostings automáticos que entregan una máquina vacía, Consterna Cloud prepara el servidor de forma personalizada **"Llave en Mano"**, tomando habitualmente entre **30 y 90 minutos** una vez confirmado el pago dentro del horario de atención (**10:00 AM a 10:00 PM GMT-5**), según el peso del modpack y la pre-generación inicial del mundo con Chunky.
- **Potenciación de Discord como Canal Oficial de Consultas, Tickets y Comunidad (`https://discord.gg/PhsZEfc4KE`):**
  - Se transformó la sección `#comunidad` en un **Hub Oficial de Discord y Comunidad** con 3 tarjetas de valor: **Consultas y Asesoría Pre-venta**, **Soporte Técnico por Tickets** y **Comunidad, Estado y Eventos**, manteniendo contraste WCAG 2.1 AA (`text-indigo-400` >= 6.7:1 sobre fondo oscuro).
  - Se añadió el botón secundario **"Consultar en Discord"** junto a WhatsApp en el Banner de Asesoría de RAM (`¿No estás seguro de cuánta RAM necesita tu servidor?`), además de destacar la atención por WhatsApp y Discord en el Hero, FAQ 2 y Footer.
- **Kit de 5 Plantillas Maestras Pre-Optimizadas para Kinetic Panel (`plantillas_kinetic/`):**
  - **Auditoría contra Código Fuente Oficial (Zero-Hallucination):** Verificación de cada clave contra `PaperMC/Paper`, `malte0811/FerriteCore` (`FerriteConfig.java`), `henkelmax/simple-voice-chat` (`ServerConfig.java`), `CaffeineMC/lithium` y `embeddedt/ModernFix`. Se fijó `pause-when-empty-seconds=-1` en `server.properties` para evitar que la pausa automática de Minecraft 1.21.2+ congele plugins, granjas o la tarea nocturna de Chunky a las 04:00 AM.
  - **`paper-1.21-optimizado/` y `Plantilla-Configs-Paper-1.21.zip`:** Configuraciones afinadas para Paper/Purpur `1.21.1–1.21.4+` (`bukkit.yml`, `spigot.yml`, `server.properties`, `config/paper-global.yml` con esquema `_version: 29` puro y Spark integrado, `config/paper-world-defaults.yml` con `_version: 31`, `ALTERNATE_CURRENT`, `per-player-mob-spawns: true`, `short_grass: 300`, `wind_charge`/`breeze_wind_charge`, `anti-xray` modo 1 y `plugins/voicechat/voicechat-server.properties`).
  - **`paper-1.20.1-optimizado/` y `Plantilla-Configs-Paper-1.20.1.zip`:** Variante específica para Paper/Purpur `1.20.1–1.20.4` adaptada al esquema real de 1.20.1 (`_version: 28` en `paper-global.yml` y `_version: 30` en `paper-world-defaults.yml`, usando `grass: 300` en lugar de `short_grass` y sin entidades exclusivas de 1.21 para evitar warnings en consola).
  - **`fabric-optimizado/` y `Plantilla-Configs-Fabric-1.21.zip` (Compatible con Fabric 1.20.1 y 1.21.x):** Incluye `server.properties`, `config/lithium.properties`, `config/ferritecore.mixin.properties` (con las claves exactas de `FerriteConfig.java`: `replaceNeighborLookup`, `replacePropertyMap`, `cacheMultipartPredicates`, `modelResourceLocations`, `multipartDeduplication`, `blockstateCacheDeduplication`, `bakedQuadDeduplication`), `config/modernfix-mixins.properties` (`mixin.perf.dynamic_resources=true`), `config/voicechat/voicechat-server.properties` (`max_voice_distance=48.0`, `whisper_distance=24.0`, `mtu_size=1024`, `codec=VOIP`) y `MODS_RECOMENDADOS.txt`.
  - **`forge-neoforge-optimizado/` y `Plantilla-Configs-Forge-NeoForge.zip` (Compatible con Forge 1.20.1 y NeoForge 1.21.x):** Diseñada para modpacks pesados (*All The Mods 9/10*, *Create*, *Prominence II*, *RLCraft Dregora*) con `max-tick-time=180000`, `config/ferritecore-mixin.toml` (formato TOML requerido por FerriteCore en Forge/NeoForge), `config/modernfix-mixins.properties`, `config/canary.properties` (con `mixin.ai.poi=false` para Forge 1.20.1), `config/lithium.properties` (para NeoForge 1.21.1+), `config/voicechat/voicechat-server.properties` y `MODS_RECOMENDADOS_FORGE_NEOFORGE.txt`.
  - **`zomboid-coop-latam/` y `Plantilla-Zomboid-Coop-LATAM.zip`:** Configuraciones `servertest.ini` y `servertest_SandboxVars.lua` afinadas para cooperativo y comunidades en LATAM (`PingLimit=350`, `KickFastPlayers=false`, `PauseEmpty=true`, `SaveWorldEveryMinutes=15`, `BackupsCount=5`, limpieza automática de basura en el suelo cada 24h in-game y reducción de manchas de sangre para proteger la RAM).
  - **`GUIA_RAPIDA_KINETIC_SOP.md`:** Manual operativo con Matriz de Decisión por versión y modloader (`1.20.1` vs `1.21.x` y `Paper` vs `Fabric` vs `Forge/NeoForge`), despliegue vía *Unarchive*, *Simple Voice Chat* (*Quick Setup* + *Open Port*), *Aikar's Flags* y el **Truco de las 2 Fases con Chunky**.
  - Se actualizó `.gitignore` (`!plantillas_kinetic/*.zip`) para permitir versionar los paquetes `.zip` de `plantillas_kinetic/`.

## [1.6.1] - 2026-10-12 - "Llave en Mano" Core Value Proposition & Healthy Add-on Boundaries (Camino 1)
### Cambios y Mejoras
- **Restauración de la Esencia "Llave en Mano" en Planes Base (`#planes`, Hero, Trust Bar, `#beneficios`, `#faq`, `#footer`):** Todos los planes (4 GB a 16 GB Dedicado) vuelven a incluir explícitamente la configuración inicial lista para entrar a jugar: instalación del juego o modpack público elegido (CurseForge, Modrinth, Steam Workshop), configuración de puertos (como *Simple Voice Chat*), optimización de argumentos de memoria, pre-generación con Chunky en Minecraft, acceso total al panel de control y soporte técnico de arranque/estabilidad.
- **Límites Sanos en los 3 Servicios Adicionales (`#addons`):** Redefinición de los Add-ons para enfocarse en trabajo pesado a medida o continuo sin chocar con el plan base: **Creación de Modpacks / Eventos a Medida** (`$5.00 USD` pago único para diseñar, combinar y testear desde cero un modpack propio o evento a medida), **Sysadmin Dedicado Mensual** (`$6.00 USD/mes` para contar con un administrador técnico de cabecera todo el mes que agregue/quite mods constantemente, configure permisos, repare crashes por ediciones manuales, gestione wipes y realice mantenimiento continuo) e **IP Dedicada Exclusiva** (`$4.00 USD/mes` con puerto por defecto ej. `25565`), actualizando también sus enlaces dinámicos de WhatsApp (`?text=...`) y alineando alturas de títulos, precios, insignias (`whitespace-nowrap`) e íconos CTA (`flex-shrink-0`) en tablet (`md:`) y desktop (`lg:`).
- **Horario y Soporte sin Contradicciones:** Distinción transparente entre la infraestructura, red y mitigación DDoS activas **24/7** y el horario de atención y soporte humano directo por WhatsApp (**Lunes a Domingo de 10:00 AM a 10:00 PM GMT-5**).

## [1.6.0] - 2026-10-12 - Business Model Alignment, Add-ons Monetization & QA Audit
### Cambios y Mejoras
- **Modelo Infraestructura + Add-ons:** Alineación integral de textos en Hero, Beneficios, Planes, FAQ y Footer diferenciando claramente la infraestructura/monitoreo 24/7 de la atención humana directa por chat (Lunes a Domingo, 10:00 AM a 10:00 PM GMT-5) y los servicios adicionales.
- **Catálogo de Add-ons Completo (`#addons`):** Se añadieron precios en USD y COP dinámico (`$5.00 USD`, `$6.00 USD/mes`, `$4.00 USD/mes`), interactividad hover y botones CTA directos a WhatsApp, además de enlazar la sección en el Navbar Desktop y Mobile en el orden exacto del DOM (`lg:` breakpoint con `whitespace-nowrap` para prevenir colisiones en resoluciones tablet `768px-1023px`).
- **Simetría en Planes por RAM (`#planes`):** Estandarización total de las 5 tarjetas (4 GB a 16 GB) con 4 viñetas estrictamente simétricas y progresivas, ajuste del precio inicial estático del Tier 4 GB a `~$34.000 COP` y aclaración de capacidad recomendada.
- **Precisión Técnica y Geográfica:** Aclaración del uso de Chunky en Minecraft y lectura NVMe PCIe en Project Zomboid, especificación de baja latencia (`~70-85ms` en LATAM) vía nodos estratégicos en Miami/EE.UU., y retiro de marcas de terceros obsoletas ("Pro Hosting").
- **Accesibilidad (WCAG 2.1 AA) y Resiliencia JS (ES5):** Adición de `aria-label` en todos los enlaces de solo ícono, `aria-labelledby` en las regiones de respuesta del FAQ, contraste mínimo >= 4.5:1 (`text-zinc-400`) en textos secundarios, recálculo de altura del acordeón FAQ en `resize`, refactorización de todos los scripts interactivos a ES5 estricto con fallback real para `IntersectionObserver` y `noscript`, y validación defensiva (`isFinite` + traversal `parentNode`) en el cálculo cambiario TRM.
- **Higiene del Repositorio:** Eliminación de archivos residuales temporales (`full_diff.txt`, `git_diff_check.txt`, `index.zip`, `update_docs.py`) y endurecimiento de `.gitignore`.

## [1.5.0] - Dynamic Pricing Automation
### Cambios y Mejoras
- **Script Cambiario Automático:** Se implementó un script en index.html que consulta la API de tasas de cambio para calcular automáticamente el precio en COP del plan base según la TRM actual, protegiendo los márgenes de ganancia. Cuenta con caché de 24h vía localStorage y mecanismo de fallback seguro.


## [1.4.0] - SEO, Conversion & SVG Legacy Support
### Cambios y Mejoras
- **Iconos SVG y Legacy:** Se optimizaron los iconos SVG creando un Sprite y se agregó compatibilidad legacy estricta (`xlink:href`) para dispositivos móviles antiguos.
- **SEO & Rich Snippets:** Inyección de JSON-LD Schema (con `AggregateRating` y enfoque de Servicio) para mejorar la visibilidad de Rich Snippets en Google. Adicionalmente se optimizó la etiqueta H1 y la `<meta name="description">`.
- **Conversiones (Trust Badges):** Se añadió un bloque de insignias de confianza (Trust Badges: Setup Instantáneo, Protección DDoS, Soporte 24/7) debajo del Call-To-Action principal para maximizar la tasa de conversión.
- **Sistema Anti-FOUC:** Corrección de fallos en la implementación previa del script.

## [1.3.0] - Cross-Browser Resilience & UI Symmetry
### Cambios y Mejoras Técnicas
- **Soporte Legacy y Anti-FOUC:** Refactorización a ES5 estricto del script Anti-FOUC para prevenir errores de sintaxis en navegadores ultra-legacy (ej. Opera) que causaban pantalla blanca infinita.
- **Simetría Visual:** Balance de simetría visual drástico acortando los textos de "Nodos Globales" y "Latencia Ultra Estable".
- **Semántica W3C:** Corrección final de salto de jerarquía semántica `<h3>` a `<h2>` en el banner de asesoría.
- **Responsive Extremo:** Adición de soporte `break-words` en el `<body>` para prevenir overflow horizontal en resoluciones extremas de 280px (Mobile).

## [1.2.1] - Extreme QA & Accessibility Audit
### Cambios y Reparaciones
- **Reparación de Enlaces:** Se reemplazaron enlaces ancla muertos (`href="#"` -> `href="/"`) en la cabecera y el footer.
- **SEO Enterprise:** Inyección de etiqueta canónica `<link rel="canonical" href="https://consterna-cloud.pages.dev/">`.
- **Accesibilidad (A11y):** Resolución de falla de contraste de color en el botón principal del Hero (`text-white` a `text-zinc-950`).
- **Jerarquía Semántica:** Ajuste estructural cambiando varios `<h3>` a `<h2>` en la sección "Trust Bar" para cumplir estrictamente con los estándares W3C.

## [1.2.0] - Global Expansion & Managed Service Pivot
### Cambios y Añadidos
- **Copywriting estratégico:** Se ajustaron los textos del sitio para reflejar que somos un Managed Service/Reseller utilizando infraestructura de hardware de partners líderes.
- **Expansión de Nodos Globales:** Se actualizó la lista de regiones soportadas (Norteamérica, Europa, Asia/Oceanía), incluyendo soporte explícito y rutas optimizadas para Argentina y el Cono Sur.

## [1.1.1] - Backend & SEO Enhancements
### Cambios y Añadidos
- **Backend FastAPI (Fase 2):** Implementación de backend con FastAPI, migraciones de base de datos con Alembic, validación estricta de UUID y codificación de emails.
- **A11y:** Se agregó la etiqueta semántica `<main>` para mejor indexación y compatibilidad con lectores de pantalla.
- **Social Cards:** Se añadieron meta etiquetas de Twitter Card y dimensiones a imágenes para optimizar las previsualizaciones en Discord y WhatsApp.
- **SEO y Cloudflare Pages:** Se actualizaron las URLs SEO y OG para ajustarse a la nueva infraestructura en Cloudflare Pages.
- **Correcciones Varias:** Arreglo de codificación en `.gitignore` para excluir archivos Excel.

## [1.1.0] - 2026-10-02
### Añadido y Reparado
- **Sistema Anti-FOUC (Flash of Unstyled Content):** Se implementó un MutationObserver y una etiqueta `<noscript>` para garantizar que la página nunca se muestre rota o desestilizada antes de cargar TailwindCSS en conexiones móviles o navegadores lentos.
- **Favicon Base64:** El ícono de la nube del sitio web ha sido codificado en formato Base64 para prevenir vulnerabilidades de parseo HTML en motores como Opera PC y navegadores móviles.
- **Prevención de Layout Shift:** Se añadieron tamaños estáticos nativos (atributos width y height) a todos los íconos SVG del proyecto para evitar parpadeos visuales al renderizar la página.
- **Corrección de Codificación (Mojibake):** Se restauraron los caracteres del idioma español en el archivo index.html a formato UTF-8 estricto.

## [1.0.0] - Lanzamiento Inicial
### Añadido
- Landing Page interactiva para Consterna Cloud.
- Optimización completa de Accesibilidad (A11y) con etiquetas ARIA.
- Archivos SEO técnicos (`robots.txt` y `sitemap.xml`) configurados para Cloudflare Pages.
