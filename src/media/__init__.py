"""media-calc: funciones estadísticas sencillas y sin dependencias."""

from .funciones import (
    desviacion_estandar,
    desviacion_estandar_muestral,
    mean,
    media,
    median,
    mediana,
    moda,
    modas,
    mode,
    multimode,
    sample_standard_deviation,
    sample_variance,
    standard_deviation,
    variance,
    varianza,
    varianza_muestral,
)

__version__ = "0.3.0"

__all__ = [
    # Nombres en español
    "media",
    "mediana",
    "moda",
    "modas",
    "varianza",
    "varianza_muestral",
    "desviacion_estandar",
    "desviacion_estandar_muestral",
    # Alias en inglés
    "mean",
    "median",
    "mode",
    "multimode",
    "variance",
    "sample_variance",
    "standard_deviation",
    "sample_standard_deviation",
]
