# Controles del stack Express

El proyecto debe exponer `lint`, `format:check`, `test`, `coverage`, `deps:check` y `check`. `check` ejecuta los anteriores antes de commit. `dependency-cruiser` prohíbe ciclos y dependencias desde dominio a HTTP, repositorios o infraestructura. El hook de pre-commit ejecuta `npm run check` y falla si algún control falla.

No copiar números de cobertura a la documentación sin ejecutar la medición. El mínimo del curso es 70 % para dominio y servicios, no solo cobertura global.
