from lib.structures.Pair import CoinPair

async def get_cross_pairs(pairs_1: list[CoinPair], pairs_2: list[CoinPair]) -> list[CoinPair]:
    if len(pairs_1) > len(pairs_2):
        base_pairs = pairs_1
        pairs = pairs_2
    else:
        base_pairs = pairs_2
        pairs = pairs_1
    cross_pairs = [p for p in pairs if p in base_pairs]
    return cross_pairs

async def filter_pairs_by_coin(pairs: list[CoinPair], symbol: str) -> list[CoinPair]:
    filtered_pairs = [pair for pair in pairs if pair.base == symbol or pair.quote == symbol]
    return filtered_pairs
