from cryptoxlib.clients.bitforex.BitforexClient import BitforexClient
from cryptoxlib.clients.bitforex.enums import OrderSide
from lib.overriden.Pair import CoinPair
from ssl import SSLContext

class BitforexMClient(BitforexClient):
    """Modified version of cryptoxlib bitforex client: get all market pairs function added"""
    def __init__(self, api_key: str = None, sec_key: str = None, api_trace_log: bool = False, ssl_context: SSLContext = None) -> None:
        super().__init__(api_key, sec_key, api_trace_log, ssl_context)
        self._test_order: int = 1

    async def get_all_pairs(self) -> list[CoinPair]:
        pairs = await self.get_exchange_info()
        pairs = pairs['response']['data']
        pairs = [CoinPair(*(pair['symbol'].upper().split('-')[1:][::-1]), pair['pricePrecision'], pair['amountPrecision']) for pair in pairs]
        return pairs

    async def create_test_order(self, pair: CoinPair, price: str, quantity: str, side: OrderSide) -> dict:
        response = {'response': {'success': True, 'data': {'orderId': self._test_order}}}
        self._test_order += 1
        return response
    
    async def cancel_all_test_orders(self, pair: CoinPair) -> dict:
        response = {'response': {'success': True, 'data': True}}
        return response