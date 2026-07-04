# /audit - COMANDO DE AUDITORÍA DE INGENIERÍA DE DATOS

## [PROPÓSITO]
Analizar el estado de adherencia a PEP 8, cobertura de tipos (Type Hinting) y manejo asíncrono del código para asegurar que no existan bloqueos en el hilo principal.

## [REGLAS DE EJECUCIÓN]
1. Revisa todos los archivos `.py` del directorio actual.
2. Identifica si alguna función carece de anotaciones de tipo estático.
3. Verifica que las operaciones de Entrada/Salida (I/O) en disco usen hilos secundarios o corrutinas.
4. Genera un reporte resumido en formato Markdown indicando: [ESTADO], [DETALLES] y [ACCIÓN REQUERIDA].
