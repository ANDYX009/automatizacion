# ESPECIFICACIÓN: PRUEBAS UNITARIAS ASÍNCRONAS CON AISLAMIENTO

## 1. OBJETIVO
Validar de forma automatizada y aislada en memoria el comportamiento del Watchdog (`heartbeat.py`) ante escenarios de éxito y fallos de integridad criptográfica, utilizando exclusivamente la biblioteca estándar de Python.

## 2. ESCENARIOS DE PRUEBA
- **Test 1 (Caso de Éxito):** Simular que la lectura de `HEARTBEAT.md` devuelve los bytes exactos que generan la firma válida (`aa0dc9...`). El script debe registrar el latido rutinario normalmente.
- **Test 2 (Ataque/Corrupción):** Simular que la lectura de `HEARTBEAT.md` devuelve bytes corruptos o alterados. El sistema debe disparar la función asíncrona `registrar_alerta()` y terminar la ejecución con un error de sistema (`SystemExit`).

## 3. RESTRICCIONES DE ENTORNO
- **Aislamiento Absoluto:** Queda estrictamente prohibido leer o escribir en los archivos reales del disco duro (`HEARTBEAT.md`, `logs/`). Todo debe ocurrir mediante parches (`unittest.mock.patch`) en la memoria RAM.
- **Entorno Asíncrono:** Uso obligatorio de `unittest.IsolatedAsyncioTestCase` para gestionar de forma limpia el bucle de eventos de las corrutinas.
- **Tipado y Estilo:** Cumplimiento estricto de PEP 8 y anotaciones de tipo completas.

