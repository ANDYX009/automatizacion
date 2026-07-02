# AGENTS.md - CONTRATO TÉCNICO Y REGLAS DE DESARROLLO

## [CONTEXTO DEL ESTUDIANTE]
- **Usuario GitHub:** ANDYX009 (acamarenac1700@alumno.ipn.mx)
- **Meta Profesional:** Ingeniero de Datos (Optimizado por Agentes de IA)
- **Meta de Empleo:** Antes de finalizar el año 2026
- **Nivel Actual:** Principiante (Explicaciones rigurosas, asertivas y corrección directa)

## [ENTORNO Y ARQUITECTURA (AI-FIRST IDE)]
- **Arquitectura:** Windows 11 + WSL (Ubuntu) nativo en terminal Warp
- **Editor:** VS Code conectado mediante la extensión remota WSL
- **Herramienta IA:** OpenCode versión 1.17.11 global en WSL
- **Proveedor Inferencia:** `opencode/deepseek-v4-flash-free` por defecto
- **Ruta Raíz del Proyecto:** `~/proyectos/automatizacion`

## [METODOLOGÍA Y REGLAS DE DESARROLLO]
- **Diseño Anclado (SDD):** Todo desarrollo debe regirse estrictamente por su archivo de especificación (ej. `HEARTBEAT.md`). Prohibido improvisar código fuera de la especificación.
- **Estilo:** Adherencia estricta a PEP 8 (indentación de 4 espacios, snake_case).
- **Tipado:** Tipado estático obligatorio (*type hinting*) en todas las funciones.
- **Restricción de Stack:** Uso exclusivo de la Biblioteca Estándar (*stdlib*). Prohibido `pip`.
- **Concurrencia:** Uso preferente de `asyncio` y operaciones no bloqueantes.

## [MANUAL DE ENTORNOS Y COMANDOS VERIFICADOS]
- **Conexión WSL:** Comando `wsl` desde PowerShell para migrar a Linux.
- **Navegación:** `cd ~/proyectos/automatizacion`
- **Seguridad SSH:** Llave ED25519 con passphrase (`ssh-add`).
- **Limpieza de Pantalla:** Comando `clear`
- **Ejecución:** `python3 heartbeat.py`
- **Comandos OpenCode TUI:** Acceso con `opencode` (Ayuda con `/`, modelos con `/models`, salir con `/exit`).

## [REGLAS ATÓMICAS DE TUTORÍA IA]
- **Regla de Turno Único:** Prohibido proporcionar código y solicitar su ejecución o prueba en el mismo turno. Cada interacción debe limitarse a una sola acción humana a la vez (o el estudiante edita, o el estudiante ejecuta). Esperar confirmación explícita del estudiante antes de avanzar.
- **Rigor Técnico:** Prohibido asumir conceptos por sentado o usar lenguaje ambiguo. Toda respuesta debe ser directa, concisa y orientada a la ingeniería de datos.
