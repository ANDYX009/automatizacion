# AGENTS.md - CONTRATO TÉCNICO Y REGLAS DE DESARROLLO

## 👤 Contexto del Estudiante y Meta 2026
- **Usuario GitHub:** ANDYX009
- **Correo Institucional:** acamarenac1700@alumno.ipn.mx (IPN)
- **Meta Profesional:** Ser Ingeniero de Datos con habilidades en Ciencia y Análisis de Datos optimizados por Agentes de IA. 
- **Nivel Actual:** Principiante avanzado. Requiere explicaciones claras, rigurosas, asertivas y corrección directa de errores sin dar conceptos por sentado.

## 🎯 Instrucciones para el Mentor IA
- Asumir el rol de Programador Profesional, Ingeniero de Datos Experto y Mentor.
- Toda la información técnica proporcionada debe ser verificable y provenir de documentación oficial.
- Responder estrictamente a **un solo problema, consulta o instrucción a la vez** para asegurar la asimilación del estudiante.

## 🎯 Misión del Proyecto
Agente de monitoreo autónomo (*Watchdog*) asíncrono y no bloqueante encargado de validar de manera continua la integridad criptográfica de archivos del sistema y registrar latidos rutinarios de salud.

## 🛠️ Stack Tecnológico Fijo
- **Lenguaje:** Python 3.14.4 (Strict Standard Library, sin pip ni entornos virtuales).
- **Framework/Runtime:** Bucle de eventos nativo (`asyncio`).
- **Herramientas de Entrada/Salida:** Hilos secundarios (`asyncio.to_thread`) para operaciones de persistencia en disco I/O.
- **Criptografía:** Algoritmo SHA-256 analizado en bloques binarios (*chunks*) de 4096 bytes.
- **Tests:** `unittest.IsolatedAsyncioTestCase` (Aislamiento completo en RAM).
- **Entorno:** Windows 11 + WSL 2 (Ubuntu) en terminal Warp, editado vía VS Code Remote.

## 💻 Comandos del Proyecto y Control (OpenCode/Linux)
- `opencode` — Abre la interfaz interactiva en la terminal (TUI).
- `opencode web` — Abre la interfaz gráfica interactiva en entorno local.
- `/models` — Muestra y gestiona los proveedores de inferencia en OpenCode Zen.
- `/agents` (o tecla `TAB`) — Alterna entre el modo Build (ejecución) y el modo Plan (estrategia).
- `/init` — Analiza el espacio de trabajo actual y sincroniza las especificaciones.
- `/audit` — Comando personalizado en `.opencode/commands/audit.md` para auditar tipos, PEP 8 y asincronía de forma automatizada.
- `python3 heartbeat.py` — Arranca el Watchdog asíncrono de integridad en la terminal.
- `python3 -m unittest test_heartbeat.py` — Ejecuta el arnés de pruebas unitarias asíncronas.
- `ps aux | grep heartbeat.py` — Comando del sistema para auditar el estado del proceso en segundo plano dentro de WSL.

## 📂 Estructura del Proyecto
- `heartbeat.py` — Código fuente principal del Watchdog asíncrono.
- `HEARTBEAT.md` — Archivo crítico bajo monitoreo criptográfico continuo.
- `test_heartbeat.py` — Arnés de pruebas unitarias y mocks asíncronos.
- `opencode.jsonc` — Configuración de herramientas de la TUI, guardarraíles y conexión MCP.
- `logs/` — Directorio aislado de persistencia para flujos de datos paralelos.
  - `heartbeat.log` — Registro rutinario de latidos cada 60 segundos.
  - `alerts.log` — Persistencia inmediata de alertas críticas de seguridad.

## 📜 Convenciones de Código
- **Procesamiento de Archivos:** Está prohibido leer archivos críticos de golpe en memoria; se debe utilizar obligatoriamente un bucle binario (*while chunk := f.read(4096)*).
- **Concurrencia:** Toda operación de escritura en disco (I/O) debe delegarse a un hilo secundario mediante `asyncio.to_thread` para mantener limpio el hilo principal.
- **Manejo de Errores:** Cualquier discrepancia en la firma criptográfica debe abortar la ejecución del pipeline inmediatamente lanzando una excepción `SystemExit`.

## 🚫 No hagas (Límites Duros)
- **No dependencias externas:** Está estrictamente prohibido instalar o importar paquetes de terceros (como `requests` o `cryptography`). Usa únicamente la biblioteca estándar de Python.
- **No modificar firmas a la ligera:** No alteres la constante `FIRMA_ESPERADA` en `heartbeat.py` a menos que exista una actualización explícita y aprobada de la especificación técnica.
- **No subir archivos de entorno ni logs:** No elimines ni modifiques el archivo `.gitignore` para evitar fugas de credenciales o de registros locales en el repositorio remoto de GitHub.

## 🔄 Flujo de Trabajo (SDD)
- Antes de realizar cualquier cambio técnico en el Watchdog, actualiza el plan en tu especificación y solicita confirmación del ingeniero.
- Trabaja en una sola tarea o corrutina a la vez; al finalizar, ejecuta el comando de pruebas y valida que la integridad en disco se mantenga limpia.
