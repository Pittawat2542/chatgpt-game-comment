import json
import logging
import os
import time

import openai
from dotenv import load_dotenv

from src.config import DATA_FOLDER, GAME_STATE_PATH, PROMPT_COMPONENTS, NUM_PREV_STATES
from src.prompt import game_comment_prompt


def run_task(selected_game_state: list[dict]) -> None:
    for idx, component in enumerate(PROMPT_COMPONENTS + ["All"]):
        logging.info("Component %s:", component)
        enable_prompt_component = []
        for k in range(len(PROMPT_COMPONENTS)):
            if k != idx:
                enable_prompt_component.append(True)
            else:
                enable_prompt_component.append(False)

        prompt = game_comment_prompt(selected_game_state, enable_prompt_component, NUM_PREV_STATES)

        logging.info('Prompt_' + str(idx+1))
        print(prompt)


if __name__ == '__main__':
    load_dotenv()

    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    with open(os.path.join(DATA_FOLDER, GAME_STATE_PATH), 'r') as data_file:
        game_state = json.load(data_file)

    game_state_idxs = [len(game_state) - 1]
    for i in game_state_idxs:
        logging.info(f"Running task for game state {i}.")
        run_task(game_state[i - NUM_PREV_STATES:i + 1])
