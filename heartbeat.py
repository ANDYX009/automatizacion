import os
import time
from datetime import datetime

# Configuración de rutas según HEARTBEAT.md
LOG_DIR = os.path.expanduser("~/proyectos/automatizacion/logs")
LOG_FILE = os.path.join(LOG_DIR, "heartbeat.log")

def registrar_latido() -> None:
    """Asegura la estructura de directorios y escribe una marca de tiempo en el log."""
    os.makedirs(LOG_DIR, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ahora}] HEARTBEAT: El sistema autónomo está operando correctamente.\n")
    print(f"[{ahora}] Latido registrado en: {LOG_FILE}")

def iniciar_watchdog() -> None:
    """Ejecuta el bucle continuo de monitoreo cada 60 segundos."""
    print("Iniciando Watchdog Autónomo... Presiona Ctrl+C para detenerlo.")
    try:
        while True:
            registrar_latido()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nWatchdog detenido de forma segura por el usuario.")

if __name__ == "__main__":
    iniciar_watchdog()
