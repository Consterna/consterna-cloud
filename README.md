# ☁️ Consterna Cloud - Game Server Hosting

![W3C Validated](https://img.shields.io/badge/W3C-Validated-brightgreen) ![Accessibility WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA-blue) ![SEO Optimized](https://img.shields.io/badge/SEO-Optimized-success)

Landing page y ecosistema de operaciones para **Consterna Cloud**, proveedor independiente de servidores de videojuegos de alto rendimiento listos para jugar ("Llave en Mano") y servicios adicionales a medida (Add-ons). Impulsado por hardware AMD Ryzen 9 9950X y almacenamiento NVMe PCIe mediante partners Tier-1, con alojamiento estratégico en EE.UU. (Miami) para lograr latencia ultra estable (~70-85ms) hacia Colombia y LATAM, más cobertura adicional en Norteamérica y Europa.

## 📂 Estructura Profesional del Proyecto

```text
consterna-cloud/
├── index.html                        # Landing page principal en producción (Cloudflare Pages)
├── banner_whatsapp.jpg               # Imagen Open Graph / Twitter Card en raíz para previsualizaciones
├── robots.txt                        # Directivas SEO de rastreo para motores de búsqueda
├── sitemap.xml                       # Mapa XML del sitio para indexación en Google y Bing
├── compose.yml                       # Orquestación Docker Compose (Traefik, PostgreSQL, Adminer, Backend, Frontend Nginx)
├── .env.example                      # Plantilla segura de variables de entorno
├── README.md                         # Documentación general del ecosistema
├── CHANGELOG.md                      # Historial detallado de versiones y auditorías
├── assets/
│   └── brand/
│       └── consterna-discord-icon.jpg # Activo oficial de marca / ícono para Discord y comunidad
├── backend/                          # API Backend en FastAPI + SQLModel + Alembic + Panel Web /admin
│   ├── app/                          # Núcleo de la aplicación (modelos, rutas REST, /admin UI, seguridad, Alembic)
│   ├── scripts/                      # Scripts de operación, calidad y migración idempotente (import_data.py, fix_emails.py)
│   ├── tests/                        # Suite de 58 pruebas automatizadas (Pytest con SQLite in-memory aislado)
│   ├── Dockerfile                    # Imagen de producción multi-stage con uv (incluye /app/scripts)
│   ├── alembic.ini                   # Configuración de migraciones de base de datos
│   ├── pyproject.toml                # Dependencias y configuración estricta de Ruff, Mypy y Pytest
│   └── README.md                     # Documentación técnica del Backend
└── plantillas_kinetic/               # Kit de 13 plantillas maestras para despliegues en Kinetic Panel
    ├── README.md                     # Índice rápido de navegación del kit de plantillas
    ├── GUIA_RAPIDA_KINETIC_SOP.md    # Manual Operativo Maestro (SOP) paso a paso
    ├── paquetes_zip/                 # 📦 Archivos .zip listos para subir ("Unarchive") en Kinetic Panel
    │   ├── minecraft/                # 7 paquetes .zip (Paper 1.21, Paper 1.20.1, Legacy, Purpur, Fabric, Forge/NeoForge, Velocity)
    │   └── otros_juegos/             # 6 paquetes .zip (Project Zomboid, Palworld, Rust, Valheim, Terraria, Core Keeper)
    ├── codigo_fuente/                # 🛠️ Carpetas fuente editables y catálogos de Mods/Plugins recomendados
    │   ├── minecraft/                # 7 carpetas fuente de Minecraft
    │   └── otros_juegos/             # 6 carpetas fuente de los demás juegos del catálogo
    └── scripts/
        └── empaquetar_plantillas.py  # Script automatizado para empaquetar y verificar los 13 archivos .zip
```

## 🚀 Componentes Principales

- `index.html`: Landing page principal (HTML5, Tailwind CSS, catálogo de 5 Planes por RAM + 3 Add-ons, **Recomendador de RAM + Cotizador "Arma tu Servidor" en Vivo (`#cotizador`)**, **Vitrina Técnica Interactiva de Optimización "Llave en Mano" por Juego (`#optimizacion`)**, Hub de Consultas/Tickets en Discord, animaciones custom y cotizador dinámico USD/COP).
- `plantillas_kinetic/`: Kit completo de **13 plantillas maestras pre-optimizadas** (Octubre 2026), organizadas limpiamente en **`paquetes_zip/`** (listas para subir con `Unarchive` en Kinetic Panel, separadas en `minecraft/` y `otros_juegos/`), **`codigo_fuente/`** (carpetas editables con sus guías `MODS_RECOMENDADOS_*.txt` / `PLUGINS_RECOMENDADOS_*.txt`), **`scripts/empaquetar_plantillas.py`** y el manual operativo **`GUIA_RAPIDA_KINETIC_SOP.md`**.
- `backend/`: API Backend implementado en FastAPI (Python) con panel web operativo **`/admin`** (KPIs financieros con reparto 50/50 Cristian & Víctor, semáforo de cobros, recordatorio WhatsApp 1-clic, generador de acta de entrega *"Llave en Mano"* y botón de sincronización con Excel CRM), endpoints operativos (`/api/v1/servers/expiring`, `/api/v1/servers/summary`, `/api/v1/servers/{id}/delivery-message`, `/api/v1/utils/sync-excel`), migración inicial real en Alembic, sincronización idempotente (`upsert`) en `backend/scripts/import_data.py` y **58 pruebas unitarias e integrales** en `backend/tests/` aisladas en SQLite in-memory.
- `banner_whatsapp.jpg`, `robots.txt` & `sitemap.xml`: Activos estáticos de raíz requeridos por **Cloudflare Pages** para SEO y previsualizaciones Open Graph en WhatsApp y Discord.
- `assets/brand/consterna-discord-icon.jpg`: Activo gráfico oficial de marca para el servidor de Discord y canales de comunidad.
- `Control_Clientes_Consterna_V7_ENTERPRISE.xlsx`: Archivo local automatizado y homologado con el catálogo oficial v1.9.0 para el seguimiento de renovaciones y pagos (excluido del repositorio público vía `.gitignore`).

## 🔧 Detalles Técnicos (`index.html`)

- **Framework CSS:** Tailwind CSS (vía CDN con sistema Anti-FOUC).
- **Fuente:** Plus Jakarta Sans (Google Fonts) cargada con `preconnect` y `preload`.
- **Modelo de Negocio (Entrega "Llave en Mano" en 30–90 min + Límites Sanos en Add-ons):**
  - **5 Planes Base por RAM (4 GB a 16 GB Dedicado):** Incluyen configuración inicial "Llave en Mano" lista para jugar (instalación del juego o modpack público elegido de CurseForge/Modrinth/Steam Workshop, puertos adicionales como *Simple Voice Chat*, optimización de memoria/flags y pre-generación con Chunky en Minecraft), entregada habitualmente entre **30 y 90 minutos** tras verificar el pago dentro del horario de atención (Lun–Dom 10:00 AM a 10:00 PM GMT-5), con acceso total al panel de control, mitigación DDoS, backups diarios automáticos e infraestructura/red activa 24/7.
  - **Recomendador de RAM + Cotizador "Arma tu Servidor" en Vivo (`#cotizador`):** Selector interactivo de juego (los 7 juegos del catálogo), slider de jugadores (`2` a `30+`), nivel de mods (*Vanilla / Ligero*, *Moderado / Workshop*, *Pesado (+100 mods)*) y checkboxes de los 3 Add-ons que calcula la RAM mínima sugerida y el desglose mensual + pago único en USD y COP dinámico (`aria-live="polite"`) con botón de orden directa a WhatsApp.
  - **Vitrina Técnica Interactiva de Optimización "Llave en Mano" (`#optimizacion`):** Pestañas interactivas para los 7 juegos mostrando las configuraciones reales del kit `plantillas_kinetic/` aplicadas en cada entrega versus un hosting genérico sin configurar.
  - **3 Servicios Adicionales (`#addons`):** Monetización modular con límites sanos para trabajo pesado a medida o continuo: *Creación de Modpacks / Eventos a Medida* ($5.00 USD, pago único para armar, diseñar, combinar y testear un modpack propio desde cero), *Sysadmin Dedicado Mensual* ($6.00 USD/mes, administrador técnico de cabecera todo el mes para agregar/quitar mods o plugins constantemente, configurar permisos complejos, reparar crashes por ediciones manuales, gestionar wipes y mantenimiento continuo) e *IP Dedicada Exclusiva* ($4.00 USD/mes, puerto por defecto ej. 25565), cada uno con precios transparentes y CTA directo a WhatsApp.
  - **Hub Oficial de Discord y Comunidad (`#comunidad`):** Integración de Discord (`https://discord.gg/PhsZEfc4KE`) junto a WhatsApp como canal oficial de consultas pre-venta, atención de soporte técnico mediante sistema de tickets privados y punto de encuentro de la comunidad.
- **Accesibilidad (WCAG 2.1 AA) y Compatibilidad:**
  - Implementación estricta de `aria-controls`, `aria-expanded`, `aria-labelledby`, `aria-hidden` y `aria-label` en todos los botones, regiones y enlaces de solo ícono, con contraste mínimo >= 4.5:1 (`text-zinc-400` / `text-indigo-400`).
  - Soporte para preferencias del usuario (`prefers-reduced-motion: reduce`).
  - Fallback progresivo para `IntersectionObserver` (más `<noscript>`) y scripts 100% en ES5 para navegadores legacy.
- **Rendimiento:**
  - Uso de `content-visibility: auto` para diferir el renderizado de secciones fuera de pantalla.
  - Aceleración por GPU para animaciones (`will-change: transform`).
  - Scroll horizontal estrictamente bloqueado para dispositivos móviles (`max-width: 100%; overflow-x: hidden`).
- **SEO y Conversiones:**
  - Inyección de JSON-LD Schema (`Product`, `AggregateRating` con `bestRating`/`worstRating`, y `AggregateOffer` para los 5 planes).
  - Insignias de confianza (Trust Badges: *Entregado 100% Configurado*, *Protección DDoS*, *Infraestructura y Red 24/7*) integradas bajo el Hero CTA.
  - Uso de SVG Sprites optimizados con retrocompatibilidad (`xlink:href`).
  - **Automatización de Precios (USD/COP):** Script cambiario en tiempo real conectado a API de divisas con caché local de 24 horas y precios piso de respaldo (`Math.max` sobre base 4.000 COP/USD) tanto en planes de RAM como en Add-ons, actualizando dinámicamente los enlaces de WhatsApp.

## 📞 Canales Oficiales de Contacto (WhatsApp y Discord)
- **WhatsApp Directo (`https://wa.me/573214118506`):** Todos los botones de planes, add-ons, barra de navegación y soporte cuentan con mensajes pre-llenados (`?text=...`) codificados en URI y alineados con la acción de cada botón.
- **Discord Oficial (`https://discord.gg/PhsZEfc4KE`):** Canal de consultas pre-venta, cotizaciones de RAM/Modpacks, soporte técnico por tickets y comunidad, integrado en el Navbar, Hero, Banner de Asesoría, `#comunidad`, FAQ y Footer.

## ☁️ Despliegue (Deploy)
Diseñado para desplegarse en **Cloudflare Pages** conectado al repositorio o subiendo los activos estáticos (`index.html`, `robots.txt`, `sitemap.xml`, `banner_whatsapp.jpg`).

## 📋 Registro de Versiones
El historial detallado de actualizaciones y auditorías se encuentra en el archivo [CHANGELOG.md](./CHANGELOG.md).

