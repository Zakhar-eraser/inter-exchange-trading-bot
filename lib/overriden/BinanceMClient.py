from cryptoxlib.clients.binance.BinanceClient import BinanceClient
from lib.overriden.Pair import CoinPair

class BinanceMClient(BinanceClient):
    """Modified version of cryptoxlib binance client: get all market pairs function added"""
    async def get_all_pairs(self) -> list[CoinPair]:
        pairs = await self.get_exchange_info()
        pairs = pairs['response']['symbols']
        pairs = [CoinPair(pair['baseAsset'], pair['quoteAsset'], pair['quoteAssetPrecision'], pair['baseAssetPrecision']) for pair in pairs]
        return pairs