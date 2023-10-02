from typing import Callable
from cryptoxlib.WebsocketMgr import Subscription
from cryptoxlib.CryptoXLibClient import CryptoXLibClient
from cryptoxlib.clients.bitforex.BitforexWebsocket import Ticker24hSubscription as BitforexTicker24hSubscription
from lib.overriden.BinanceWebsocketSubscriptions import IndividualSymbolTickerSubscription as BinanceTicker24hSubscription
from cryptoxlib.Pair import Pair

from lib.overriden.BinanceMClient import BinanceMClient
from lib.overriden.BitforexMClient import BitforexMClient
from lib.overriden.Pair import CoinPair
from keys import BITFOREX_KEY
from keys import BINANCE_KEY

class Strings:
    PAIRS_EXTENSION = '.prs'
    LOGS_DIRECTORY = 'logs/'
    LOG_FILE_NAME = 'moves'
    LOG_EXTENSION = '.log'
    LOG_FILE = LOGS_DIRECTORY + LOG_FILE_NAME + LOG_EXTENSION
    BASE_MARKET_NAME = 'binance'
    TRADING_MARKET_NAME = 'bitforex'
    PROJECT_DIRECTORY = 'data/'
    FILTERED_PAIRS = BASE_MARKET_NAME + '_' + TRADING_MARKET_NAME + '_' + 'filtered'
    QUOTE_COIN = 'USDT'

def map_trading(symbol: str) -> Pair:
    return Pair(*symbol['symbol'].upper().split('-')[1:][::-1])

def map_base(symbol: str) -> Pair:
    return Pair(symbol[0:symbol.find(Strings.QUOTE_COIN)])

def trading_client() -> CryptoXLibClient:
    return BitforexMClient(BITFOREX_KEY)

def base_client() -> CryptoXLibClient:
    return BinanceMClient(BINANCE_KEY)

def trading_subscription(pair: Pair, callbacks: list[Callable[[dict], None]]) -> Subscription:
    return BitforexTicker24hSubscription(pair, callbacks)

def base_subscription(pair: Pair, callbacks: list[Callable[[dict], None]]) -> Subscription:
    return BinanceTicker24hSubscription(pair, callbacks)