from pathlib import Path
from random import randint
from typing import Tuple, List

import pytest
import pytest_check as softly

from calculator import Calculator, CalculatorException


class TestCalculator:
    calculator: Calculator

    def setup_method(self):
        self.calculator = Calculator()

    def test_when_add_two_numbers_then_correct_answer_given(self) -> None:
        assert 7 == self.calculator.add(2, 5)

    @pytest.mark.parametrize("left, right, expected", [
        (-3, -5, -8),
        (2, -4, -2),
        (-4, 5, 1)
    ])
    def test_when_adding_positive_and_negative_numbers_then_correct_answer_given(
            self,
            left: int,
            right: int,
            expected: int) -> None:
        assert expected == self.calculator.add(left, right)

    def test_when_divide_by_zero_then_calculator_exception_raised(self):
        with pytest.raises(CalculatorException) as ex:
            self.calculator.divide(1, 0)

        assert "Divide by zero" in ex.value.args

    @pytest.fixture(scope="function")
    def random_sums(self) -> List[Tuple[int, int, int]]:
        return [(a := randint(0, 1000), b := randint(0, 1000), a + b) for _ in range(10)]

    def test_when_test_random_set_then_sums_are_correct(self, random_sums: List[Tuple[int, int, int]]) -> None:
        print(random_sums)
        assert all([self.calculator.add(a, b) == c for (a, b, c) in random_sums])

    def test_when_scope_class_then_random_sums_are_same(self, random_sums: List[Tuple[int, int, int]]) -> None:
        print(random_sums)
        assert True

    def test_when_write_sum_to_file_then_file_written(self, tmp_path: Path) -> None:
        self.calculator.add_write_to_file(tmp_path / "sum.txt", 3, 4)
        with open(tmp_path / "sum.txt", "r") as f:
            assert f.read() == "7"

    def test_when_multiple_asserts_then_softly_used(self) -> None:
        softly.equal(1, 2)
        softly.is_in(4, [1, 2, 3])
