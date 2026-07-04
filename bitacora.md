# bitacora.md - HISTORIAL DE AVANCE Y LOGROS DEL PROYECTO

## [LOGROS Y CONFIGURACIONES INICIALES]
- **Seguridad SSH:** Autenticación local mediante llave ED25519 con frase de contraseña (*passphrase*) activa. El agente de seguridad `ssh-agent` fue inicializado y la llave privada fue registrada de forma exitosa (`ssh-add`).
- **Sincronización Nube:** Repositorio remoto `automatizacion` creado desde cero en GitHub Web. Enlace local por SSH configurado correctamente. Primer `git push` completado con éxito hacia la rama remota `main`.
- **Herramienta IA:** Instalación global de OpenCode versión 1.17.11 en WSL. Autenticación completada con OpenCode Zen y OpenCode Gateway.

## [HISTORIAL DE CLASES COMPLETADAS]

### Clase 2: Entorno e Interfaz
- Corregimos el entorno de la terminal asegurando la conexión nativa a Linux (WSL/Ubuntu) en lugar de PowerShell.
- Testeamos el entorno interactivo completo de OpenCode (TUI), localizando visualmente la existencia de `/models` para el cambio de IA.
- Desmentimos el comando teórico `/variance` tras verificar en la documentación que no existía en el motor local.

### Clase 3: Integridad Criptográfica
- Implementamos un control de integridad criptográfico (SHA-256) binario y optimizado en bloques (*chunks*) de 4096 bytes en `heartbeat.py`.
- Realizamos un ejercicio de estrés simulando una alteración en `HEARTBEAT.md`, validando el bloqueo autónomo del pipeline.
- Solucionamos un falso positivo de seguridad mediante la herramienta `Undo` para eliminar caracteres invisibles.
- Consolidamos el historial del proyecto con un control de versiones impecable en GitHub usando `.gitignore`.

### Clase 4: Concurrencia y Logs Paralelos
- Migramos el Watchdog síncrono a una arquitectura asíncrona nativa utilizando corrutinas (`async`/`await`) con el módulo `asyncio`.
- Implementamos persistencia no bloqueante en disco usando `asyncio.to_thread` para registrar latidos en `logs/heartbeat.log` cada 60 segundos.
- Diseñamos un flujo paralelo de alertas críticas que se consolida de forma autónoma en `logs/alerts.log` al detectar fallos de integridad.
- Sincronizamos con éxito el código estable hacia la rama remota `main` de GitHub mediante autenticación segura por SSH.

## [PUNTO EXACTO PARA RETOMAR LA PRÓXIMA SESIÓN]
- El entorno local y remoto se encuentran completamente alineados y respaldados en GitHub (`working tree clean`).
- El archivo `heartbeat.py` se mantiene en su versión estable asíncrona con el loop de eventos protegido de tracebacks.
- Los logs de alertas y latidos están estructurados y validados bit por bit en el disco local de Ubuntu.
- En la siguiente sesión se debe iniciar directamente con la **Clase 5 del manual**: Configuración de scripts de inicio automático en la terminal para automatizar tu Watchdog en el arranque del sistema.

### Clase 5: Automatización y Loop Engineering
- Estructuramos el flujo de trabajo bajo el marco del archivo `AGENTS.md` e inicializamos el entorno de OpenCode (`opencode.jsonc`).
- Diseñamos y guardamos la especificación técnica en `INICIO_AUTOMATICO.md` antes de modificar configuraciones del sistema (SDD).
- Automatizamos el arranque del Watchdog asíncrono en segundo plano inyectando un bloque condicional robusto en `~/.bashrc`.
- Validamos el aislamiento de flujos redirigiendo las salidas a `/dev/null` y auditamos con éxito el proceso mediante `ps aux`.

### Clase 6: Pruebas Unitarias Robustas y Mocking Asíncrono
- Diseñamos el plan de pruebas bajo la metodología SDD en el archivo `SPEC_TESTS.md`.
- Construimos un arnés de pruebas asíncronas heredando de `unittest.IsolatedAsyncioTestCase` para aislar el bucle de eventos en RAM.
- Implementamos inyección quirúrgica de estados simulando lecturas físicas por bloques mediante el control de `side_effect`.
- Auditamos y corregimos falsos negativos mediante la verificación del hash SHA-256 (`5d0c63...`) con la biblioteca estándar.
- Validamos con éxito el comportamiento del Watchdog ante escenarios de integridad exitosa y ataques simulados.
### Clase 7: Infraestructura MCP y Comandos Personalizados
- Configuramos con éxito el cliente de OpenCode conectando el protocolo MCP con el servidor remoto de Context7.
- Implementamos inyección dinámica de credenciales mediante variables de entorno para blindar tokens de seguridad en Git.
- Diseñamos y registramos el comando personalizado `/audit` en el directorio oculto `.opencode/commands/`.
- Automatizamos la re-auditoría estática del proyecto y corregimos desviaciones estéticas de PEP 8 en RAM desde la TUI de OpenCode.



