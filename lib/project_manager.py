from pickle import dump
from pickle import load
from os.path import exists
from os import mkdir
from os.path import join

from asyncio import Task
from lib.structures.Pair import CoinPair

PROJECT_DIRECTORY = 'data/'

def initialize_project() -> None:
    if not exists(PROJECT_DIRECTORY):
        mkdir(PROJECT_DIRECTORY)

async def load_or_create_pairs(path: str, get_func: Task) -> list[CoinPair]:
    path = join(PROJECT_DIRECTORY, path)
    if exists(path):
        with open(path, 'rb') as file:
            pairs = load(file)
    else:
        with open(path, 'wb') as file:
            pairs = await get_func
            dump(pairs, file)
    return pairs