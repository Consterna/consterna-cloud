# ☁️ Consterna Cloud - Game Server Hosting

![W3C Validated](https://img.shields.io/badge/W3C-Validated-brightgreen) ![Accessibility WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA-blue) ![SEO Optimized](https://img.shields.io/badge/SEO-Optimized-success)

Landing page y ecosistema de operaciones para **Consterna Cloud**, proveedor independiente de servidores de videojuegos de alto rendimiento listos para jugar ("Llave en Mano") y servicios adicionales a medida (Add-ons). Impulsado por hardware AMD Ryzen 9 9950X y almacenamiento NVMe PCIe mediante partners Tier-1, con alojamiento estratégico en EE.UU. (Miami) para lograr latencia ultra estable (~70-85ms) hacia Colombia y LATAM, más cobertura adicional en Norteamérica y Europa.

## 🚀 Archivos del Proyecto

- `index.html`: Landing page principal (HTML5, Tailwind CSS, catálogo de 5 Planes por RAM + 3 Add-ons, animaciones custom y cotizador dinámico USD/COP).
- `backend/`: API Backend implementado en FastAPI (Python) con migraciones de base de datos vía Alembic, manejando validación estricta de UUID y codificación de emails.
- `banner_whatsapp.jpg`: Imagen OG (Open Graph) para las previsualizaciones de WhatsApp, Discord y redes sociales.
- `robots.txt` & `sitemap.xml`: Archivos de configuración SEO para motores de búsqueda (Google, Bing).
- `Control_Clientes_Consterna_V7_ENTERPRISE.xlsx`: Archivo local automatizado para el seguimiento de renovaciones y pagos (excluido del repositorio público vía `.gitignore`).

## 🔧 Detalles Técnicos (`index.html`)

- **Framework CSS:** Tailwind CSS (vía CDN con sistema Anti-FOUC).
- **Fuente:** Plus Jakarta Sans (Google Fonts) cargada con `preconnect` y `preload`.
- **Modelo de Negocio (Entrega "Llave en Mano" + Límites Sanos en Add-ons):**
  - **5 Planes Base por RAM (4 GB a 16 GB Dedicado):** Incluyen configuración inicial "Llave en Mano" lista para jugar (instalación del juego o modpack público elegido de CurseForge/Modrinth/Steam Workshop, puertos adicionales como *Simple Voice Chat*, optimización de memoria/flags y pre-generación con Chunky en Minecraft), acceso total al panel de control, mitigación DDoS, backups diarios automáticos, infraestructura/red activa 24/7 y soporte técnico (Lun–Dom 10:00 AM a 10:00 PM GMT-5).
  - **3 Servicios Adicionales (`#addons`):** Monetización modular con límites sanos para trabajo pesado a medida o continuo: *Creación de Modpacks / Eventos a Medida* ($5.00 USD, pago único para armar, diseñar, combinar y testear un modpack propio desde cero), *Sysadmin Dedicado Mensual* ($6.00 USD/mes, administrador técnico de cabecera todo el mes para agregar/quitar mods o plugins constantemente, configurar permisos complejos, reparar crashes por ediciones manuales, gestionar wipes y mantenimiento continuo) e *IP Dedicada Exclusiva* ($4.00 USD/mes, puerto por defecto ej. 25565), cada uno con precios transparentes y CTA directo a WhatsApp.
- **Accesibilidad (WCAG 2.1 AA) y Compatibilidad:**
  - Implementación estricta de `aria-controls`, `aria-expanded`, `aria-labelledby`, `aria-hidden` y `aria-label` en todos los botones, regiones y enlaces de solo ícono, con contraste mínimo >= 4.5:1 (`text-zinc-400`).
  - Soporte para preferencias del usuario (`prefers-reduced-motion: reduce`).
  - Fallback progresivo para `IntersectionObserver` (más `<noscript>`) y scripts 100% en ES5 para navegadores legacy.
- **Rendimiento:**
  - Uso de `content-visibility: auto` para diferir el renderizado de secciones fuera de pantalla.
  - Aceleración por GPU para animaciones (`will-change: transform`).
  - Scroll horizontal estrictamente bloqueado para dispositivos móviles (`max-width: 100%; overflow-x: hidden`).
- **SEO y Conversiones:**
  - Inyección de JSON-LD Schema (`Product`, `AggregateRating` con `bestRating`/`worstRating`, y `AggregateOffer` para los 5 planes).
  - Insignias de confianza (Trust Badges) integradas bajo el Hero CTA.
  - Uso de SVG Sprites optimizados con retrocompatibilidad (`xlink:href`).
  - **Automatización de Precios (USD/COP):** Script cambiario en tiempo real conectado a API de divisas con caché local de 24 horas y precios piso de respaldo (`Math.max` sobre base 4.000 COP/USD) tanto en planes de RAM como en Add-ons, actualizando dinámicamente los enlaces de WhatsApp.

## 📞 Enlaces de Contacto Dinámicos
Todos los botones de planes, add-ons, barra de navegación y soporte apuntan a WhatsApp (`https://wa.me/573214118506`) con mensajes pre-llenados (`?text=...`) codificados en URI y alineados con la acción de cada botón.

## ☁️ Despliegue (Deploy)
Diseñado para desplegarse en **Cloudflare Pages** conectado al repositorio o subiendo los activos estáticos (`index.html`, `robots.txt`, `sitemap.xml`, `banner_whatsapp.jpg`).

## 📋 Registro de Versiones
El historial detallado de actualizaciones y auditorías se encuentra en el archivo [CHANGELOG.md](./CHANGELOG.md).

