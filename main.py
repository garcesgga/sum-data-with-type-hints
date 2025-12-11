from typing import TextIO

def sum_data(file: TextIO) -> float:
    return sum(float(line.strip()) for line in file)

with open("dados.txt", "r") as f:
    result = sum_data(f)

print(result)
