import os
import time
import hashlib
from datetime import datetime

# Configuración de rutas según HEARTBEAT.md
LOG_DIR = os.path.expanduser("~/proyectos/automatizacion/logs")
LOG_FILE = os.path.join(LOG_DIR, "heartbeat.log")
CONFIG_FILE = os.path.expanduser("~/proyectos/automatizacion/HEARTBEAT.md")

# La firma matemática exacta que acabamos de validar en la terminal
FIRMA_ESPERADA = "aa0dc9d0e7012f77db6877ce6d9564a0c26c7869e3a31bb14e9683be7d8ec362"

def verificar_integridad() -> bool:
    """Calcula el hash SHA-256 de HEARTBEAT.md y lo compara con la firma esperada."""
    if not os.path.exists(CONFIG_FILE):
        print(f"[ALERTA ROJA] El archivo de configuración no existe en: {CONFIG_FILE}")
        return False
        
    sha256 = hashlib.sha256()
    with open(CONFIG_FILE, "rb") as f:
        # Lee en bloques binarios para optimizar memoria
        while chunk := f.read(4096):
            sha256.update(chunk)
            
    firma_actual = sha256.hexdigest()
    return firma_actual == FIRMA_ESPERADA

def registrar_latido() -> None:
    """Escribe una marca de tiempo en el log solo si pasa el control de integridad."""
    if not verificar_integridad():
        print("[SISTEMA CORRUPTO] El latido fue cancelado por violación de integridad.")
        raise SystemExit("Fallo de seguridad: Modificación no autorizada detectada.")
        
    os.makedirs(LOG_DIR, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ahora}] HEARTBEAT: Integridad verificada. Sistema seguro.\n")
    print(f"[{ahora}] Latido registrado con éxito (Integridad: OK).")

def iniciar_watchdog() -> None:
    """Ejecuta el bucle continuo de monitoreo cada 60 segundos."""
    print("Iniciando Watchdog con Control de Integridad... Ctrl+C para detener.")
    try:
        while True:
            registrar_latido()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nWatchdog detenido de forma segura por el usuario.")

if __name__ == "__main__":
    iniciar_watchdog()
