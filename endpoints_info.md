# Endpoints existentes

El repositorio actual no incluye la implementación de la aplicación, pero los tests definen los endpoints esperados:

- `GET /secure/`
  - Endpoint seguro protegido con autenticación HTTP Basic.
  - Se espera que devuelva `401` sin credenciales o con credenciales inválidas.
  - Debe devolver `200` con credenciales válidas (`admin` / `secret`).

- `POST /items/`
  - Crea un nuevo item con JSON de entrada.
  - Se espera que devuelva el item creado con un campo `id`.

- `GET /items/`
  - Lista items.
  - Debe aceptar parámetros de consulta `limit` y `offset` para paginación.

- `GET /items/{id}`
  - Recupera un item por su ID.

- `PUT /items/{id}`
  - Actualiza un item existente.

- `DELETE /items/{id}`
  - Elimina un item existente.

- `GET /items/search?name=a&sort=asc&limit=10&offset=0`
  - Busca items por nombre.
  - Debe filtrar por el texto `name` y devolver resultados según `sort`, `limit` y `offset`.

- `GET /openapi.json`
  - Debe exponer la documentación OpenAPI.
  - Se espera que `info.title` sea `Curso de FastAPI` y `info.version` sea `1.0.0`.

> Nota: estos endpoints se basan en los tests existentes, ya que la implementación del código de la API aún no está presente en el repositorio.
