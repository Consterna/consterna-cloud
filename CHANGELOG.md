# Registro de Cambios (Changelog)

Todas las modificaciones importantes de este proyecto serán documentadas en este archivo.

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
