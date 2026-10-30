# Cambios del arnés

## 0.1.0 — 2026-10-30

- Separado el arnés nacional Ecclesia del arnés anterior de una sola iglesia.
- Añadidas reglas de trazabilidad, arquitectura, cinco ADR, cinco prompts y dos checklists.
- Documentadas las preguntas pendientes del cliente y la prohibición de fingir validaciones o entradas de bitácora.

Las nuevas reglas derivadas de errores reales de Codex se añadirán aquí con fecha, error observado y verificación que evita repetirlo.

## 0.1.1 — 2026-10-30

- Error real: la primera versión de `priestHasConflict` comparó dos identificadores ausentes como si fueran el mismo horario y dejó pasar un traslape. La prueba `rechaza misa traslapada del mismo sacerdote` falló. Se corrigió la condición y se añadió a la checklist la revisión de entidades aún sin ID.

## 0.1.2 — 2026-10-30

- Una prueba con PostgreSQL detectó que `bigint` llega desde `pg` como texto. La comparación estricta con un número permitió crear un horario traslapado. Se normalizaron los identificadores y se añadió un caso de regresión.
- Las lecturas públicas de módulos secundarios deben comprobar el estado activo de la iglesia. La prueba de cierre reveló que servicios y patrimonio podían seguir visibles por ruta directa; se incorporó esta revisión a la checklist.
- Para equipos sin Docker se documentó una base PostgreSQL embebida de desarrollo. Esta vía no reemplaza la prueba final con PostgreSQL de servidor.

## 0.1.3 — 2026-10-30

- Añadido `reference-module/tasks/` como ejemplo genérico con ruta, servicio, repositorio, migración y prueba. El arnés dejó de depender de copiar directamente el módulo Ecclesia.
- Instalado en `ecclesia-portabilidad-prueba`: lint, formato, dependencias y prueba pasaron. La prueba copiada necesitó adaptar su import al directorio `tests/`, corrección registrada en el proyecto de prueba.
- Añadido `AGENTS.md` propio para mantener el arnés; el archivo que se instala en productos sigue siendo `core/AGENTS.base.md`.
