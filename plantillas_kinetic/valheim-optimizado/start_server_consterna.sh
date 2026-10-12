#!/bin/bash
# ==============================================================================
# CONSTERNACLOUD - SCRIPT DE REFERENCIA VALHEIM DEDICATED SERVER (Octubre 2026)
# Archivo: start_server_consterna.sh
# Nota: En Kinetic Panel, estos argumentos se configuran desde "Settings -> Startup",
#       o bien usando este script si se ejecuta en contenedor personalizado.
# ==============================================================================
export templdpath=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=./linux64:$LD_LIBRARY_PATH
export SteamAppId=892970

./valheim_server.x86_64 \
  -nographics \
  -batchmode \
  -name "Consterna Cloud | Valheim LATAM" \
  -port 2456 \
  -world "Dedicated" \
  -password "consterna" \
  -savedir "/home/container/saves" \
  -public 1 \
  -saveinterval 1200 \
  -backups 4 \
  -backupshort 7200 \
  -backuplong 43200

export LD_LIBRARY_PATH=$templdpath
