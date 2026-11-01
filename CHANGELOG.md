# Cambios del arnés

## 0.1.5 — 2026-11-01

- Se documentó el cierre técnico de RF-02, RF-03, RF-04, RF-16, RF-21 y RF-27, con procedencia de capacidades, ficha ampliada, seis tipos, prueba concurrente en PostgreSQL 17, reportes y matriz de permisos.
- La prueba del hook 0.1.4 se repitió en el repositorio independiente de tareas y su salida quedó registrada. El video explicativo local de 1:36 acompaña la entrega; la grabación personal del alumno sigue siendo un requisito distinto.
- `ARNES_FINAL.md` integra las instrucciones seguidas, estructura, reglas, límites, arquitectura, uso, invariantes y evidencia real. Se prepararon tres repositorios públicos separados.

## 0.1.4 — 2026-11-01

- Error observado: la ficha y el ranking devolvían 500 cuando el cliente consultaba recursos en paralelo contra el socket PostgreSQL embebido. El protocolo ahora exige `DB_POOL_MAX=1` para esa base, una regresión de lecturas paralelas y repetición sobre PostgreSQL de servidor antes de dar por validada la concurrencia.
- Se añadieron reglas de procedencia para el directorio: identidad y ubicación de templos con fuente y enlace Maps; patrimonio, horarios, personas, capacidad, precios y finanzas simulados deben indicarse como tales. Una ubicación municipal no se presenta como dirección de calle verificada.
- La cobertura de dominio y servicios se comprueba con `npm run coverage:full` sobre una base sembrada. Se conserva el umbral de 70 %; si el socket embebido falla, se registra el fallo y se repite en una base estable sin atribuirlo al código.
- Se agregó `hooks/pre-commit` instalable y se documentó su verificación. La prueba de portabilidad anterior no demuestra que este nuevo hook se haya instalado en un repositorio remoto.
- Se corrigió la referencia al prompt de módulo en la guía de portabilidad.

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
