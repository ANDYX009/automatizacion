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
