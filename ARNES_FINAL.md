# Arnés de desarrollo de Ecclesia

Versión de entrega del 1 de noviembre de 2026. Este documento describe el conjunto de instrucciones y controles usado para construir el Sistema Nacional de Gestión de Iglesias. El arnés vive en un repositorio distinto del producto y se probó en un proyecto de tareas sin código de Ecclesia.

## 1  Alcance y fuente de decisiones

El documento del caso **Proyecto Ecclesia Sistema Nacional de Gestión de Iglesias** define el alcance nacional. Se extrajeron 27 requisitos funcionales obligatorios, cuatro deseables, ocho no funcionales y reglas de negocio. `ecclesia-proyecto/docs/requerimientos.md` conserva origen, aceptación y diez preguntas P-01 a P-10. Las preguntas aún no respondidas no se atribuyen al docente ni se presentan como requisitos validados.

El prototipo anterior de una sola iglesia sirvió de referencia visual. El producto nacional se implementó por separado con Express, PostgreSQL y módulos de dominio. La demostración publicada en Sites sirve para recorrer la interfaz y guardar cambios en un navegador; su panel de roles no es autenticación real y no reemplaza la API probada con PostgreSQL.

## 2  Instrucciones seguidas para cada tarea

1. Leer `AGENTS.md` del producto, `docs/PROYECTO.md`, requisitos, trazabilidad y arquitectura.
2. Asociar el cambio con RF, regla de negocio, criterio de aceptación y pregunta abierta cuando aplique.
3. Preparar un plan de archivos, validación de entrada, permisos, migración, datos semilla y pruebas antes de modificar código.
4. Implementar la ruta HTTP, el servicio y el repositorio; colocar cálculos y transiciones puras en `domain/`.
5. Cubrir caso exitoso, límite, error y acceso de otra iglesia. Actualizar OpenAPI, trazabilidad y bitácora con resultados observados.
6. Ejecutar `npm run check`; si cambió dominio o servicios, ejecutar `npm run coverage:full` sobre base sembrada. Repetir integración en PostgreSQL de servidor cuando importa la concurrencia.
7. Revisar diff, checklist de código y definición de terminado. Crear commits pequeños con autor de la cuenta y tráiler `Asistido-por: Codex`.

El hook `hooks/pre-commit` ejecuta `npm run check` antes de un commit. El CI repite controles de calidad, migración, semilla, integración y cobertura. Una prueba que falla se registra y corrige; no se cambia el resultado escrito para hacerla parecer aprobada.

## 3  Estructura del arnés y del producto

| Elemento | Función |
|---|---|
| `core/AGENTS.base.md` | Reglas que se instalan como `AGENTS.md` en el producto |
| `plantilla-proyecto/PROYECTO.md` | Contexto variable de un proyecto nuevo |
| `ARCHITECTURE.md` | Capas, dependencias e invariantes |
| `core/adr/001` a `005` | Stack, arquitectura, datos, autenticación e índice patrimonial |
| `core/prompts/` | Instrucciones reutilizables para módulo, endpoint, migración, pruebas y revisión |
| `core/checklists/` | Revisión de código y definición de terminado |
| `reference-module/tasks/` | Ejemplo independiente con ruta, servicio, repositorio, migración y prueba |
| `stacks/express/` y `hooks/` | Scripts y puerta de calidad |
| `CHANGELOG.md` y `PORTABILIDAD.md` | Cambios del arnés y procedimiento de instalación externa |

El producto se organiza en `src/app.js`, `src/modules/<modulo>/routes.js`, `service.js` y `repository.js`, `src/domain/`, `src/infrastructure/db/` y `auth/`, `migrations/`, `scripts/`, `tests/` y `public/`. La carpeta `docs/` contiene requisitos, trazabilidad, modelo, ADR, defensa y bitácora.

## 4  Arquitectura y cómo se usa

El flujo de una operación es **HTTP → ruta → servicio → repositorio → PostgreSQL**. La ruta analiza la petición, valida formato y aplica middleware de identidad. El servicio decide reglas y permisos de negocio, invocando funciones puras de `domain/`. El repositorio ejecuta SQL parametrizado dentro de transacciones cuando corresponde. La respuesta vuelve por la ruta con códigos HTTP documentados.

`domain/` no importa HTTP ni SQL. El repositorio no importa rutas. Las rutas no contienen consultas SQL ni cálculos del índice, dinero o transiciones. `dependency-cruiser` revisa esas direcciones. El módulo `iglesias` muestra la composición real y `reference-module/tasks` permite aplicar el patrón a un dominio distinto.

Los datos se crean mediante migraciones versionadas y una semilla reproducible. La identidad del usuario se obtiene de JWT; el rol y `user_churches` se comprueban en el servidor por operación. La interfaz puede ocultar botones, pero el permiso real lo establece la API. Un `church_id` delimita las lecturas y escrituras locales.

## 5  Reglas permanentes

**Siempre:** validar datos y permisos en servidor; usar consultas parametrizadas; guardar dinero en centavos enteros; distinguir horario recurrente de celebración real; conservar auditorías; señalar qué datos de iglesias reales son ficticios; comprobar pruebas y cobertura; registrar errores reales y decisiones revisables.

**Nunca:** inventar respuestas del cliente, pruebas o defensa; exponer cotizaciones, claves, contactos privados o diezmos en rutas públicas; permitir acceso entre iglesias sin autorización; borrar silenciosamente historial; contar objetos no vigentes en el índice; presentar el Site estático como una base compartida o como autenticación segura.

## 6  Invariantes de negocio y seguridad

- Iglesia cerrada: no aparece en directorio, ficha ni ranking público, pero conserva historial y puede reactivarse.
- Patrimonio: los estados perdido, prestado y baja no puntúan; los criterios del índice son versionados y el ejemplo del caso de 35.5 tiene prueba.
- Agenda: el mismo sacerdote no puede tener dos horarios incompatibles. El bloqueo transaccional se comprobó con solicitudes concurrentes en PostgreSQL 17.
- Celebración: registra fecha y oficiante real. El diezmo se asocia a la celebración, con un registro único y correcciones auditadas.
- Solicitud: puede crearse sin cuenta, se consulta con folio y clave; se almacena hash de la clave, y la cotización privada vence a los 15 días.
- Procedencia: los 40 templos tienen fuente y enlace Maps. La capacidad sembrada se marca como demostración; objetos, personas, horarios, servicios e importes no describen actividad real.

## 7  Verificación realizada

`npm run check` pasó lint, formato, dependencias, OpenAPI y pruebas de dominio. PostgreSQL 17 de servidor recibió migraciones y semilla desde cero: 32 estados, 2478 municipios, 40 iglesias, 120 objetos, 15 sacerdotes y 12 solicitudes. Pasaron 15 pruebas de integración, incluidas concurrencia, reportes y matriz de permisos. La cobertura conjunta de dominio y servicios pasó 39 pruebas y registró 86.41 % de sentencias y 78.98 % de ramas, por encima del umbral global de 70 %.

RF-02, RF-03, RF-04, RF-16, RF-21 y RF-27 se cerraron técnicamente con prueba o datos verificables. La aceptación definitiva de reglas sujetas a P-01 a P-10 depende de respuestas del docente o cliente. La defensa oral y el video grabado personalmente por el alumno no se declaran realizados por este documento.

## 8  Portabilidad

El arnés se instaló en `ecclesia-portabilidad-prueba`: se adaptó `AGENTS.md`, se creó un módulo genérico de tareas y se copió `hooks/pre-commit` a `.githooks/`. `git hook run pre-commit` aprobó lint, formato, dependencias y una prueba. La ruta de importación de la prueba se corrigió y registró. El video explicativo de 1:36 muestra comandos y salida de esa ejecución local.

Para otro proyecto: copiar `core/AGENTS.base.md` como `AGENTS.md`, completar `docs/PROYECTO.md`, adaptar arquitectura y scripts, instalar el hook, crear un módulo siguiendo `reference-module/tasks/` y ejecutar todos los controles. Se deben sustituir las reglas propias de Ecclesia por reglas del nuevo dominio.

## 9  Repositorios de entrega

- Producto: https://github.com/mauayalahardy018-lab/ecclesia-proyecto
- Arnés: https://github.com/mauayalahardy018-lab/ecclesia-arnes
- Prueba independiente: https://github.com/mauayalahardy018-lab/ecclesia-portabilidad-prueba

El historial de Git, las pruebas y la bitácora permiten reconstruir las decisiones. La URL de Sites presenta una demostración de interfaz; estos repositorios contienen el código de la aplicación, las instrucciones y la evidencia de portabilidad.
