# media-calc

[![PyPI version](https://img.shields.io/pypi/v/media-calc.svg)](https://pypi.org/project/media-calc/)
[![Python Versions](https://img.shields.io/pypi/pyversions/media-calc.svg)](https://pypi.org/project/media-calc/)
[![Tests](https://github.com/omardev29/media-calc/actions/workflows/tests.yml/badge.svg)](https://github.com/omardev29/media-calc/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A small, dependency-free Python library for basic statistics: mean, median,
mode, variance and standard deviation.

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

Install it as `media-calc` and import it as `media_calc`.

## Usage

```python
from media_calc import mean, median, mode, variance, standard_deviation

numbers = [2, 4, 4, 4, 5, 5, 7, 9]

print(mean(numbers))                # 5.0
print(median(numbers))              # 4.5
print(mode(numbers))                # 4
print(variance(numbers))            # 4.0
print(standard_deviation(numbers))  # 2.0
```

Every function accepts any iterable of numbers (lists, tuples, `range`,
generators...), not only lists.

## Available functions

| Function                          | Description                                                              |
| --------------------------------- | ------------------------------------------------------------------------ |
| `mean(data)`                      | Arithmetic mean                                                          |
| `median(data)`                    | Middle value (average of the two middle values if the count is even)    |
| `mode(data)`                      | Most frequent value (the first one seen, on ties)                        |
| `multimode(data)`                 | All the most frequent values, in order of appearance                    |
| `variance(data)`                  | Population variance (divides by `n`)                                     |
| `sample_variance(data)`           | Sample variance (divides by `n - 1`)                                     |
| `standard_deviation(data)`        | Population standard deviation                                            |
| `sample_standard_deviation(data)` | Sample standard deviation                                                |

`mode` and `multimode` work with any hashable values, so they can also be
used with non-numeric data:

```python
mode(["red", "blue", "red"])   # 'red'
multimode([1, 2, 2, 3, 3])     # [2, 3]
```

### Population vs. sample

`variance` and `standard_deviation` treat the data as the whole population.
If your data is a sample of a bigger population, use `sample_variance` and
`sample_standard_deviation`:

```python
variance(numbers)          # 4.0
sample_variance(numbers)   # 4.571428571428571
```

### Empty input and invalid values

Empty input never raises:

- `mean`, `median`, `variance`, `standard_deviation` and their sample
  versions return `0.0` (the variances also return `0.0` for a single value).
- `mode` returns `None` and `multimode` returns `[]`.

Passing something that is not a number (for example `"3"` or `None`) to a
numeric function raises `TypeError` with a clear message, instead of failing
somewhere inside the calculation.

### Version

```python
import media_calc
print(media_calc.__version__)
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
