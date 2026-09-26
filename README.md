# media-calc

[![PyPI version](https://img.shields.io/pypi/v/media-calc.svg)](https://pypi.org/project/media-calc/)
[![Python Versions](https://img.shields.io/pypi/pyversions/media-calc.svg)](https://pypi.org/project/media-calc/)
[![Tests](https://github.com/omardev29/media-calc/actions/workflows/tests.yml/badge.svg)](https://github.com/omardev29/media-calc/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A small, dependency-free Python library for basic statistics: mean, median,
mode, variance and standard deviation. Function names are in Spanish, with
English aliases for every one of them.

## Installation

With **pip**:

```bash
pip install media-calc
```

With **uv**:

```bash
uv add media-calc          # add it as a dependency of your uv project
uv pip install media-calc  # or install it into the current environment
```

The distribution is called `media-calc`, but the package you import is `media`.

## Usage

```python
from media import media, mediana, moda, varianza, desviacion_estandar

numbers = [2, 4, 4, 4, 5, 5, 7, 9]

print(media(numbers))                # 5.0
print(mediana(numbers))              # 4.5
print(moda(numbers))                 # 4
print(varianza(numbers))             # 4.0
print(desviacion_estandar(numbers))  # 2.0
```

The same code with the English aliases:

```python
from media import mean, median, mode, variance, standard_deviation
```

Every function accepts any iterable of numbers (lists, tuples, `range`,
generators...), not only lists.

## Available functions

| Spanish                           | English alias                    | Description                                                      |
| --------------------------------- | -------------------------------- | ---------------------------------------------------------------- |
| `media(lista)`                    | `mean`                           | Arithmetic mean                                                  |
| `mediana(lista)`                  | `median`                         | Middle value (average of the two middle values if the count is even) |
| `moda(lista)`                     | `mode`                           | Most frequent value (the first one seen, on ties)                |
| `modas(lista)`                    | `multimode`                      | All the most frequent values, in order of appearance            |
| `varianza(lista)`                 | `variance`                       | Population variance (divides by `n`)                             |
| `varianza_muestral(lista)`        | `sample_variance`                | Sample variance (divides by `n - 1`)                             |
| `desviacion_estandar(lista)`      | `standard_deviation`             | Population standard deviation                                    |
| `desviacion_estandar_muestral(lista)` | `sample_standard_deviation`  | Sample standard deviation                                        |

`moda` and `modas` work with any hashable values, so they can also be used
with non-numeric data:

```python
moda(["red", "blue", "red"])   # 'red'
modas([1, 2, 2, 3, 3])          # [2, 3]
```

### Population vs. sample

`varianza` and `desviacion_estandar` treat the data as the whole population.
If your data is a sample of a bigger population, use `varianza_muestral` and
`desviacion_estandar_muestral`:

```python
varianza(numbers)            # 4.0
varianza_muestral(numbers)   # 4.571428571428571
```

### Empty input and invalid values

Empty input never raises:

- `media`, `mediana`, `varianza`, `desviacion_estandar` and their sample
  versions return `0.0` (the variances also return `0.0` for a single value).
- `moda` returns `None` and `modas` returns `[]`.

Passing something that is not a number (for example `"3"` or `None`) to a
numeric function raises `TypeError` with a clear message, instead of failing
somewhere inside the calculation.

### Version

```python
import media
print(media.__version__)
```

## Development

The project uses a standard `pyproject.toml`, so it works with both uv and
pip.

With uv:

```bash
uv sync          # create .venv and install the package + dev dependencies
uv run pytest    # run the tests
uv build         # build the sdist and wheel into dist/
```

With pip:

```bash
python -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install -e . pytest
pytest
```

See [CHANGELOG.md](CHANGELOG.md) for the release history.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
