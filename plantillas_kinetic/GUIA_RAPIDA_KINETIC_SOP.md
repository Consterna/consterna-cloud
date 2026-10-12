# 🛠️ Manual Operativo (SOP): Entrega "Llave en Mano" en Kinetic Panel
**Versión:** Octubre 2026 (Actualizado y Auditado al 12 de octubre de 2026)  
**Uso Interno:** Guía paso a paso para **Cristian y Víctor** en **Consterna Cloud**  
**Objetivo:** Entregar cualquier servidor 100% configurado, optimizado y con mapa pre-generado dentro de nuestro SLA prometido (**30 a 90 minutos**), reduciendo el trabajo manual repetitivo a menos de **5 minutos de clics efectivos**.

---

## 🧭 Matriz de Decisión: ¿Qué cambia entre Versiones de Minecraft y qué Plantilla usar?

Una duda muy común al operar un hosting es: ***"¿Necesitamos una plantilla distinta por cada versión de Minecraft (1.20.1, 1.20.4, 1.21.1, 1.21.4)?"***  
La respuesta técnica real (verificada contra el código fuente de PaperMC, Fabric, Forge y NeoForge) es:

1. **En Servidores con Mods (`Fabric`, `Forge`, `NeoForge`): NO cambia por versión (`1.20.1` vs `1.21.x`), sino por MODLOADER.**
   - **Fabric (`1.20.1` y `1.21.x`):** Los mods de optimización (**Lithium**, **FerriteCore**, **ModernFix** y **Simple Voice Chat**) leen exactamente las mismas rutas y claves en `1.20.1` y en `1.21.x` (`config/lithium.properties`, `config/ferritecore.mixin.properties`, `config/modernfix-mixins.properties` y `config/voicechat/voicechat-server.properties`). Por eso, **una sola plantilla de Fabric sirve para 1.20.1 y 1.21.x**.
   - **Forge (`1.20.1`) y NeoForge (`1.21.x`):** En el ecosistema Forge/NeoForge (donde viven modpacks pesados como *All The Mods 9/10*, *Prominence II*, *Create*, *RLCraft Dregora*), **FerriteCore** NO lee archivos `.properties`, sino un archivo TOML (**`config/ferritecore-mixin.toml`**). Además, en Forge 1.20.1 se usa **Canary** (`config/canary.properties`) y en NeoForge 1.21.1+ ya existe **Lithium oficial** (`config/lithium.properties`). Nuestra plantilla **`forge-neoforge-optimizado`** incluye ambos archivos para que sirva **tanto en Forge 1.20.1 como en NeoForge 1.21.x** sin tocar nada.

2. **En Servidores con Plugins (`Paper` / `Purpur`): SÍ cambia entre `1.21.x` y `1.20.1`.**
   - En **Paper 1.21.x**, `config/paper-world-defaults.yml` usa el esquema `_version: 31`, el ítem de pasto corto se llama `short_grass: 300` (renombrado por Mojang en 1.20.3+), existen los proyectiles `wind_charge` y `breeze_wind_charge`, y **Spark** ya viene integrado nativamente dentro de `paper-global.yml` (`_version: 29`).
   - En **Paper 1.20.1**, el esquema es `_version: 30` y el ítem todavía se llamaba **`grass: 300`** (si subes la plantilla de 1.21 en un Paper 1.20.1, dará advertencia en consola porque `short_grass` y `wind_charge` no existían en 1.20.1). Por eso tenemos dos plantillas separadas para Paper: **`1.21+`** y **`1.20.1`**.
   - *(Nota sobre versiones muy antiguas como `1.16.5` o `1.18.2`: esas versiones antiguas no usaban la carpeta `config/paper-world-defaults.yml`, sino un único archivo `paper.yml` en la raíz. Si algún cliente pide 1.16.5/1.18.2, solo sube `bukkit.yml`, `spigot.yml` y `server.properties` y deja que Paper genere su propio `paper.yml`).*

---

## 📦 Resumen de las 5 Plantillas Maestras (`.zip`)

En esta carpeta (`plantillas_kinetic/`) tienes listas las 5 plantillas comprimidas para arrastrar directamente al **File Manager** de Kinetic Panel:

| # | Archivo `.zip` (y Carpeta Fuente) | ¿Cuándo usarla? | Qué configura y optimiza automáticamente |
| :--- | :--- | :--- | :--- |
| **1** | **`Plantilla-Configs-Paper-1.21.zip`**<br>*(Carpeta: `paper-1.21-optimizado/`)* | **Paper o Purpur 1.21.1 – 1.21.4+**<br>*(Survival con Plugins moderno)* | `bukkit.yml`, `spigot.yml`, `server.properties` (`pause-when-empty-seconds=-1`), `config/paper-global.yml` (`_version: 29` con Spark activo), `config/paper-world-defaults.yml` (`_version: 31`, `ALTERNATE_CURRENT`, `per-player-mob-spawns: true`, `Anti-Xray Mode 1`) y `plugins/voicechat/voicechat-server.properties`. |
| **2** | **`Plantilla-Configs-Paper-1.20.1.zip`**<br>*(Carpeta: `paper-1.20.1-optimizado/`)* | **Paper o Purpur 1.20.1 – 1.20.4**<br>*(Survival con Plugins 1.20)* | Igual que la de 1.21 pero adaptada al esquema real de Paper 1.20.1 (`_version: 28` y `_version: 30`, `grass: 300` en lugar de `short_grass`, y sin entidades exclusivas de 1.21) más `plugins/voicechat/voicechat-server.properties`. |
| **3** | **`Plantilla-Configs-Fabric-1.21.zip`**<br>*(Carpeta: `fabric-optimizado/`)* | **Fabric 1.20.1 y Fabric 1.21.x**<br>*(Survival Técnico, Series con Voice Chat, Modpacks Fabric como Cobblemon / Prominence II)* | `server.properties` (`pause-when-empty-seconds=-1`), `config/lithium.properties`, `config/ferritecore.mixin.properties` (claves oficiales `FerriteConfig.java`), `config/modernfix-mixins.properties` (`dynamic_resources=true`), `config/voicechat/voicechat-server.properties` (`max_voice_distance=48.0`, `whisper_distance=24.0`, `mtu_size=1024`) y `MODS_RECOMENDADOS.txt`. |
| **4** | **`Plantilla-Configs-Forge-NeoForge.zip`**<br>*(Carpeta: `forge-neoforge-optimizado/`)* | **Forge 1.20.1 y NeoForge 1.21.x**<br>*(Modpacks pesados: All The Mods 9/10, Create, RLCraft Dregora, Better MC Forge)* | `server.properties` (`max-tick-time=180000` anti-crash en carga de modpacks), `config/ferritecore-mixin.toml` (formato TOML de Forge/NeoForge), `config/modernfix-mixins.properties` (`dynamic_resources=true`), `config/canary.properties` (para Forge 1.20.1 con `mixin.ai.poi=false` compatible con Create/Valkyrien Skies), `config/lithium.properties` (para NeoForge 1.21.1+) y `config/voicechat/voicechat-server.properties`. |
| **5** | **`Plantilla-Zomboid-Coop-LATAM.zip`**<br>*(Carpeta: `zomboid-coop-latam/`)* | **Project Zomboid (Co-op / Mods)**<br>*(Todos los planes de Zomboid)* | `servertest.ini` y `servertest_SandboxVars.lua`: `PingLimit=350`, `KickFastPlayers=false` (cero expulsiones injustas al conducir vehículos desde LATAM), `PauseEmpty=true`, `SaveWorldEveryMinutes=15`, `BackupsCount=5`, limpieza automática de basura en el suelo cada 24h in-game (`HoursForWorldItemRemoval = 24.0`) y `BloodLevel = 2` (`Low`). |

---

## ⚡ PASO 1: Cómo aplicar la plantilla en 2 segundos (`Unarchive`)

### A. Para Minecraft (`Paper`, `Fabric`, `Forge` o `NeoForge`)
1. En **Kinetic Panel**, instala primero la versión base desde **Version Installer** (Paper, Fabric, Forge o NeoForge) o el Modpack desde **Modpack Installer**.
2. Inicia el servidor **una sola vez**, acepta el EULA cuando salga el aviso y **apágalo (`Stop`)** apenas termine de generar las carpetas base.
3. Ve a **Management -> File Manager** (asegúrate de estar en la raíz `/home/container`).
4. Arrastra el archivo `.zip` correspondiente de la tabla superior directamente hacia la ventana del File Manager.
5. Haz clic en los **3 puntos (`...`)** a la derecha del archivo `.zip` recién subido y selecciona **`Unarchive`**.
   - ¡Listo! Kinetic Panel sobrescribirá automáticamente `server.properties`, los archivos YAML y las subcarpetas `config/` o `plugins/` en su ubicación exacta.
   - *(Nota si instalaste un Modpack pre-armado de CurseForge/Modrinth: si el modpack tenía un `level-type` especial como `biomesoplenty` en su `server.properties`, verifica que `level-type=` conserve el del modpack).*
6. Borra el archivo `.zip` del File Manager para dejar limpio el directorio del cliente.

### B. Para Project Zomboid
1. Inicia el servidor de Project Zomboid por primera vez hasta que diga `SERVER STARTED` y luego **apágalo (`Stop`)**.
2. En **File Manager**, entra a la ruta: `/.cache/Server/` (si no ves `.cache`, activa mostrar archivos ocultos o verifica la carpeta `Zomboid/Server/`).
3. Arrastra **`Plantilla-Zomboid-Coop-LATAM.zip`** dentro de `/.cache/Server/`, haz clic en los **3 puntos (`...`)** -> **`Unarchive`** y borra el `.zip`.
4. Si el cliente pidió mods de Steam Workshop, abre `servertest.ini` desde el editor de Kinetic Panel y pega los IDs separados por punto y coma en:
   - `Mods=ModID1;ModID2`
   - `WorkshopItems=123456789;987654321`

---

## 🎙️ PASO 2: Configurar Simple Voice Chat en 30 segundos (`Quick Setup` + `Open Port`)

Una de las mayores ventajas de nuestra entrega **"Llave en Mano"** es entregar el chat de voz por proximidad funcionando a la primera (tanto en Mods como en Plugins):

1. Instala el mod o plugin **Simple Voice Chat** desde el **Mod Manager / Plugin Installer** de Kinetic Panel (o súbelo a `/mods` o `/plugins`).
2. En el menú lateral izquierdo de Kinetic Panel, ve a **Network -> Ports** (o **Split Ports / Allocations**).
3. Si ves el botón **Quick Setup**, selecciona **Simple Voice Chat**; o bien haz clic en **`Open Port` / `Create Allocation`** para generar un puerto adicional libre.
4. Copia el número del nuevo puerto secundario asignado (por ejemplo: `25618`). *Nota: NUNCA uses el puerto principal del servidor de Minecraft para Voice Chat.*
5. Ve a **File Manager** y abre el archivo que nuestra plantilla ya dejó preconfigurado:
   - En **Fabric / Forge / NeoForge**: `/config/voicechat/voicechat-server.properties`
   - En **Paper / Purpur**: `/plugins/voicechat/voicechat-server.properties`
6. Busca la línea `port=24454` y cámbiala por el puerto que abriste:
   ```properties
   port=25618
   ```
7. Guarda el archivo (`Save`) e inicia el servidor. Verás en consola: `[voicechat] Voice chat server started at port 25618`.

---

## 🚀 PASO 3: Activar Aikar's Flags en `Startup Flags`

Para evitar que el recolector de basura de Java (Garbage Collector) congele el servidor cada 30 segundos cuando hay muchos mods o jugadores:

1. En el menú lateral de Kinetic Panel, entra a **Settings -> Startup** (o **Startup Parameters**).
2. Busca el selector o casilla de **Startup Flags / JVM Flags**.
3. Selecciona **`Aikar's Flags`** (recomendado para todos los planes de **4 GB, 6 GB, 8 GB y 12 GB** tanto en Java 17 para 1.20.1 como en Java 21 para 1.21.x).
4. *(Opcional para el Plan **Tier 16 GB Dedicado** con Java 21+ en modpacks masivos como All The Mods 9/10)*: Puedes usar **Aikar's Flags** o **Generational ZGC** (`-XX:+UseZGC -XX:+ZGenerational`), que elimina por completo las pausas de recolección de memoria en heaps superiores a 12 GB.

---

## 🌍 PASO 4: El "Truco de las 2 Fases" con Chunky (Entregar rápido y sin Lag)

Pre-generar un radio enorme de 4.000 bloques de golpe antes de entregar tardaría más de 1 hora, retrasando la entrega al cliente. Con el **Truco de las 2 Fases**, entregamos el servidor en **menos de 30 minutos** y el mapa completo se expande solo mientras todos duermen (gracias a que nuestras plantillas tienen `pause-when-empty-seconds=-1` para que el servidor no se congele cuando está vacío):

### Fase 1: Pre-generación Express de Spawn (~4 a 6 minutos)
Con el plugin/mod **Chunky** instalado y el servidor encendido, pega estos comandos uno por uno en la **Console** de Kinetic Panel:

```text
chunky world world
chunky shape square
chunky center 0 0
chunky radius 1500
chunky start
```
- **¿Por qué `radius 1500`?** Genera un área de **3.000 x 3.000 bloques** alrededor del spawn en apenas **4 a 6 minutos** gracias al Ryzen 9 9950X y el disco NVMe PCIe. Esto cubre de sobra las primeras horas de juego del grupo en el día 1.

### Fase 2: Expansión Nocturna Automática en `Schedules` (04:00 AM)
Para que los jugadores tengan un mapa aún más grande al día siguiente sin sufrir lag mientras juegan:
1. En Kinetic Panel, ve a **Management -> Schedules** y haz clic en **`Create Schedule`**.
2. Configúralo así:
   - **Name:** `Expansion Nocturna Chunky + Backup`
   - **Minute:** `0` | **Hour:** `4` | **Day of Month:** `*` | **Month:** `*` | **Day of Week:** `*` *(Se ejecuta a las 04:00 AM)*.
3. Añade un **New Task** dentro de ese Schedule:
   - **Action:** `Send Command`
   - **Payload:**
     ```text
     chunky world world
     ```
   - Y un segundo Task (con 5 segundos de delay):
     ```text
     chunky radius 3000
     ```
   - Y un tercer Task (con 5 segundos de delay):
     ```text
     chunky start
     ```
   *(Nota: Una vez que al día siguiente veas que llegó al 100%, puedes borrar o desactivar esa tarea de Chunky en Schedules y dejar únicamente la tarea diaria de Restart/Backup a las 04:30 AM).*

---

## ✅ PASO 5: Checklist Final y Mensaje de Entrega al Cliente

Antes de escribirle al cliente por **WhatsApp o Discord**, verifica estos 4 checks rápidos (toma 30 segundos):
- [ ] ¿El servidor encendió en verde (`Online`) sin errores rojos en consola?
- [ ] ¿El puerto de *Simple Voice Chat* (si aplica) coincide con el puerto secundario de `Network -> Ports`?
- [ ] ¿Terminó la **Fase 1 de Chunky** (`radius 1500` al 100%)?
- [ ] ¿Agregaste al usuario del cliente como Sub-user en Kinetic Panel (`Users -> New User`) con todos los permisos sobre su servidor?

### 💬 Plantilla de Mensaje de Entrega (Copiar y Pegar en WhatsApp / Discord)

> ¡Hola **[Nombre]**! ☁️🚀 Tu servidor en **Consterna Cloud** ya está **100% configurado, optimizado y listo para entrar a jugar**.
>
> 🎮 **Datos de Conexión al Juego:**
> • **IP del Servidor:** `[IP_Y_PUERTO]`
> • **Versión / Modpack:** `[Ej. Fabric 1.21.1 / Forge 1.20.1 / Modpack elegido]`
> • **Simple Voice Chat:** Ya está configurado y activo en el puerto `[PUERTO_VOICE]` *(solo necesitas tener el mod Simple Voice Chat en tu cliente y pulsar la tecla `V` dentro del juego)*.
>
> 🛠️ **Lo que dejamos optimizado para tu grupo:**
> • Argumentos de memoria **Aikar's Flags** activados para cero tirones de RAM.
> • Configuraciones anti-lag aplicadas y **mapa pre-generado con Chunky** alrededor del spawn para que puedan explorar fluido desde el primer minuto.
> • **Backups diarios automáticos** activados.
>
> 🖥️ **Acceso Total a tu Panel de Control:**
> • **Enlace del Panel:** `[URL_DEL_PANEL]`
> • **Tu Correo:** `[EMAIL_CLIENTE]` *(revisa tu bandeja de entrada para activar tu contraseña si es tu primera vez)*.
>
> Recuerda que nuestra infraestructura opera **24/7** y nuestro equipo está atento por **WhatsApp y Discord (Lun–Dom de 10:00 AM a 10:00 PM)** por si tienes cualquier duda al entrar. ¡Que disfruten muchísimo la aventura! 🔥
