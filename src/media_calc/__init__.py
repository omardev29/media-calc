"""media-calc: simple, dependency-free statistics functions."""

from .functions import (
    mean,
    median,
    mode,
    multimode,
    sample_standard_deviation,
    sample_variance,
    standard_deviation,
    variance,
)

__version__ = "0.3.0"

__all__ = [
    "mean",
    "median",
    "mode",
    "multimode",
    "variance",
    "sample_variance",
    "standard_deviation",
    "sample_standard_deviation",
]
