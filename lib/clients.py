from structs import TradeInfo
import lib.project_commons as pc
#from cryptoxlib.CryptoXLibClient import CryptoXLibClient

from lib.overriden.Pair import CoinPair

class TradingClient:
    def __init__(self) -> None:
        self._client = pc.trading_client()

    async def subscribe_on_pairs_tickets(self, pairs: list[CoinPair], infos: list[TradeInfo]) -> None:
        self._infos = infos
        self._client.compose_subscriptions([pc.trading_subscription(pair, [self._callback]) for pair in pairs])
        await self._client.start_websockets()
    
    def _callback(self) -> None:
        pass