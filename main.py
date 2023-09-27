import json
import logging
import os
import time

import openai
from dotenv import load_dotenv

from src.config import LOGS_FOLDER, DATA_FOLDER
from src.models import chatgpt
from src.prompt import game_comment_prompt
from src.utils import parse_json


def run_task(game_state: list[dict]) -> None:
    logging.info(f"Starting game comment generation.")
    for component in range(4):
        logging.info("Component %s:", component)
        prompt = game_comment_prompt(game_state, 2, component)
        logging.info(f"Interacting with ChatGPT API.")
        # logging.info(f"Prompt: {prompt}")
        response = chatgpt(prompt)
        logging.info(f"Finished interacting with ChatGPT API.")
        logging.info(f"Response: {response}")
        try:
            parsed_response = parse_json(response)
            # with open(f'{LOGS_FOLDER}/{time.strftime("%Y%m%d-%H%M%S")}.txt', 'w', encoding="utf-8") as raw_file:
            #     logging.info(f"Saving raw response.")
            #     raw_file.write(response)

            # with open(f'{LOGS_FOLDER}/{time.strftime("%Y%m%d-%H%M%S")}.json', 'w', encoding="utf-8") as parsed_file:
            #     logging.info(f"Saving parsed response.")
            #     parsed_file.write(json.dumps(parsed_response, indent=2))
            logging.info(f"Finished game comment generation.")
        except json.decoder.JSONDecodeError as e:
            logging.error(f"Failed to parse response: {e}")
            run_task([])  # TODO: Replace with actual state


if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)

    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(format=FORMAT, filename=f'{LOGS_FOLDER}/{time.strftime("%Y%m%d-%H%M%S")}.log',
                        level=logging.INFO,
                        filemode='a', datefmt='%Y-%m-%d %H:%M:%S')
    # logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    with open(os.path.join(DATA_FOLDER, "P2Slow/game_state.json"), 'r') as data_file:
        game_state = json.load(data_file)

    selected_game_state = [3, (len(game_state) + 2) // 2, len(game_state) - 1]
    for i in selected_game_state:
        logging.info(f"Running task for game state {i}.")
        run_task(game_state[i-2:i+1])
