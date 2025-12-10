Type hints in Python are used to indicate the expected types of variables, function parameters, and return values, improving readability and enabling static error checking.

# Sum data with Type Hints
This project demonstrates how to use **Python type hints** in a simple function that reads a text file containing a list of floats (one per line) and returns their sum.

# file
- `sum-data-with-type-hints.py`: This file contains a Python example demonstrating the use of type hints.
- `dados.txt`: Simple database example.

## Example

```python
from typing import TextIO

def sum_data(file: TextIO) -> float:
    """
    Reads a text file containing a list of floats (one per line)
    and returns the sum of these values.
    """
    return sum(float(line.strip()) for line in file)

with open("data.txt", "r") as f:
    result = sum_data(f)

print(result)  # Output: 36.0
