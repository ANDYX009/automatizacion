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
### Clase 8: Aseguramiento de Calidad (QA), Perfilado de RAM y Refactor Agéntico
- **Auditoría de Bloqueos (I/O síncrono):** Ejecutamos el comando personalizado `/audit` en OpenCode, detectando micro-congelamientos arquitectónicos en el hilo principal causados por llamadas síncronas a `verificar_integridad` y `os.makedirs`.
- **Refactor Asíncrono de Bajo Nivel:** Modificamos el Watchdog para encapsular por completo el bucle de lectura binaria de 4096 bytes y la creación de rutas dentro de hilos secundarios usando `asyncio.to_thread`.
- **Higiene de Escrituras:** Eliminamos las funciones anónimas `lambda` fugaces en la persistencia de logs, sustituyéndolas por funciones internas estructuradas con administradores de contexto (`with open`) para prevenir fugas de descriptores de archivos (*file descriptor leaks*).
- **Alineación del Arnés:** Actualizamos el arnés de pruebas unitarias (`test_heartbeat.py`) para adaptarlo a la nueva arquitectura asíncrona de hilos, validando el éxito total del laboratorio con un resultado de 2/2 tests aprobados en RAM.
- **Perfilado Científico de Memoria:** Diseñamos e inyectamos un script de estrés con el módulo nativo `tracemalloc`, midiendo un pico máximo de memoria RAM fijo de apenas **235.88 KB**. Esto demostró matemáticamente la eficiencia y el comportamiento plano del *chunking* de 4 KB ante el *Out of Memory Killer* de Linux.
- **Sincronización y Cierre:** Eliminamos los scripts temporales de prueba, consolidamos el historial estético del proyecto y subimos de forma segura todos los cambios estables a la rama remota `main` de GitHub mediante autenticación por SSH.

## [PUNTO EXACTO PARA RETOMAR LA PRÓXIMA SESIÓN]
- El entorno local en WSL y el repositorio remoto están 100% alineados y protegidos (`working tree clean`).
- El Watchdog autónomo asíncrono y su arnés de pruebas se encuentran en su versión más óptima, eficiente y libre de bloqueos I/O.
- El archivo `AGENTS.md` está blindado con el contexto del estudiante del IPN, la meta profesional hacia el 2026 y los guardarraíles técnicos de desarrollo de la biblioteca estándar de Python.
- En la siguiente sesión se debe iniciar directamente con el siguiente bloque del manual de automatización avanzada o la **Clase 9**.





