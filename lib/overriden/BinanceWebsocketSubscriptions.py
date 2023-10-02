from cryptoxlib.WebsocketMgr import CallbacksType
from cryptoxlib.Pair import Pair
from cryptoxlib.clients.binance.BinanceCommonWebsocket import BinanceSubscription
from cryptoxlib.clients.binance.BinanceWebsocket import map_ws_pair

class IndividualSymbolTickerSubscription(BinanceSubscription):
    def __init__(self, pair: Pair, callbacks: CallbacksType):
        super().__init__(callbacks)

        self.pair = pair

    def get_channel_name(self):
        return f"{map_ws_pair(self.pair)}@miniTicker"