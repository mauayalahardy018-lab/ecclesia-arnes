# Revisión de código

1. ¿Qué párrafo del caso justifica el cambio y qué pregunta sigue abierta?
2. ¿Hay una regla de negocio escondida en ruta, SQL o interfaz?
3. ¿La respuesta pública filtra datos personales y financieros?
4. ¿Puede un usuario local manipular el identificador de otra iglesia?
5. ¿Se conservan el valor anterior, actor y fecha cuando corresponde?
6. ¿Hay pruebas de bordes, duplicados, traslapes, zonas horarias y fallos de autorización?
7. ¿OpenAPI, seeds, trazabilidad y bitácora reflejan el comportamiento real?
8. Si se excluye una entidad por su ID al comparar, ¿qué ocurre cuando ambos registros aún no tienen ID?
9. ¿Los identificadores `bigint` que devuelve PostgreSQL llegan como texto y se comparan con números en el dominio?
10. ¿Cada ruta pública de un submódulo comprueba que la iglesia esté activa, incluso cuando se conoce su ID?
11. ¿La ficha y el ranking soportan cargas paralelas sin devolver 500 con el pool configurado para la base usada?
12. ¿Cada iglesia real tiene fuente y enlace Maps, y se distinguen sus datos verificados de los simulados?
13. ¿La cobertura incluye servicios y dominio con base sembrada, además de la prueba de dominio aislada?
