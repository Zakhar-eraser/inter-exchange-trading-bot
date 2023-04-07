from keys import BINANCE_KEY
from keys import BITFOREX_KEY
from lib.structures.Pair import CoinPair
from lib.structures.BitforexMClient import BitforexMClient
from lib.structures.BinanceMClient import BinanceMClient
from lib.pairs_filters import get_cross_pairs
from lib.pairs_filters import filter_pairs_by_coin
from lib.project_manager import load_or_create_pairs
from lib.project_manager import initialize_project

import asyncio

#LOG = logging.getLogger("cryptoxlib")
#LOG.setLevel(logging.DEBUG)
#LOG.addHandler(logging.StreamHandler())

BINANCE_PAIRS_FILE = 'binanace.prs'
BITFOREX_PAIRS_FILE = 'bitforex.prs'
BINANCE_BITFOREX_FILE = 'binance_bitforex.prs'
BINANCE_BITFOREX_FILTERED_FILE = 'binance_bitforex_filtered.prs'

async def main() -> None:
    initialize_project()
    bitforex_client = BitforexMClient(*BITFOREX_KEY)
    binance_client = BinanceMClient(*BINANCE_KEY)
    pairs = await asyncio.gather(load_or_create_pairs(BITFOREX_PAIRS_FILE,
                                                      asyncio.create_task(bitforex_client.get_all_pairs())),
                                 load_or_create_pairs(BINANCE_PAIRS_FILE,
                                                      asyncio.create_task(binance_client.get_all_pairs())))
    binance_bitforex_pairs = await load_or_create_pairs(BINANCE_BITFOREX_FILE,
                                                        asyncio.create_task(get_cross_pairs(*pairs)))
    filtered_binance_bitforex_pairs = await load_or_create_pairs(BINANCE_BITFOREX_FILTERED_FILE, 
                                                                 asyncio.create_task(filter_pairs_by_coin(binance_bitforex_pairs,
                                                                                                          'USDT')))
    await asyncio.gather(bitforex_client.close(), binance_client.close())
    print(filtered_binance_bitforex_pairs)

if __name__ == '__main__':
    asyncio.run(main())