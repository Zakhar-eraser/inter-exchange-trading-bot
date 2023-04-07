from cryptoxlib.Pair import Pair

class CoinPair(Pair):
    def __eq__(self, __value: Pair) -> bool:
        return self.base == __value.base and self.quote == __value.quote