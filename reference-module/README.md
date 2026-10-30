# Módulo de referencia: tareas genéricas

Este ejemplo no pertenece al dominio Ecclesia. Muestra una ruta Express que valida entrada, un servicio que aplica una regla pura y un repositorio que usa SQL parametrizado. Adapta nombres, reglas, tablas y pruebas al proyecto destino. Nunca copies este módulo como una funcionalidad de Ecclesia.

Flujo: `routes.js` → `service.js` → `repository.js`. La prueba unitaria de `service.js` puede ejecutarse con Vitest tras instalar las dependencias del stack. La migración de ejemplo define la tabla mínima.
