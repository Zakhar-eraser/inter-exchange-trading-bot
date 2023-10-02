import asyncio
import pickle

from structs import TradeInfo

import lib.project_manager as pm
from lib.overriden.Pair import CoinPair

#/api/v1/market/symbols 10 seconds /time
#/ticker 10 seconds / 5 times
#/api/v1/market/depth 10 seconds / 5 times
#/api/v1/market/trades 10 seconds /time
#/api/v1/market/kline 10 seconds /time
#
#/api/v1/fund/mainAccount seconds / 2times
#/api/v1/fund/allAccount 30seconds / 2times
#/api/v1/trade/placeOrder 10 seconds / 20 times
#/api/v1/trade/placeMultiOrder 10 seconds / 2times
#/api/v1/trade/cancelOrder 10 seconds / 20times
#/api/v1/trade/cancelMultiOrder 10 seconds /time
#/api/v1/trade/cancelAllOrder 10 seconds /time
#/api/v1/trade/orderInfo 10 seconds / 20times
#/api/v1/trade/multiOrderInfo 10 seconds / 2times

#POST https://api.bitforex.com/api/v1/trade/orderInfo
## Response
#{
#	"success": true,
#	"data": {
#		"symbol":"coin-usd-etc",
#		"avgPrice": 0,
#		"createTime": 1516691438000,
#                "lastTime": 1516691438000,
#		"dealAmount": 0,
#		"orderAmount": 2,
#		"orderId": 1,
#		"orderPrice": 103,
#		"orderState": 4,
#		"tradeFee": 0,
#		"tradeType": 2
#	}
#}

class Trade:
    def __init__(self, trading_client, base_client) -> None:
        self._trading_client = trading_client
        self._base_client = base_client
        self._stop_trading = False
        self._infos: set[TradeInfo] = {}
    def set_pairs(self, pairs: list[CoinPair]) -> None:
        self._pairs = pairs
    async def trade_task(self, info: TradeInfo):
        pass
    async def run(self):
        self._infos = {TradeInfo(pair) for pair in self._pairs}
        log_file = open(pm.Strings.LOG_FILE, 'a')
        self._trading_client.
        while self._stop_trading is False:
            try:
                async with asyncio.TaskGroup() as tg:
                    for info in self._infos:
                        tg.create_task(self.trade_task(info))
            except KeyboardInterrupt:
                self._stop_trading = True
        log_file.close()
        

async def main():
    pm.initialize_project()
    trader = Trade(pm.get_trading_client(), pm.get_base_client())
    with open(pm.Strings.FILTERED_PAIRS, 'rb') as file:
        pairs = pickle.load(file)
    trader.set_pairs(pairs)
    await trader.run()

if __name__ == '__main__':
    asyncio.run(main())
