# To-do

- [ ] Leer el `README.md` del repositorio para entender requisitos y arquitectura.
- [ ] Revisar cada prueba en `app/tests/` y listar qué endpoints/models/middleware se necesitan.
- [ ] Crear `app/main.py` con FastAPI y metadata:
  - title: "Curso de FastAPI"
  - version: "1.0.0"
- [ ] Crear `app/models.py` con el modelo `Usuario` y validaciones de email/nombre.
- [ ] Crear `app/routers/` con rutas:
  - `POST /items/`
  - `GET /items/{id}`
  - `PUT /items/{id}`
  - `DELETE /items/{id}`
  - `GET /items/?limit=&offset=`
  - `GET /items/search?name=&sort=&limit=&offset=`
  - `GET /secure/` con autenticación HTTP Basic
- [ ] Crear middleware en `app/core/` para logging de peticiones.
- [ ] Añadir `app/db/` si se necesita persistencia o usar almacenamiento en memoria.
- [ ] Ejecutar `pytest` y corregir errores hasta pasar todas las pruebas.
