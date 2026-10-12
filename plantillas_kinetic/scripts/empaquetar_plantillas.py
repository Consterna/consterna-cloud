"""Empaquetador y validador oficial de las 13 plantillas maestras de Kinetic Panel.

Genera todos los archivos `.zip` en `paquetes_zip/minecraft/` y `paquetes_zip/otros_juegos/`
a partir de `codigo_fuente/minecraft/` y `codigo_fuente/otros_juegos/`, garantizando:
1. Estructura directa en la raíz del `.zip` (sin carpetas contenedoras intermedias)
   para que el botón `Unarchive` en `/home/container` de Kinetic Panel extraiga los
   archivos directamente en las rutas del servidor.
2. Separadores de ruta POSIX (`/`) compatibles al 100% con contenedores Linux.
3. Preservación y validación estricta de saltos de línea LF en scripts `.sh`
   (ej. `start_server_consterna.sh`).
"""

import logging
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parents[1]
SRC_ROOT = BASE_DIR / "codigo_fuente"
ZIP_ROOT = BASE_DIR / "paquetes_zip"

TEMPLATES_MAP: dict[str, list[tuple[str, str]]] = {
    "minecraft": [
        ("paper-1.21-optimizado", "Plantilla-Configs-Paper-1.21.zip"),
        ("paper-1.20.1-optimizado", "Plantilla-Configs-Paper-1.20.1.zip"),
        (
            "paper-legacy-1.16.5-1.18.2",
            "Plantilla-Configs-Paper-Legacy-1.16.5-1.18.2.zip",
        ),
        ("purpur-optimizado", "Plantilla-Configs-Purpur.zip"),
        ("fabric-optimizado", "Plantilla-Configs-Fabric-1.21.zip"),
        ("forge-neoforge-optimizado", "Plantilla-Configs-Forge-NeoForge.zip"),
        ("velocity-proxy-optimizado", "Plantilla-Velocity-Proxy.zip"),
    ],
    "otros_juegos": [
        ("zomboid-coop-latam", "Plantilla-Zomboid-Coop-LATAM.zip"),
        ("palworld-optimizado", "Plantilla-Palworld-Optimizado.zip"),
        ("rust-optimizado", "Plantilla-Rust-Optimizado.zip"),
        ("valheim-optimizado", "Plantilla-Valheim-Optimizado.zip"),
        ("terraria-optimizado", "Plantilla-Terraria-Optimizado.zip"),
        ("core-keeper-optimizado", "Plantilla-CoreKeeper-Optimizado.zip"),
    ],
}


def build_and_verify_all() -> int:
    total_built = 0
    for category, items in TEMPLATES_MAP.items():
        out_dir = ZIP_ROOT / category
        out_dir.mkdir(parents=True, exist_ok=True)

        for folder_name, zip_name in items:
            src_dir = SRC_ROOT / category / folder_name
            if not src_dir.is_dir():
                raise FileNotFoundError(
                    f"No existe la carpeta fuente esperada: {src_dir}"
                )

            zip_path = out_dir / zip_name
            files_to_pack = sorted(p for p in src_dir.rglob("*") if p.is_file())
            if not files_to_pack:
                raise RuntimeError(f"La carpeta fuente está vacía: {src_dir}")

            for file_path in files_to_pack:
                if file_path.suffix == ".sh":
                    raw_bytes = file_path.read_bytes()
                    if b"\r\n" in raw_bytes:
                        file_path.write_bytes(raw_bytes.replace(b"\r\n", b"\n"))

            with zipfile.ZipFile(
                zip_path, mode="w", compression=zipfile.ZIP_DEFLATED
            ) as zf:
                for file_path in files_to_pack:
                    arcname = file_path.relative_to(src_dir).as_posix()
                    zf.write(file_path, arcname=arcname)

            # Verificación de integridad del archivo .zip generado
            with zipfile.ZipFile(zip_path, mode="r") as zf:
                corrupt = zf.testzip()
                if corrupt is not None:
                    raise RuntimeError(f"Archivo corrupto en {zip_name}: {corrupt}")
                names = zf.namelist()
                if any(
                    "\\" in name or name.startswith(folder_name + "/") for name in names
                ):
                    raise RuntimeError(f"Estructura inválida en {zip_name}: {names}")
                for name in names:
                    if name.endswith(".sh") and b"\r\n" in zf.read(name):
                        raise RuntimeError(
                            f"El script {name} en {zip_name} contiene saltos CRLF"
                        )

            total_built += 1
            logger.info(
                "[OK] %s/%s (%d archivos verificados)",
                category,
                zip_name,
                len(files_to_pack),
            )

    logger.info(
        "\nTotal empaquetado y verificado con éxito: %d/13 plantillas.",
        total_built,
    )
    return total_built


if __name__ == "__main__":
    build_and_verify_all()
