# 🛠️ Manual Operativo (SOP): Entrega "Llave en Mano" en Kinetic Panel
**Versión:** Octubre 2026 (Actualizado al 11 de octubre de 2026)  
**Uso Interno:** Guía paso a paso para **Cristian y Víctor** en **Consterna Cloud**  
**Objetivo:** Entregar cualquier servidor 100% configurado, optimizado y con mapa pre-generado dentro de nuestro SLA prometido (**30 a 90 minutos**), reduciendo el trabajo manual repetitivo a menos de **5 minutos de clics efectivos**.

---

## 📦 Resumen de las 3 Plantillas Maestras (`.zip`)

En esta carpeta (`plantillas_kinetic/`) tienes listas las 3 plantillas comprimidas para arrastrar directamente al **File Manager** de Kinetic Panel:

1. **`Plantilla-Configs-Paper-1.21.zip`** *(Para servidores Minecraft con Plugins / Survival Clásico)*
   - Contiene `bukkit.yml`, `spigot.yml`, `server.properties`, `config/paper-global.yml` y `config/paper-world-defaults.yml`.
   - **Optimizaciones clave:** `redstone-implementation: ALTERNATE_CURRENT` (hasta 70% menos uso de CPU en redstone sin romper mecanismos), `per-player-mob-spawns: true` (granjas justas sin saturar MSPT), `max-auto-save-chunks-per-tick: 8` (cero tirones al guardar mundo), `simulation-distance: 8` / `view-distance: 10`, `entity-activation-range` equilibrado para no romper granjas de hierro y **Anti-Xray Engine Mode 1** activado de fábrica.
2. **`Plantilla-Configs-Fabric-1.21.zip`** *(Para servidores Técnicos, Series con Voice Chat y Modpacks)*
   - Contiene `server.properties`, `config/lithium.properties`, `config/ferritecore.mixin.properties`, `config/voicechat/voicechat-server.properties` y `MODS_RECOMENDADOS.txt`.
   - **Optimizaciones clave:** Configuración lista para el stack oficial de rendimiento server-side (**Lithium + FerriteCore + ModernFix + Krypton + ServerCore + Spark + Chunky + Simple Voice Chat**), reduciendo el consumo de RAM hasta un 40% y optimizando paquetes UDP (`mtu_size=1024`) para conexiones de LATAM.
3. **`Plantilla-Zomboid-Coop-LATAM.zip`** *(Para servidores de Project Zomboid Cooperativos o con Mods)*
   - Contiene `servertest.ini` y `servertest_SandboxVars.lua`.
   - **Optimizaciones clave:** `PingLimit=350` y `KickFastPlayers=false` (evita expulsiones falsas cuando alguien conduce rápido con 80ms de ping desde LATAM), `PauseEmpty=true`, `SaveWorldEveryMinutes=15`, `BackupsCount=5`, limpieza automática de basura en el suelo cada 24h in-game (`HoursForWorldItemRemoval = 24.0`), eliminación de cadáveres a las 72h y reducción de manchas de sangre (`BloodLevel = 3`) para evitar saturar la RAM tras semanas de partida.

---

## ⚡ PASO 1: Cómo aplicar la plantilla en 2 segundos (`Unarchive`)

### A. Para Minecraft (Paper 1.21+ o Fabric 1.21+)
1. En **Kinetic Panel**, instala primero la versión base desde **Version Installer** (Paper 1.21.x o Fabric 1.21.x) o el Modpack desde **Modpack Installer**.
2. Inicia el servidor **una sola vez**, acepta el EULA cuando salga el aviso y **apágalo (`Stop`)** apenas termine de generar las carpetas base.
3. Ve a **Management -> File Manager** (asegúrate de estar en la raíz `/home/container`).
4. Arrastra el archivo **`Plantilla-Configs-Paper-1.21.zip`** (o **`Plantilla-Configs-Fabric-1.21.zip`**) directamente hacia la ventana del File Manager.
5. Haz clic en los **3 puntos (`...`)** a la derecha del archivo `.zip` recién subido y selecciona **`Unarchive`**.
   - ¡Listo! Kinetic Panel sobrescribirá automáticamente `server.properties`, `bukkit.yml`, `spigot.yml` y la subcarpeta `config/` en su ubicación exacta.
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

Una de las mayores ventajas de nuestra entrega **"Llave en Mano"** es entregar el chat de voz por proximidad funcionando a la primera:

1. Instala el mod o plugin **Simple Voice Chat** desde el **Mod Manager / Plugin Installer** de Kinetic Panel (o súbelo a `/mods` o `/plugins`).
2. En el menú lateral izquierdo de Kinetic Panel, ve a **Network -> Ports** (o **Split Ports / Allocations**).
3. Si ves el botón **Quick Setup**, selecciona **Simple Voice Chat**; o bien haz clic en **`Open Port` / `Create Allocation`** para generar un puerto adicional libre.
4. Copia el número del nuevo puerto secundario asignado (por ejemplo: `25618`). *Nota: NUNCA uses el puerto principal del servidor de Minecraft para Voice Chat.*
5. Ve a **File Manager** -> `/config/voicechat/voicechat-server.properties` (o `/plugins/voicechat/voicechat-server.properties` en Paper).
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
3. Selecciona **`Aikar's Flags`** (recomendado para todos los planes de **4 GB, 6 GB, 8 GB y 12 GB**).
4. *(Opcional para el Plan **Tier 16 GB Dedicado** con Java 21+ en modpacks masivos como All The Mods 9/10)*: Puedes usar **Aikar's Flags** o **Generational ZGC** (`-XX:+UseZGC -XX:+ZGenerational`), que elimina por completo las pausas de recolección de memoria en heaps superiores a 12 GB.

---

## 🌍 PASO 4: El "Truco de las 2 Fases" con Chunky (Entregar rápido y sin Lag)

Pre-generar un radio enorme de 4.000 bloques de golpe antes de entregar tardaría más de 1 hora, retrasando la entrega al cliente. Con el **Truco de las 2 Fases**, entregamos el servidor en **menos de 30 minutos** y el mapa completo se expande solo mientras todos duermen:

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
> • **Versión / Modpack:** `[Ej. Fabric 1.21.1 / Modpack elegido]`
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
