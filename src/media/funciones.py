"""Funciones estadísticas de media-calc.

Todas las funciones aceptan cualquier iterable (listas, tuplas, ``range``,
generadores...) y lo recorren una sola vez. Las entradas vacías se manejan
sin lanzar excepciones: las medidas numéricas devuelven ``0.0`` y ``moda``
devuelve ``None``.
"""

from __future__ import annotations

import math
from collections import Counter
from numbers import Real
from typing import Hashable, Iterable, List, Optional, TypeVar

T = TypeVar("T", bound=Hashable)


def _numeros(lista: Iterable[Real]) -> List[Real]:
    """Materializa ``lista`` y comprueba que todos sus elementos son números reales."""
    if isinstance(lista, (str, bytes)):
        raise TypeError("se esperaba un iterable de números, no una cadena de texto")
    try:
        datos = list(lista)
    except TypeError:
        raise TypeError(
            f"se esperaba un iterable de números, no {type(lista).__name__}"
        ) from None
    for x in datos:
        if not isinstance(x, Real):
            raise TypeError(
                f"todos los valores deben ser números reales; "
                f"se encontró {x!r} ({type(x).__name__})"
            )
    return datos


def _suma_cuadrados(datos: List[Real]) -> float:
    """Suma de los cuadrados de las desviaciones respecto a la media."""
    m = media(datos)
    return math.fsum((x - m) ** 2 for x in datos)


def media(lista: Iterable[Real]) -> float:
    """Devuelve la media aritmética de una colección de números.

    Usa :func:`math.fsum` para evitar errores de redondeo acumulados
    (por ejemplo, ``media([0.1] * 10)`` devuelve exactamente ``0.1``).

    Args:
        lista: Iterable de números (enteros o decimales).

    Returns:
        La media aritmética, o ``0.0`` si no hay datos.

    Raises:
        TypeError: Si algún elemento no es un número.
    """
    datos = _numeros(lista)
    if not datos:
        return 0.0
    return math.fsum(datos) / len(datos)


def mediana(lista: Iterable[Real]) -> float:
    """Devuelve la mediana (valor central) de una colección de números.

    Si hay un número par de elementos, devuelve la media de los dos centrales.

    Args:
        lista: Iterable de números (enteros o decimales).

    Returns:
        La mediana, o ``0.0`` si no hay datos.

    Raises:
        TypeError: Si algún elemento no es un número.
    """
    datos = sorted(_numeros(lista))
    n = len(datos)
    if n == 0:
        return 0.0
    mitad = n // 2
    if n % 2 == 1:
        return datos[mitad]
    return (datos[mitad - 1] + datos[mitad]) / 2


def moda(lista: Iterable[T]) -> Optional[T]:
    """Devuelve el valor más frecuente de una colección.

    Funciona con cualquier valor *hashable* (números, cadenas, etc.). Si hay
    varios valores empatados, devuelve el que aparece primero; usa
    :func:`modas` para obtenerlos todos.

    Args:
        lista: Iterable de valores.

    Returns:
        El valor más frecuente, o ``None`` si no hay datos.
    """
    conteo = Counter(lista)
    if not conteo:
        return None
    return conteo.most_common(1)[0][0]


def modas(lista: Iterable[T]) -> List[T]:
    """Devuelve todos los valores más frecuentes, en orden de aparición.

    Args:
        lista: Iterable de valores.

    Returns:
        Lista con los valores más frecuentes, o ``[]`` si no hay datos.
    """
    conteo = Counter(lista)
    if not conteo:
        return []
    maximo = max(conteo.values())
    return [valor for valor, veces in conteo.items() if veces == maximo]


def varianza(lista: Iterable[Real]) -> float:
    """Devuelve la varianza poblacional (divide entre ``n``).

    Para la varianza de una muestra (divide entre ``n - 1``) usa
    :func:`varianza_muestral`.

    Args:
        lista: Iterable de números (enteros o decimales).

    Returns:
        La varianza poblacional, o ``0.0`` si hay menos de dos datos.

    Raises:
        TypeError: Si algún elemento no es un número.
    """
    datos = _numeros(lista)
    if len(datos) < 2:
        return 0.0
    return _suma_cuadrados(datos) / len(datos)


def varianza_muestral(lista: Iterable[Real]) -> float:
    """Devuelve la varianza muestral (corrección de Bessel, divide entre ``n - 1``).

    Args:
        lista: Iterable de números (enteros o decimales).

    Returns:
        La varianza muestral, o ``0.0`` si hay menos de dos datos.

    Raises:
        TypeError: Si algún elemento no es un número.
    """
    datos = _numeros(lista)
    if len(datos) < 2:
        return 0.0
    return _suma_cuadrados(datos) / (len(datos) - 1)


def desviacion_estandar(lista: Iterable[Real]) -> float:
    """Devuelve la desviación estándar poblacional (raíz de :func:`varianza`).

    Args:
        lista: Iterable de números (enteros o decimales).

    Returns:
        La desviación estándar poblacional, o ``0.0`` si hay menos de dos datos.

    Raises:
        TypeError: Si algún elemento no es un número.
    """
    return math.sqrt(varianza(lista))


def desviacion_estandar_muestral(lista: Iterable[Real]) -> float:
    """Devuelve la desviación estándar muestral (raíz de :func:`varianza_muestral`).

    Args:
        lista: Iterable de números (enteros o decimales).

    Returns:
        La desviación estándar muestral, o ``0.0`` si hay menos de dos datos.

    Raises:
        TypeError: Si algún elemento no es un número.
    """
    return math.sqrt(varianza_muestral(lista))


# Alias en inglés. ``median``, ``mode``, ``variance`` y ``standard_deviation``
# son los nombres que exportaba la versión 0.2.5 y se mantienen por compatibilidad.
mean = media
median = mediana
mode = moda
multimode = modas
variance = varianza
sample_variance = varianza_muestral
standard_deviation = desviacion_estandar
sample_standard_deviation = desviacion_estandar_muestral
