# Watchdog Autónomo de Integridad Asíncrono

## 📋 Descripción General
Este proyecto consiste en un agente de monitoreo autónomo (*Watchdog*) diseñado bajo un enfoque de desarrollo guiado por especificaciones (SDD). Su función principal es validar de manera continua la integridad de los archivos críticos del entorno mediante criptografía y registrar latidos rutinarios de salud del sistema, aislando las alertas de seguridad en flujos de datos paralelos.

## ⚡ Arquitectura de la Solución
El sistema opera de forma continua y asíncrona mediante un bucle de eventos nativo. Su arquitectura se compone de:
1. **Módulo de Integridad:** Un validador criptográfico basado en el algoritmo **SHA-256** que procesa archivos mediante bloques binarios (*chunks*) de 4096 bytes para mantener un consumo de memoria RAM plano y predecible (evitando el *Out of Memory Killer*).
2. **Orquestador Asíncrono (`asyncio`):** Un bucle continuo no bloqueante que administra los tiempos de espera mediante tareas cooperativas.
3. **Persistencia Aislada de Logs:** Utiliza hilos secundarios (`asyncio.to_thread`) para realizar operaciones de escritura en disco sin congelar el hilo principal del agente, dividiendo los datos en dos archivos paralelos:
   - `logs/heartbeat.log`: Registro de latidos rutinarios cada 60 segundos.
   - `logs/alerts.log`: Persistencia inmediata de alertas críticas al detectar fallos de integridad.
4. **Bloqueo Autónomo:** Si la huella criptográfica es alterada, el sistema suspende los latidos, persiste el error crítico y aborta la ejecución para proteger el pipeline de datos.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.14.4
- **Biblioteca:** Python Standard Library (`os`, `asyncio`, `hashlib`, `datetime`) — *Sin dependencias externas de terceros*.
- **Entorno de Desarrollo:** WSL 2 (Ubuntu) en terminal Warp, editado vía VS Code Remote.

## 🚀 Instrucciones de Ejecución
1. Asegurar el entorno nativo Linux en la consola:
   ```bash
   wsl
   ```
2. Navegar a la raíz del proyecto:
   ```bash
   cd ~/proyectos/automatizacion
   ```
3. Ejecutar el agente autónomo:
   ```bash
   python3 heartbeat.py
   ```
