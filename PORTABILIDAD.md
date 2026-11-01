# Prueba de portabilidad del arnés

Este protocolo describe la prueba y su evidencia. La instalación y ejecución local ya se realizaron; la publicación remota sigue pendiente.

La instalación local ejecutada el 30 de octubre de 2026 y su actualización a la versión 0.1.4 del 1 de noviembre están documentadas en el repositorio hermano `ecclesia-portabilidad-prueba/docs/resultado.md`. La copia del hook pasó los controles. La publicación remota sigue pendiente.

El video explicativo `ecclesia-portabilidad-prueba/docs/Video_portabilidad_arnes_0.1.4.mp4` dura 1:36 y usa los comandos y la salida real guardada en `ecclesia-portabilidad-prueba/docs/evidencia-hook-2026-11-01.txt`. La grabación personal del alumno pedida para la evaluación se mantiene como evidencia separada.

## Repositorio de prueba

Crear un repositorio nuevo y vacío, con un dominio distinto de Ecclesia. Registrar URL, fecha, hash del commit inicial y versión de Node. El repositorio de prueba debe ser independiente del producto.

## Instalación

1. Copiar `core/AGENTS.base.md` a `AGENTS.md`.
2. Copiar `plantilla-proyecto/PROYECTO.md` a `docs/PROYECTO.md` y reemplazar todas las reglas de Ecclesia por el nuevo dominio.
3. Adaptar `ARCHITECTURE.md`, ADR y scripts de `stacks/express/package-scripts.md`.
4. Pedir a Codex un módulo mínimo con el prompt `core/prompts/nuevo-modulo.md`.
5. Ejecutar lint, formato, dependencias y prueba; registrar salida y correcciones en el CHANGELOG del repositorio de prueba.

## Criterios de éxito

- El módulo nuevo sigue ruta→servicio→repositorio y tiene una prueba de una regla de negocio propia.
- El nuevo repositorio no importa archivos de `ecclesia-proyecto` ni menciona iglesia, misa, diezmo o patrimonio en el código.
- Los controles pasan y el alumno puede explicar qué cambió del arnés base.

## Video de máximo cinco minutos

0:00–0:45, mostrar repositorios separados. 0:45–1:45, instalar archivos del arnés. 1:45–3:15, generar o adaptar el módulo. 3:15–4:15, ejecutar controles. 4:15–5:00, explicar una corrección y el resultado. Guardar ruta, duración y enlace solo después de grabarlo.
