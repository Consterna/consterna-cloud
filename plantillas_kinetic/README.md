# 📦 Kit de Plantillas Maestras — Kinetic Panel (Consterna Cloud)

Este directorio centraliza las **13 plantillas oficiales pre-optimizadas**, sus catálogos de **Mods y Plugins Recomendados** y el **Manual Operativo Maestro (SOP)** para entregas *"Llave en Mano"* (30 a 90 minutos) de **Consterna Cloud**.

---

## 🗂️ Estructura Organizada del Directorio

Para separar claramente los paquetes listos para subir a producción de los archivos fuente editables, el directorio se divide en:

```text
plantillas_kinetic/
├── README.md                          # Este índice de navegación rápida
├── GUIA_RAPIDA_KINETIC_SOP.md         # Manual Operativo Maestro (SOP) paso a paso
├── paquetes_zip/                      # 📦 Archivos .zip listos para subir y dar "Unarchive" en Kinetic Panel
│   ├── minecraft/                     # 7 paquetes .zip de Minecraft (Paper, Purpur, Fabric, Forge/NeoForge, Velocity)
│   │   ├── Plantilla-Configs-Paper-1.21.zip
│   │   ├── Plantilla-Configs-Paper-1.20.1.zip
│   │   ├── Plantilla-Configs-Paper-Legacy-1.16.5-1.18.2.zip
│   │   ├── Plantilla-Configs-Purpur.zip
│   │   ├── Plantilla-Configs-Fabric-1.21.zip
│   │   ├── Plantilla-Configs-Forge-NeoForge.zip
│   │   └── Plantilla-Velocity-Proxy.zip
│   └── otros_juegos/                  # 6 paquetes .zip del resto de juegos principales del catálogo
│       ├── Plantilla-Zomboid-Coop-LATAM.zip
│       ├── Plantilla-Palworld-Optimizado.zip
│       ├── Plantilla-Rust-Optimizado.zip
│       ├── Plantilla-Valheim-Optimizado.zip
│       ├── Plantilla-Terraria-Optimizado.zip
│       └── Plantilla-CoreKeeper-Optimizado.zip
├── codigo_fuente/                     # 🛠️ Carpetas fuente desempaquetadas para edición, lectura y auditoría
│   ├── minecraft/                     # 7 carpetas fuente de Minecraft
│   │   ├── paper-1.21-optimizado/
│   │   ├── paper-1.20.1-optimizado/
│   │   ├── paper-legacy-1.16.5-1.18.2/
│   │   ├── purpur-optimizado/
│   │   ├── fabric-optimizado/
│   │   ├── forge-neoforge-optimizado/
│   │   └── velocity-proxy-optimizado/
│   └── otros_juegos/                  # 6 carpetas fuente del resto de juegos principales
│       ├── zomboid-coop-latam/
│       ├── palworld-optimizado/
│       ├── rust-optimizado/
│       ├── valheim-optimizado/
│       ├── terraria-optimizado/
│       └── core-keeper-optimizado/
└── scripts/
    └── empaquetar_plantillas.py       # 🔄 Script automatizado para regenerar y auditar los 13 .zip desde codigo_fuente/
```

---

## ⚡ Guía Rápida de Uso

1. **Para desplegar un servidor a un cliente en Kinetic Panel:**
   - Entra directamente a [`paquetes_zip/minecraft/`](./paquetes_zip/minecraft/) o [`paquetes_zip/otros_juegos/`](./paquetes_zip/otros_juegos/).
   - Sube el archivo `.zip` correspondiente al **File Manager** del servidor en Kinetic Panel (`/home/container` o `/.cache/Server/` en Project Zomboid), haz clic en **`...` -> `Unarchive`** y elimina el `.zip`.
   - Sigue los pasos detallados en [`GUIA_RAPIDA_KINETIC_SOP.md`](./GUIA_RAPIDA_KINETIC_SOP.md).

2. **Para editar configuraciones o consultar las guías de Mods/Plugins recomendados:**
   - Abre la carpeta correspondiente dentro de [`codigo_fuente/minecraft/`](./codigo_fuente/minecraft/) o [`codigo_fuente/otros_juegos/`](./codigo_fuente/otros_juegos/).
   - Si modificas algún archivo de configuración o guía en `codigo_fuente/`, ejecuta el empaquetador oficial para actualizar y verificar automáticamente los 13 paquetes `.zip`:
     ```powershell
     python plantillas_kinetic/scripts/empaquetar_plantillas.py
     ```
