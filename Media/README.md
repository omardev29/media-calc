# media-calc

A comprehensive Python library for statistical calculations.

## Description

This library provides a set of robust statistical functions for data analysis. It's ideal for:
- Basic and advanced statistical analysis
- Data processing and exploration
- Educational projects
- Mathematical calculations
- Research and analysis

## Installation

```bash
pip install media-calc
```

## Usage

```python
from media import (
    media, 
    mediana, 
    moda, 
    varianza, 
    desviacion_estandar
)

# Sample data
numbers = [2, 4, 4, 4, 5, 5, 7, 9]

# Calculate basic statistics
print(f"Mean: {media(numbers)}")          # Output: 5.0
print(f"Median: {mediana(numbers)}")      # Output: 4.5
print(f"Mode: {moda(numbers)}")           # Output: 4
print(f"Variance: {varianza(numbers)}")   # Output: 4.0
print(f"Std Dev: {desviacion_estandar(numbers)}")  # Output: 2.0
```

## Available Functions

### Basic Statistics
- `media(lista)`: Calculate arithmetic mean of a list of numbers
- `mediana(lista)`: Find the middle value of a sorted list
- `moda(lista)`: Find the most frequent value

### Advanced Statistics
- `varianza(lista)`: Calculate the variance of the data
- `desviacion_estandar(lista)`: Calculate the standard deviation

### Empty List Handling
All functions handle empty lists gracefully:
- `media()`: returns 0
- `mediana()`: returns 0
- `moda()`: returns None
- `varianza()`: returns 0
- `desviacion_estandar()`: returns 0

### Version Information
You can check the current version of the library:
```python
import media
print(media.__version__)  # Shows current version
```

# 2.0: more funcioanalities added
# 2.1: better documentation
## License

This project is licensed under the MIT License.
