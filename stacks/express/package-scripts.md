# Controles del stack Express

El proyecto debe exponer `lint`, `format:check`, `test`, `coverage`, `deps:check` y `check`. `check` ejecuta los anteriores antes de commit. `dependency-cruiser` prohíbe ciclos y dependencias desde dominio a HTTP, repositorios o infraestructura. El hook de pre-commit ejecuta `npm run check` y falla si algún control falla.

Instalar `hooks/pre-commit` en `.githooks/pre-commit` y configurar `git config core.hooksPath .githooks`. Comprobar con `git hook run pre-commit`. Si el proyecto tiene OpenAPI, `check` también ejecuta la validación del contrato.

Para un proyecto que usa PostgreSQL embebido mediante PGlite/socket, configurar `DB_POOL_MAX=1` durante desarrollo y ejecutar una regresión de consultas públicas paralelas. Las pruebas de bloqueo y concurrencia se repiten en PostgreSQL de servidor. La cobertura conjunta de dominio y servicios se ejecuta con `npm run coverage:full` después de migrar y sembrar la base.

No copiar números de cobertura a la documentación sin ejecutar la medición. El mínimo del curso es 70 % para dominio y servicios, no solo cobertura global.
