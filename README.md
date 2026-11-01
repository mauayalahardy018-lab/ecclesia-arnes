# Arnés de desarrollo con Codex para Ecclesia

Este repositorio contiene las reglas, ejemplos y verificaciones que guían a Codex en el proyecto Ecclesia. Es independiente del código del producto y puede instalarse en otro proyecto adaptando `plantilla-proyecto/PROYECTO.md`.

La explicación completa de instrucciones, estructura, límites, arquitectura, uso y evidencia de la entrega está en `ARNES_FINAL.md`.

## Instalación

1. Copiar `core/AGENTS.base.md` como `AGENTS.md` en la raíz del proyecto.
2. Copiar `plantilla-proyecto/PROYECTO.md` a `docs/PROYECTO.md` y completar dominio, actores y reglas con evidencia del cliente.
3. Copiar `stacks/express/package-scripts.md` al proyecto y configurar los comandos de lint, formato, pruebas y arquitectura.
4. Leer `ARCHITECTURE.md`, los ADR y `core/checklists/definicion-de-terminado.md` antes de la primera tarea.
5. Ejecutar `npm run check` y documentar fallos o adaptaciones en `CHANGELOG.md`.
6. Copiar `hooks/pre-commit` a `.githooks/pre-commit` del producto y ejecutar `git config core.hooksPath .githooks`. Verificarlo con `git hook run pre-commit` antes del primer commit.

El módulo de referencia portátil está en `reference-module/tasks/`, con ruta, servicio, repositorio, migración y prueba. El módulo real `ecclesia-proyecto/src/modules/iglesias/` muestra su uso dentro del producto.

## Flujo de trabajo

Cada cambio parte de un requisito trazado. Codex propone archivos, validaciones y pruebas; el alumno revisa el plan, el código y la salida de los controles. Los commits asistidos terminan con `Asistido-por: Codex`. La bitácora registra decisiones y errores reales; nunca se inventan entradas para alcanzar una cuota.

## Contenido

- `core/AGENTS.base.md`: reglas siempre/nunca y contexto de IA.
- `ARCHITECTURE.md`: capas, dependencias y estructura.
- `core/adr/`: cinco decisiones principales.
- `core/prompts/`: cinco instrucciones reutilizables.
- `core/checklists/`: definición de terminado y revisión.
- `stacks/express/`: instalación de controles de Express.
- `hooks/pre-commit`: puerta ejecutable de lint, formato, dependencias, contrato y pruebas mediante `npm run check`.
- `plantilla-proyecto/PROYECTO.md`: datos variables del proyecto.
- `CHANGELOG.md`: evolución del arnés.
