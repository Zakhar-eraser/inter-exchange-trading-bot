from lib.structures.Pair import CoinPair

class MarketsPair:
    """holder of trades on common markets` pairs"""

    def __init__(self, pairs: list[CoinPair], base_market_symbols: dict, trading_market_symbols: dict) -> None:
        self._pairs = pairs
        self._base_market_symbols = base_market_symbols
        self._trading_market_symbols = trading_market_symbols
        self.base_market = Market(pairs)
        
    
    def write_long_order(self, response: dict):
        pass

class Market:
    """holder of trades and prices on an market"""

    def __init__(self, pairs: list[CoinPair]) -> None:
        pass

class TradeInfo:
    """Info about tradings of pair"""
    WAITING: int = 0
    BUYING: int = 1
    SELLING: int = 2

    def __init__(self) -> None:
        self.state: int = TradeInfo.WAITING
        self.price: float = -1.
        self.buy_price: float = -1.
        self.sell_price: float = -1.
        self.order_id: int
