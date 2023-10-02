from lib.pairs_filters import get_cross_pairs
from lib.pairs_filters import filter_pairs_by_coin
from lib.project_manager import load_or_create_pairs
from lib.project_manager import Strings
from lib.project_manager import initialize_project
from lib.project_manager import get_trading_client
from lib.project_manager import get_base_client
from lib.structures.Pair import CoinPair

import asyncio

async def load_filtered_cross_pairs(trading_client, base_client, base_coin: str) -> list[CoinPair]:
    pairs = await load_pairs(trading_client, base_client)
    return await filter_pairs_by_coin(await load_or_create_pairs(Strings.TRADING_MARKET_NAME,
                                                                 lambda: asyncio.create_task(get_cross_pairs(*pairs))),
                                                                 base_coin)

async def load_pairs(trading_client, base_client) -> [list[CoinPair], list[CoinPair]]:
    return await asyncio.gather(load_or_create_pairs(Strings.TRADING_MARKET_NAME,
                                                      lambda: asyncio.create_task(trading_client.get_all_pairs())),
                                load_or_create_pairs(Strings.BASE_MARKET_NAME,
                                                      lambda: asyncio.create_task(base_client.get_all_pairs())))

async def main() -> None:
    initialize_project()
    trading_client = get_trading_client()
    base_client = get_base_client()
    filtered_cross_pairs = await load_or_create_pairs(Strings.FILTERED_PAIRS, 
                                                                 lambda: asyncio.create_task(load_filtered_cross_pairs(trading_client, base_client,
                                                                                                              Strings.QUOTE_COIN)))
    await asyncio.gather(trading_client.close(), base_client.close())
    print(filtered_cross_pairs)

if __name__ == '__main__':
    asyncio.run(main())