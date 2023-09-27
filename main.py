import json
import logging
import os
import time

import openai
from dotenv import load_dotenv
from tqdm import tqdm

from src.config import LOGS_FOLDER, DATA_FOLDER, GAME_STATE_PATH, OUTPUTS_DIR_PATH, PROMPT_COMPONENTS, NUM_PREV_STATES
from src.models import chatgpt
from src.prompt import game_comment_prompt
from src.utils import parse_json


def run_task(selected_game_state: list[dict]) -> None:
    logging.info(f"Starting game comment generation.")
    for idx, component in enumerate(tqdm(PROMPT_COMPONENTS, desc="Prompt components")):
        logging.info("Component %s:", component)
        enable_prompt_component = []
        for k in range(len(PROMPT_COMPONENTS)):
            if k != idx:
                enable_prompt_component.append(True)
            else:
                enable_prompt_component.append(False)

        prompt = game_comment_prompt(selected_game_state, enable_prompt_component, NUM_PREV_STATES)

        logging.info(f"Interacting with ChatGPT API.")
        response = chatgpt(prompt)
        logging.info(f"Finished interacting with ChatGPT API.")
        logging.info(f"Response: {response}")

        try:
            parsed_response = parse_json(response)
            with open(f'{OUTPUTS_DIR_PATH}/raw/{time.strftime("%Y%m%d-%H%M%S")}.txt', 'w',
                      encoding="utf-8") as raw_file:
                logging.info(f"Saving raw response.")
                raw_file.write(response)

            with open(f'{OUTPUTS_DIR_PATH}/parsed/{time.strftime("%Y%m%d-%H%M%S")}.json', 'w',
                      encoding="utf-8") as parsed_file:
                logging.info(f"Saving parsed response.")
                parsed_file.write(json.dumps(parsed_response, indent=2))

            logging.info(f"Finished game comment generation.")
        except json.decoder.JSONDecodeError as e:
            logging.error(f"Failed to parse response: {e}")
            run_task(selected_game_state)


def prepare_output_dirs():
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)

    if not os.path.exists(OUTPUTS_DIR_PATH):
        os.makedirs(OUTPUTS_DIR_PATH)

    if not os.path.exists(f'{OUTPUTS_DIR_PATH}/raw'):
        os.makedirs(f'{OUTPUTS_DIR_PATH}/raw')

    if not os.path.exists(f'{OUTPUTS_DIR_PATH}/parsed'):
        os.makedirs(f'{OUTPUTS_DIR_PATH}/parsed')


if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prepare_output_dirs()

    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(format=FORMAT, filename=f'{LOGS_FOLDER}/{time.strftime("%Y%m%d-%H%M%S")}.log',
                        level=logging.INFO,
                        filemode='a', datefmt='%Y-%m-%d %H:%M:%S')

    with open(os.path.join(DATA_FOLDER, GAME_STATE_PATH), 'r') as data_file:
        game_state = json.load(data_file)

    game_state_idxs = [3, (len(game_state) + NUM_PREV_STATES) // 2, len(game_state) - 1]
    for i in tqdm(game_state_idxs, desc="Game state"):
        logging.info(f"Running task for game state {i}.")
        run_task(game_state[i - NUM_PREV_STATES:i + 1])
