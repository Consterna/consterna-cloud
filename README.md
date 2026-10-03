# ☁️ Consterna Cloud - Game Server Hosting

Landing page y ecosistema de operaciones para **Consterna Cloud**, un servicio de hosting de servidores de videojuegos enfocado en LATAM, operado como servicio boutique/concierge.

## 🚀 Archivos del Proyecto

- `index.html`: La landing page principal (HTML5, Tailwind CSS, animaciones custom).
- `banner_whatsapp.jpg`: Imagen OG (Open Graph) para las previsualizaciones de WhatsApp, Discord y Facebook.
- `robots.txt` & `sitemap.xml`: Archivos de configuración SEO para motores de búsqueda (Google, Bing).
- `Control_Clientes_Consterna_V1.xlsx`: Archivo "CRM" Excel automatizado para el seguimiento de renovaciones y pagos.

## 🔧 Detalles Técnicos (index.html)

- **Framework CSS:** Tailwind CSS (vía CDN dinámico).
- **Fuente:** Plus Jakarta Sans (Google Fonts) cargada con `preconnect` y `preload`.
- **Accesibilidad (a11y):**
  - Implementación estricta de `aria-controls`, `aria-expanded` y `aria-hidden`.
  - Soporte para preferencias del usuario (`prefers-reduced-motion: reduce`).
- **Rendimiento:**
  - Uso de `content-visibility: auto` para diferir el renderizado de secciones fuera de pantalla.
  - Aceleración por GPU para animaciones (`will-change: transform`).
  - Scroll horizontal estrictamente bloqueado para dispositivos móviles (`max-width: 100vw; overflow-x: hidden`).

## 📞 Enlaces de Contacto Dinámicos
Los planes apuntan automáticamente a WhatsApp con parámetros pre-llenados (`?text=...`) codificados en URI para una mejor conversión de ventas.

## ☁️ Despliegue (Deploy)
Pensado para ser subido directamente a **Cloudflare Pages / Workers**. Solo arrastra los archivos HTML, TXT, XML y JPG al dashboard.

## Registro de Versiones
El historial de actualizaciones y parches de seguridad/rendimiento se encuentra en el archivo [CHANGELOG.md](./CHANGELOG.md).
