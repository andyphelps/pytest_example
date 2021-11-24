from pathlib import Path


class CalculatorException(Exception):
    ...


class Calculator:

    def add(self, left: int, right: int) -> int:
        return left + right

    def divide(self, left: int, right: int) -> float:
        try:
            return left / right
        except ZeroDivisionError as ex:
            raise CalculatorException("Divide by zero", ex)

    def add_write_to_file(self, path: Path, left: int, right: int) -> int:
        answer: int = self.add(left, right)
        with open(path, "w") as f:
            f.write(str(answer))
