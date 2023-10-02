from cryptoxlib.Pair import Pair
from typing import Any

class CoinPair(Pair):
    def __init__(self, base: str, quote: str, pricePrecision: int = 0, amountPrecision: int = 0) -> None:
        super().__init__(base, quote)
        self.costPrecision = pricePrecision
        self.amountPrecision = amountPrecision

    def __eq__(self, __value: Any) -> bool:
        return self.__hash__() == hash(__value)
    
    def __hash__(self) -> int:
        return hash(self.base + self.quote)