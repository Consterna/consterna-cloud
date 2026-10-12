# Registro de Cambios (Changelog)

Todas las modificaciones importantes de este proyecto serán documentadas en este archivo.

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
