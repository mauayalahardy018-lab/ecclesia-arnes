# Prueba de portabilidad del arnés

Este protocolo produce evidencia; no representa una prueba ya realizada.

La instalación local ejecutada el 30 de octubre de 2026 está documentada en el repositorio hermano `ecclesia-portabilidad-prueba/docs/resultado.md`. Falta su publicación remota y el video.

## Repositorio de prueba

Crear un repositorio nuevo y vacío, con un dominio distinto de Ecclesia. Registrar URL, fecha, hash del commit inicial y versión de Node. El repositorio de prueba debe ser independiente del producto.

## Instalación

1. Copiar `core/AGENTS.base.md` a `AGENTS.md`.
2. Copiar `plantilla-proyecto/PROYECTO.md` a `docs/PROYECTO.md` y reemplazar todas las reglas de Ecclesia por el nuevo dominio.
3. Adaptar `ARCHITECTURE.md`, ADR y scripts de `stacks/express/package-scripts.md`.
4. Pedir a Codex un módulo mínimo con el prompt `core/prompts/01-nuevo-modulo.md`.
5. Ejecutar lint, formato, dependencias y prueba; registrar salida y correcciones en el CHANGELOG del repositorio de prueba.

## Criterios de éxito

- El módulo nuevo sigue ruta→servicio→repositorio y tiene una prueba de una regla de negocio propia.
- El nuevo repositorio no importa archivos de `ecclesia-proyecto` ni menciona iglesia, misa, diezmo o patrimonio en el código.
- Los controles pasan y el alumno puede explicar qué cambió del arnés base.

## Video de máximo cinco minutos

0:00–0:45, mostrar repositorios separados. 0:45–1:45, instalar archivos del arnés. 1:45–3:15, generar o adaptar el módulo. 3:15–4:15, ejecutar controles. 4:15–5:00, explicar una corrección y el resultado. Guardar ruta, duración y enlace solo después de grabarlo.
