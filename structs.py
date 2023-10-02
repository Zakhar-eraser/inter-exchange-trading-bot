from enum import Enum

from lib.overriden.Pair import CoinPair

class TradeStates(Enum):
    UNITIAILIZED = -1
    PRICE_AWAIT = 0
    LONG_CONFIRM_CHECK = 1
    PRICE_ALIGN_AWAIT = 2
    SHORT_CONFIRM_CHECK = 3

class TradeInfo:
    def __init__(self, pair: CoinPair = CoinPair('', '', 0, 0)) -> None:
        self.symbol = pair
        self.order_id: str = ''
        self.tm_cur_price: float = 0.
        self.bm_cur_price: float = 0.
        self.purchase_price: float = 0.
        self.selling_price: float = 0.
        self.state: int = TradeStates.UNITIAILIZED

    def __eq__(self, __value: CoinPair) -> bool:
        return self.symbol == __value