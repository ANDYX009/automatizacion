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

async def registrar_alerta(mensaje: str) -> None:
    """Escribe alertas de seguridad de forma asíncrona en el log paralelo."""
    os.makedirs(LOG_DIR, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto_alerta = f"[{ahora}] CRITICAL_ALERT: {mensaje}\n"
    
    # asyncio.to_thread ejecuta la escritura de archivos en un hilo separado
    # para evitar bloquear el bucle de eventos asíncronos de la biblioteca estándar.
    await asyncio.to_thread(
        lambda: open(ALERT_FILE, "a", encoding="utf-8").write(texto_alerta)
    )
    print(f"[{ahora}] ⚠️ Alerta crítica persistida en {ALERT_FILE}")

async def registrar_latido_async() -> None:
    """Valida integridad y registra el latido rutinario de forma asíncrona."""
    # Nota técnica: verificar_integridad sigue siendo síncrona por eficiencia en ráfaga
    if not verificar_integridad():
        msg_error = "Violación de integridad en HEARTBEAT.md detectada de forma autónoma."
        # Disparamos la alerta asíncrona en paralelo antes de colapsar
        await registrar_alerta(msg_error)
        raise SystemExit(f"Fallo de seguridad: {msg_error}")
        
    os.makedirs(LOG_DIR, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto_log = f"[{ahora}] HEARTBEAT: Integridad verificada. Sistema seguro.\n"
    
    await asyncio.to_thread(
        lambda: open(LOG_FILE, "a", encoding="utf-8").write(texto_log)
    )
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
