# Changelog

## 0.3.0

### Breaking changes

- The whole API is now in English. `media` was renamed to `mean`, and the
  internal module `media.funciones` was renamed to `media.functions`. The
  first parameter of every function is now called `data` (was `lista`).

### Fixed

- The README documented `mediana`, `moda`, `varianza` and
  `desviacion_estandar`, which never existed, so the README example failed
  with `ImportError`. The README now matches the real API.
- Passing a generator or other iterator no longer fails or gives wrong
  results (for example `variance` used to read its input twice).
- `mean` and the variances use `math.fsum`, so results no longer drift from
  accumulated rounding (`mean([0.1] * 10)` now returns `0.1`, not
  `0.09999999999999999`).
- Non-numeric values raise a clear `TypeError` instead of failing somewhere
  inside the calculation.
- Empty input now consistently returns `0.0` (a float) for numeric results.

### Added

- `sample_variance` and `sample_standard_deviation` (sample statistics,
  divide by `n - 1`).
- `multimode`, which returns every most frequent value.
- Type hints and a `py.typed` marker.
- Test suite and GitHub Actions workflows for tests and PyPI releases.

### Changed

- Packaging moved from `setup.py` to `pyproject.toml` (hatchling), so the
  project works with pip, uv and any other standard tool.
- Minimum Python version is now 3.8 (tested on 3.8 to 3.13).
- Removed build artifacts and bytecode (`dist/`, `*.egg-info`, `__pycache__`)
  from the repository.

## 0.2.5

- Initial public release with `media`, `median`, `mode`, `variance` and
  `standard_deviation`.
