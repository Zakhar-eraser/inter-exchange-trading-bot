from pickle import dump
from pickle import load
from os.path import exists
from os import mkdir
from os.path import join
from typing import Callable

from lib.project_commons import Strings

from lib.overriden.Pair import CoinPair

def mkdir_force(path: str):
    if not exists(path):
        mkdir(path)

def initialize_project() -> None:
    mkdir_force(Strings.PROJECT_DIRECTORY)
    mkdir_force(Strings.LOGS_DIRECTORY)

async def load_or_create_pairs(fileName: str, get_func: Callable[[], list[CoinPair]]) -> list[CoinPair]:
    fileName = join(Strings.PROJECT_DIRECTORY, fileName + Strings.PAIRS_EXTENSION)
    if exists(fileName):
        with open(fileName, 'rb') as file:
            pairs = load(file)
    else:
        with open(fileName, 'wb') as file:
            pairs = await get_func()
            dump(pairs, file)
    return pairs