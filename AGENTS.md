# AGENTS.md - PUNTO DE RESTAURACIÓN DE CONTEXTO Y TUTORÍA
## [CONTEXTO DEL ESTUDIANTE]
- **Usuario GitHub:** ANDYX009 (Correo: acamarenac1700@alumno.ipn.mx).
- **Meta Profesional:** Ser Ingeniero de Datos con habilidades en Ciencia y Análisis de Datos optimizados por Agentes de IA. Meta de empleo: Antes de finalizar el año 2026.
- **Nivel Actual:** Principiante. Requiere explicaciones claras, rigurosas, asertivas y corrección directa de errores sin dar conceptos por sentado.

## [ESTADO DEL ENTORNO DE TRABAJO]
- **Sistema Operativo:** WSL (Ubuntu) ejecutado de forma nativa desde la terminal Warp.
- **Editor Visual:** VS Code conectado mediante la extensión remota WSL.
- **Lenguaje:** Python 3.14.4 nativo en Linux (stdlib únicamente, sin entornos virtuales aún).
- **Ruta del Proyecto:** `~/proyectos/automatizacion`

## [LOGROS Y CONFIGURACIONES DE LA SESIÓN ACTUAL]
1. **Seguridad SSH:** Autenticación local mediante llave ED25519 con frase de contraseña (*passphrase*) activa. El agente de seguridad `ssh-agent` fue inicializado y la llave privada fue registrada de forma exitosa (`ssh-add`).
2. **Sincronización Nube:** Repositorio remoto `automatizacion` creado desde cero en GitHub Web. Enlace local por SSH configurado correctamente. Primer `git push` completado con éxito hacia la rama remota `main`.
3. **Herramienta IA:** Instalación global de OpenCode versión 1.17.11 en WSL. Autenticación completada con OpenCode Zen y OpenCode Gateway. Proveedor de inferencia configurado por defecto en el modelo gratuito `opencode/deepseek-v4-flash-free`.

## [PUNTO EXACTO PARA RETOMAR LA PRÓXIMA SESIÓN]
El entorno local y remoto se encuentran completamente alineados y respaldados en GitHub (`working tree clean`). En la siguiente sesión se debe iniciar directamente con el desglose de la **Clase 2 del manual**:
1. Modificación y personalización del arnés de desarrollo (`AGENTS.md`) en VS Code para fijar las reglas de Python 3.14.4.
2. Configuración y entendimiento del Watchdog Autónomo (`HEARTBEAT.md`).
3. Práctica en terminal con los comandos interactivos de OpenCode (`/variance` y `/models`).

## [INSTRUCCIONES PARA EL TUTOR IA EN LA PRÓXIMA SESIÓN]
- Asumir un rol de Programador Profesional, Ingeniero de Datos Experto y Mentor.
- Toda la información técnica proporcionada debe ser verificable y provenir de documentación de alta calidad, estudios o repositorios oficiales.
- Responder estrictamente a **un solo problema, consulta o instrucción a la vez** para asegurar la asimilación del estudiante.

## [REGLAS DE DESARROLLO - PYTHON 3.14.4]
- **Estilo:** Adherencia estricta a PEP 8 (identación de 4 espacios, nombres en snake_case).
- **Tipado:** Tipado estático obligatorio (*type hinting*) en todas las funciones y métodos.
- **Restricción:** Uso exclusivo de la Biblioteca Estándar (*stdlib*). Prohibido `pip` o entornos virtuales por el momento.
- **Concurrencia moderna:** Uso preferente de `asyncio` y el nuevo módulo `interpreters` (PEP 734) si se requiere aislamiento de hilos sin GIL.
## [RECAPITULACIÓN DE LA SESIÓN - CLASE 2 COMPLETADA]
- **Lo que hicimos:** 
  1. Corregimos el entorno de la terminal asegurando la conexión nativa a Linux (WSL/Ubuntu) en lugar de PowerShell.
  2. Testeamos el entorno interactivo completo de OpenCode (TUI), localizando visualmente la existencia de `/models` para el cambio de IA.
  3. Desmentimos el comando teórico `/variance` tras verificar en la documentación que no existía en el motor local.
  4. Programamos, testeamos y detuvimos con éxito el bucle continuo del Watchdog Autónomo (`heartbeat.py`) con intervalos exactos de 60 segundos.
- **Lo que falta (Próxima Sesión):**
  1. Iniciar la Clase 3 del manual de automatización.
  2. Implementar un validador de integridad para que el Watchdog detecte si los archivos de configuración son modificados externamente.
  3. Configurar el inicio automático del script al abrir la terminal.
- **Contexto requerido por la IA para continuar:**
  1. El archivo `heartbeat.py` se encuentra en su versión estable con manejo de interrupción limpia.
  2. El árbol de trabajo local contiene registros actualizados en `logs/heartbeat.log`.

## [MANUAL DE ENTORNOS Y COMANDOS VERIFICADOS]
### 1. Entorno de Ejecución Correcto
- **Sistema Operativo Base:** Windows 11.
- **Entorno de Desarrollo:** Subsistema de Windows para Linux (WSL / Ubuntu) ejecutado nativamente en Warp.
- **Regla de Conexión:** Si la terminal inicia en PowerShell de Windows, se debe ingresar obligatoriamente el comando `wsl` para migrar al entorno de datos Linux.

### 2. Comandos de Consola Validados
- **Limpieza de Pantalla:** Comando `clear` (Limpia el buffer actual de la shell de Linux).
- **Navegación:** `cd ~/proyectos/automatizacion` (Mueve el cursor a la raíz del proyecto).
- **Ejecución de Automatismos:** `python3 ~/proyectos/automatizacion/heartbeat.py` (Inicia el bucle continuo).

### 3. Comandos Internos OpenCode (TUI)
- **Acceso:** `opencode` (Abre la interfaz gráfica completa en la terminal).
- **Menú de Ayuda:** Presionar la tecla `/` despliega de forma nativa la lista oficial de comandos del sistema.
- **Verificación de Modelos:** Comando `/models` (Permite interactuar y mapear los proveedores disponibles en OpenCode Zen).
- **Salida Segura:** Comando `/exit` (Cierra la interfaz interactiva y devuelve el control a Ubuntu).


