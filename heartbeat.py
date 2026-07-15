import os
import asyncio
import hashlib
from datetime import datetime

# Configuración de rutas según Clase 4
LOG_DIR = os.path.expanduser("~/proyectos/automatizacion/logs")
LOG_FILE = os.path.join(LOG_DIR, "heartbeat.log")
ALERT_FILE = os.path.join(LOG_DIR, "alerts.log")  # <-- NUEVO LOG PARALELO
CONFIG_FILE = os.path.expanduser("~/proyectos/automatizacion/HEARTBEAT.md")

# Firma matemática validada
FIRMA_ESPERADA = "aa0dc9d0e7012f77db6877ce6d9564a0c26c7869e3a31bb14e9683be7d8ec362"


async def verificar_integridad() -> bool:
    if not await asyncio.to_thread(os.path.exists, CONFIG_FILE):
        print(f"[ALERTA ROJA] El archivo de configuración no existe en: {CONFIG_FILE}")
        return False

    def _calcular_firma() -> str:
        sha256 = hashlib.sha256()
        with open(CONFIG_FILE, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()

    firma_actual = await asyncio.to_thread(_calcular_firma)
    return firma_actual == FIRMA_ESPERADA

async def registrar_alerta(mensaje: str) -> None:
    await asyncio.to_thread(os.makedirs, LOG_DIR, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto_alerta = f"[{ahora}] CRITICAL_ALERT: {mensaje}\n"

    def _persistir_alerta() -> None:
        with open(ALERT_FILE, "a", encoding="utf-8") as f:
            f.write(texto_alerta)

    await asyncio.to_thread(_persistir_alerta)
    print(f"[{ahora}] ⚠️ Alerta crítica persistida en {ALERT_FILE}")

async def registrar_latido_async() -> None:
    if not await verificar_integridad():
        msg_error = "Violación de integridad en HEARTBEAT.md detectada de forma autónoma."
        await registrar_alerta(msg_error)
        raise SystemExit(f"Fallo de seguridad: {msg_error}")

    await asyncio.to_thread(os.makedirs, LOG_DIR, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto_log = f"[{ahora}] HEARTBEAT: Integridad verificada. Sistema seguro.\n"

    def _persistir_log() -> None:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(texto_log)

    await asyncio.to_thread(_persistir_log)
    print(f"[{ahora}] Latido registrado con éxito (Asíncrono: OK).")


async def iniciar_watchdog_async() -> None:
    """Ejecuta el bucle asíncrono continuo de monitoreo cada 60 segundos."""
    print("Iniciando Watchdog Asíncrono con Control de Integridad... Ctrl+C para detener.")
    try:
        while True:
            await registrar_latido_async()
            # REGLA DE ORO DE ASYNCIO: await asyncio.sleep() NO bloquea el hilo de ejecución,
            # permite que el bucle de eventos atienda otras tareas concurrentes mientras espera.
            await asyncio.sleep(60)
    except asyncio.CancelledError:
        print("\nTarea del Watchdog cancelada internamente.")

if __name__ == "__main__":
    try:
        # Inicializa de forma limpia el bucle de eventos principal de Python 3.14
        asyncio.run(iniciar_watchdog_async())
    except KeyboardInterrupt:
        print("\nWatchdog detenido de forma segura por el usuario en Warp.")
