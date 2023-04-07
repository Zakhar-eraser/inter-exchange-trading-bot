from cryptoxlib.clients.bitforex.BitforexClient import BitforexClient
from lib.structures.Pair import CoinPair

class BitforexMClient(BitforexClient):
    """Modified version of cryptoxlib bitforex client: get all market pairs function added"""
    async def get_all_pairs(self) -> list[CoinPair]:
        pairs = await self.get_exchange_info()
        pairs = pairs['response']['data']
        pairs = [CoinPair(*(pair['symbol'].upper().split('-')[1:][::-1])) for pair in pairs]
        return pairs