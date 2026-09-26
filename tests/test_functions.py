import math
import statistics
from fractions import Fraction

import pytest

import media_calc
from media_calc import (
    mean,
    median,
    mode,
    multimode,
    sample_standard_deviation,
    sample_variance,
    standard_deviation,
    variance,
)

DATA = [2, 4, 4, 4, 5, 5, 7, 9]


def test_version():
    assert media_calc.__version__ == "0.3.0"


def test_readme_example():
    assert mean(DATA) == 5.0
    assert median(DATA) == 4.5
    assert mode(DATA) == 4
    assert variance(DATA) == 4.0
    assert standard_deviation(DATA) == 2.0


# --- mean ----------------------------------------------------------------


def test_mean_returns_float():
    result = mean([1, 2, 3])
    assert result == 2.0
    assert isinstance(result, float)


def test_mean_float_precision():
    # sum() accumulates error: sum([0.1] * 10) / 10 == 0.09999999999999999
    assert mean([0.1] * 10) == 0.1


def test_mean_negatives_and_fractions():
    assert mean([-1, 1]) == 0.0
    assert mean([Fraction(1, 2), Fraction(3, 2)]) == 1.0


# --- median --------------------------------------------------------------


def test_median_odd_and_even():
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 3, 2]) == 2.5


def test_median_does_not_modify_input():
    data = [3, 1, 2]
    median(data)
    assert data == [3, 1, 2]


# --- mode / multimode ----------------------------------------------------


def test_mode_tie_returns_first_seen():
    assert mode([3, 1, 1, 3]) == 3


def test_mode_accepts_non_numeric_values():
    assert mode(["red", "blue", "red"]) == "red"


def test_multimode():
    assert multimode([1, 2, 2, 3, 3]) == [2, 3]
    assert multimode([5]) == [5]


# --- variance and standard deviation -------------------------------------


def test_sample_variance():
    assert sample_variance(DATA) == pytest.approx(32 / 7)
    assert sample_standard_deviation(DATA) == pytest.approx(math.sqrt(32 / 7))


def test_variance_single_value():
    assert variance([7]) == 0.0
    assert sample_variance([7]) == 0.0
    assert standard_deviation([7]) == 0.0


def test_variance_constant_data():
    assert variance([3.3] * 5) == 0.0


def test_variance_matches_statistics_module():
    data = [1.5, 2.25, 3.0, 10.75, -4.5, 0.0]
    assert variance(data) == pytest.approx(statistics.pvariance(data))
    assert sample_variance(data) == pytest.approx(statistics.variance(data))
    assert standard_deviation(data) == pytest.approx(statistics.pstdev(data))
    assert sample_standard_deviation(data) == pytest.approx(statistics.stdev(data))


# --- empty input ---------------------------------------------------------


@pytest.mark.parametrize(
    "func",
    [
        mean,
        median,
        variance,
        sample_variance,
        standard_deviation,
        sample_standard_deviation,
    ],
)
def test_empty_input_returns_zero(func):
    assert func([]) == 0.0


def test_mode_empty():
    assert mode([]) is None
    assert multimode([]) == []


# --- input types ---------------------------------------------------------


@pytest.mark.parametrize(
    "func, expected",
    [
        (mean, 5.0),
        (median, 4.5),
        (mode, 4),
        (variance, 4.0),
        (standard_deviation, 2.0),
    ],
)
def test_accepts_generators_and_tuples(func, expected):
    assert func(x for x in DATA) == expected
    assert func(tuple(DATA)) == expected


@pytest.mark.parametrize("func", [mean, median, variance, standard_deviation])
@pytest.mark.parametrize("value", [[1, "2", 3], [1, None], "123", 5])
def test_rejects_non_numeric_values(func, value):
    with pytest.raises(TypeError):
        func(value)


# --- public API ----------------------------------------------------------


def test_import_from_functions_module():
    from media_calc.functions import mean, median, mode, standard_deviation, variance

    assert mean(DATA) == 5.0
    assert median(DATA) == 4.5
    assert mode(DATA) == 4
    assert variance(DATA) == 4.0
    assert standard_deviation(DATA) == 2.0


def test_all_exports_existing_callables():
    for name in media_calc.__all__:
        assert callable(getattr(media_calc, name))
