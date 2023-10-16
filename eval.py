import json
import logging
import os

from dotenv import load_dotenv

from src.config import LOGS_FOLDER
from src.eval import eval



if __name__ == '__main__':
    load_dotenv()

    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('Starting evaluation...')
    eval(LOGS_FOLDER)
