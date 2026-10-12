# Registro de Cambios (Changelog)

Todas las modificaciones importantes de este proyecto serán documentadas en este archivo.

## [1.6.0] - 2026-10-12 - Business Model Alignment, Add-ons Monetization & QA Audit
### Cambios y Mejoras
- **Modelo Infraestructura + Add-ons:** Alineación integral de textos en Hero, Beneficios, Planes, FAQ y Footer diferenciando claramente la infraestructura/monitoreo 24/7 (con entrega siempre incluida del panel de control y juego base) de la atención humana directa por chat (Lunes a Domingo, 10:00 AM a 10:00 PM GMT-5) y los servicios adicionales.
- **Catálogo de Add-ons Completo (`#addons`):** Se añadieron precios en USD y COP dinámico (`$5.00 USD` Instalación de Modpacks Complejos, `$6.00 USD/mes` Soporte VIP Sysadmin Dedicado, `$4.00 USD/mes` IP Dedicada Exclusiva), interactividad hover y botones CTA directos a WhatsApp, además de enlazar la sección en el Navbar Desktop y Mobile en el orden exacto del DOM (`lg:` breakpoint con `whitespace-nowrap` para prevenir colisiones en resoluciones tablet `768px-1023px`).
- **Simetría en Planes por RAM (`#planes`):** Estandarización total de las 5 tarjetas (4 GB a 16 GB) con 4 viñetas estrictamente simétricas y progresivas (`N Cores Ryzen 9 9950X (5.7 GHz)`, `NVMe PCIe, Panel Total y Motor Optimizado`, `Backups diarios automáticos y Anti-DDoS`, `Red 24/7 y Soporte de Infraestructura`), ajuste del precio inicial estático del Tier 4 GB a `~$34.000 COP` y aclaración de capacidad de hardware recomendada.
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
