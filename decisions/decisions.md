# DEC-001: Diccionarios en memoria

## Estado

Aceptada.

## Contexto

Se necesita almacenar información de socios y pagos
sin utilizar una base de datos externa.
Se busca una solución sencilla para el sistema.

## Decisión

Se utilizarán diccionarios de Python en memoria
para almacenar los datos de socios y pagos.

La estructura será la siguiente:

```python
base_datos = {
    "socios": {},
    "pagos": {}
}
```

Los diccionarios permitirán organizar, consultar
y actualizar los registros durante la ejecución.

## Consecuencias

**Ventajas:**

- Implementación sencilla.
- No requiere dependencias externas.
- Facilita la organización de los datos.

**Limitaciones:**

- Los datos se pierden al cerrar el programa.
- Los datos no persisten entre ejecuciones.
- No ofrece persistencia ni transacciones.

## Justificación

Esta solución simplifica la implementación inicial.
Si los requisitos aumentan, se evaluará utilizar
una base de datos persistente.
