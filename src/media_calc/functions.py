"""Statistics functions for media-calc.

Every function accepts any iterable (lists, tuples, ``range``, generators...)
and reads it only once. Empty input never raises: numeric measures return
``0.0`` and ``mode`` returns ``None``.
"""

from __future__ import annotations

import math
from collections import Counter
from numbers import Real
from typing import Hashable, Iterable, List, Optional, TypeVar

T = TypeVar("T", bound=Hashable)


def _numbers(data: Iterable[Real]) -> List[Real]:
    """Materialize ``data`` and check that every element is a real number."""
    if isinstance(data, (str, bytes)):
        raise TypeError("expected an iterable of numbers, not a string")
    try:
        values = list(data)
    except TypeError:
        raise TypeError(
            f"expected an iterable of numbers, not {type(data).__name__}"
        ) from None
    for x in values:
        if not isinstance(x, Real):
            raise TypeError(
                f"all values must be real numbers; "
                f"found {x!r} ({type(x).__name__})"
            )
    return values


def _sum_of_squares(values: List[Real]) -> float:
    """Sum of the squared deviations from the mean."""
    m = mean(values)
    return math.fsum((x - m) ** 2 for x in values)


def mean(data: Iterable[Real]) -> float:
    """Return the arithmetic mean of a collection of numbers.

    Uses :func:`math.fsum` to avoid accumulated rounding errors
    (for example, ``mean([0.1] * 10)`` returns exactly ``0.1``).

    Args:
        data: Iterable of numbers (integers or floats).

    Returns:
        The arithmetic mean, or ``0.0`` if there is no data.

    Raises:
        TypeError: If any element is not a number.
    """
    values = _numbers(data)
    if not values:
        return 0.0
    return math.fsum(values) / len(values)


def median(data: Iterable[Real]) -> float:
    """Return the median (middle value) of a collection of numbers.

    With an even number of elements, returns the mean of the two middle values.

    Args:
        data: Iterable of numbers (integers or floats).

    Returns:
        The median, or ``0.0`` if there is no data.

    Raises:
        TypeError: If any element is not a number.
    """
    values = sorted(_numbers(data))
    n = len(values)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2


def mode(data: Iterable[T]) -> Optional[T]:
    """Return the most frequent value of a collection.

    Works with any hashable value (numbers, strings, etc.). On ties, returns
    the value that appears first; use :func:`multimode` to get all of them.

    Args:
        data: Iterable of values.

    Returns:
        The most frequent value, or ``None`` if there is no data.
    """
    counts = Counter(data)
    if not counts:
        return None
    return counts.most_common(1)[0][0]


def multimode(data: Iterable[T]) -> List[T]:
    """Return every most frequent value, in order of first appearance.

    Args:
        data: Iterable of values.

    Returns:
        List of the most frequent values, or ``[]`` if there is no data.
    """
    counts = Counter(data)
    if not counts:
        return []
    highest = max(counts.values())
    return [value for value, count in counts.items() if count == highest]


def variance(data: Iterable[Real]) -> float:
    """Return the population variance (divides by ``n``).

    For the variance of a sample (divides by ``n - 1``) use
    :func:`sample_variance`.

    Args:
        data: Iterable of numbers (integers or floats).

    Returns:
        The population variance, or ``0.0`` if there are fewer than two values.

    Raises:
        TypeError: If any element is not a number.
    """
    values = _numbers(data)
    if len(values) < 2:
        return 0.0
    return _sum_of_squares(values) / len(values)


def sample_variance(data: Iterable[Real]) -> float:
    """Return the sample variance (Bessel's correction, divides by ``n - 1``).

    Args:
        data: Iterable of numbers (integers or floats).

    Returns:
        The sample variance, or ``0.0`` if there are fewer than two values.

    Raises:
        TypeError: If any element is not a number.
    """
    values = _numbers(data)
    if len(values) < 2:
        return 0.0
    return _sum_of_squares(values) / (len(values) - 1)


def standard_deviation(data: Iterable[Real]) -> float:
    """Return the population standard deviation (square root of :func:`variance`).

    Args:
        data: Iterable of numbers (integers or floats).

    Returns:
        The population standard deviation, or ``0.0`` if there are fewer
        than two values.

    Raises:
        TypeError: If any element is not a number.
    """
    return math.sqrt(variance(data))


def sample_standard_deviation(data: Iterable[Real]) -> float:
    """Return the sample standard deviation (square root of :func:`sample_variance`).

    Args:
        data: Iterable of numbers (integers or floats).

    Returns:
        The sample standard deviation, or ``0.0`` if there are fewer than
        two values.

    Raises:
        TypeError: If any element is not a number.
    """
    return math.sqrt(sample_variance(data))
