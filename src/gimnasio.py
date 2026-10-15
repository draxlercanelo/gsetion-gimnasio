"""
Proyecto Integrador: Gestión de Gimnasio

Practica Semana 1 - Clean Code.
Modulo para gestionar socios, pagos y membresias.
"""

base_datos = {
    'socios': {},
    'pagos': {}
}


def registrar_socio(*args, **kwargs):
    """Registra un socio en la base de datos en memoria."""
    identificador = kwargs.get(
        'identificador', args[0] if args else None
    )

    if identificador is None:
        return "Error: falta el identificador del socio."

    if identificador in base_datos['socios']:
        return "Error: el socio ya está registrado."

    socio = kwargs.copy()
    socio.pop('identificador', None)

    if args and len(args) > 1:
        socio.setdefault('nombre', args[1])

    socio.setdefault('activo', True)
    socio.setdefault('congelada', False)

    base_datos['socios'][identificador] = socio

    return f"Socio {identificador} registrado correctamente."


def registrar_pago_mensualidad(*args, **kwargs):
    """Registra el pago de la mensualidad de un socio."""
    identificador = kwargs.get(
        'identificador', args[0] if args else None
    )
    monto = kwargs.get('monto', args[1] if len(args) > 1 else None)

    if identificador not in base_datos['socios']:
        return "Error: el socio no está registrado."

    if not isinstance(monto, (int, float)) or isinstance(monto, bool):
        return "Error: el monto debe ser numérico."

    if monto <= 0:
        return "Error: el monto debe ser mayor que cero."

    pago = {
        'monto': monto,
        'estado': 'pagado'
    }

    base_datos['pagos'].setdefault(identificador, []).append(pago)

    return f"Pago registrado para el socio {identificador}."


def verificar_acceso(*args, **kwargs):
    """Verifica si un socio cumple las condiciones básicas de acceso."""
    identificador = kwargs.get(
        'identificador', args[0] if args else None
    )

    socio = base_datos['socios'].get(identificador)

    if socio is None:
        return "Acceso denegado: socio no registrado."

    if not socio.get('activo', True):
        return "Acceso denegado: socio dado de baja."

    if socio.get('congelada', False):
        return "Acceso denegado: membresía congelada."

    pagos = base_datos['pagos'].get(identificador, [])

    if not any(pago.get('estado') == 'pagado' for pago in pagos):
        return "Acceso denegado: no hay pagos registrados."

    return "Acceso permitido."


def congelar_membresia(*args, **kwargs):
    """Congela la membresía de un socio registrado."""
    identificador = kwargs.get(
        'identificador', args[0] if args else None
    )

    socio = base_datos['socios'].get(identificador)

    if socio is None:
        return "Error: el socio no está registrado."

    if not socio.get('activo', True):
        return "Error: el socio está dado de baja."

    socio['congelada'] = True

    return f"Membresía del socio {identificador} congelada."


def dar_baja_socio(*args, **kwargs):
    """Da de baja a un socio registrado."""
    identificador = kwargs.get(
        'identificador', args[0] if args else None
    )

    socio = base_datos['socios'].get(identificador)

    if socio is None:
        return "Error: el socio no está registrado."

    socio['activo'] = False

    return f"Socio {identificador} dado de baja."
