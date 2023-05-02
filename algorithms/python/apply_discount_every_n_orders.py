from operator import mul
from typing import List


class Cashier:  # pylint: disable=too-few-public-methods
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.i = 0
        self.n = n
        self.discount = (100 - discount) / 100
        self.prices = dict(zip(products, prices))

    def get_bill(self, products: List[int], amounts: List[int]) -> float:
        self.i = (self.i + 1) % self.n
        bill = sum(map(mul, map(self.prices.get, products), amounts))
        return bill if self.i else bill * self.discount


def test_example_1():
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    for (products, amounts), expected in zip(
        [
            [[1, 2], [1, 2]],
            [[3, 7], [10, 10]],
            [[1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]],
            [[4], [10]],
            [[7, 3], [10, 10]],
            [[7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]],
            [[2, 3, 5], [5, 3, 2]],
        ],
        [500.0, 4000.0, 800.0, 4000.0, 4000.0, 7350.0, 2500.0],
    ):
        assert cashier.get_bill(products, amounts) == expected
