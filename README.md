# ☁️ Consterna Cloud - Game Server Hosting

![W3C Validated](https://img.shields.io/badge/W3C-Validated-brightgreen) ![Accessibility WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA-blue) ![SEO Optimized](https://img.shields.io/badge/SEO-Optimized-success)

Landing page y ecosistema de operaciones para **Consterna Cloud**, un servicio de hosting gestionado (Managed Service / Reseller) de servidores de videojuegos. Ofrecemos infraestructura de hardware de partners líderes con nodos globales (Norteamérica, Europa, Asia/Oceanía) y rutas optimizadas para LATAM (incluyendo Argentina y el Cono Sur), operado como un servicio boutique/concierge.


## 🚀 Archivos del Proyecto

- `index.html`: La landing page principal (HTML5, Tailwind CSS, animaciones custom).
- `backend/`: API Backend implementado en FastAPI (Python) con migraciones de base de datos vía Alembic, manejando validación estricta de UUID y codificación de emails.
- `banner_whatsapp.jpg`: Imagen OG (Open Graph) para las previsualizaciones de WhatsApp, Discord y Facebook.
- `robots.txt` & `sitemap.xml`: Archivos de configuración SEO para motores de búsqueda (Google, Bing).
- `Control_Clientes_Consterna_V7_ENTERPRISE.xlsx`: Archivo automatizado para el seguimiento de renovaciones y pagos (actualizado a V7 Enterprise).

## 🔧 Detalles Técnicos (index.html)

- **Framework CSS:** Tailwind CSS (vía CDN dinámico).
- **Fuente:** Plus Jakarta Sans (Google Fonts) cargada con `preconnect` y `preload`.
- **Accesibilidad (a11y) y Compatibilidad:**
  - Implementación estricta de `aria-controls`, `aria-expanded` y `aria-hidden`.
  - Soporte para preferencias del usuario (`prefers-reduced-motion: reduce`).
  - Soporte total para navegadores legacy (incluyendo Opera clásico) gracias a scripts anti-FOUC en ES5 estricto.
- **Rendimiento:**
  - Uso de `content-visibility: auto` para diferir el renderizado de secciones fuera de pantalla.
  - Aceleración por GPU para animaciones (`will-change: transform`).
  - Scroll horizontal estrictamente bloqueado para dispositivos móviles (`max-width: 100vw; overflow-x: hidden`).
- **SEO y Conversiones:**
  - Inyección de JSON-LD Schema (`AggregateRating`) para la generación de Rich Snippets en Google.
  - Insignias de confianza (Trust Badges) integradas estratégicamente para maximizar conversiones.
  - Uso de SVG Sprites optimizados con retrocompatibilidad para dispositivos móviles antiguos (`xlink:href`).

## 📞 Enlaces de Contacto Dinámicos
Los planes apuntan automáticamente a WhatsApp con parámetros pre-llenados (`?text=...`) codificados en URI para una mejor conversión de ventas.

## ☁️ Despliegue (Deploy)
Pensado para ser subido directamente a **Cloudflare Pages / Workers**. Solo arrastra los archivos HTML, TXT, XML y JPG al dashboard.

## Registro de Versiones
El historial de actualizaciones y parches de seguridad/rendimiento se encuentra en el archivo [CHANGELOG.md](./CHANGELOG.md).
