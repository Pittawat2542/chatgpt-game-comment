import json
import logging
import os
import time

import openai
from dotenv import load_dotenv

from src.config import LOGS_FOLDER
from src.models import chatgpt
from src.prompt import game_comment_prompt
from src.utils import parse_json

TEST_STATE = [{
    "player_1": {
        "character_name": "Zen",
        "hp": 249,
        "energy": 98,
        "position": {
            "left": 726,
            "right": 766,
            "top": 435,
            "bottom": 640
        },
        "speed": {
            "x": 0,
            "y": 0
        },
        "direction": "Right",
        "state": "Stand",
        "action": "Stand_recov",
        "control": False,
        "combo": 0
    },
    "player_2": {
        "character_name": "Zen",
        "hp": 31,
        "energy": 76,
        "position": {
            "left": 920,
            "right": 960,
            "top": 435,
            "bottom": 640
        },
        "speed": {
            "x": 0,
            "y": 0
        },
        "direction": "Left",
        "state": "Stand",
        "action": "Stand_d_df_fa",
        "control": False,
        "combo": 1
    },
    "time_left": 960,
    "projectiles": []
},
    {
        "player_1": {
            "character_name": "Zen",
            "hp": 249,
            "energy": 108,
            "position": {
                "left": 726,
                "right": 766,
                "top": 475,
                "bottom": 640
            },
            "speed": {
                "x": 0,
                "y": 0
            },
            "direction": "Right",
            "state": "Crouch",
            "action": "Crouch_fb",
            "control": False,
            "combo": 0
        },
        "player_2": {
            "character_name": "Zen",
            "hp": 19,
            "energy": 86,
            "position": {
                "left": 910,
                "right": 950,
                "top": 435,
                "bottom": 640
            },
            "speed": {
                "x": 0,
                "y": 0
            },
            "direction": "Left",
            "state": "Down",
            "action": "Rise",
            "control": False,
            "combo": 0
        },
        "time_left": 900,
        "projectiles": []
    },
    {
        "player_1": {
            "character_name": "Zen",
            "hp": 249,
            "energy": 98,
            "position": {
                "left": 454,
                "right": 494,
                "top": 435,
                "bottom": 640
            },
            "speed": {
                "x": 0,
                "y": 0
            },
            "direction": "Right",
            "state": "Stand",
            "action": "Throw_b",
            "control": False,
            "combo": 0
        },
        "player_2": {
            "character_name": "Zen",
            "hp": 19,
            "energy": 86,
            "position": {
                "left": 498,
                "right": 538,
                "top": 435,
                "bottom": 640
            },
            "speed": {
                "x": -1,
                "y": 0
            },
            "direction": "Left",
            "state": "Air",
            "action": "Stand_d_db_ba",
            "control": False,
            "combo": 0
        },
        "time_left": 840,
        "projectiles": []
    }
]


def run_task(game_state: list[dict]) -> None:
    logging.info(f"Starting game comment generation.")
    prompt = game_comment_prompt(TEST_STATE, 3)  # TODO: Replace with actual state
    logging.info(f"Interacting with ChatGPT API.")
    response = chatgpt(prompt)
    logging.info(f"Finished interacting with ChatGPT API.")

    try:
        parsed_response = parse_json(response)
        with open(f'{LOGS_FOLDER}/{time.strftime("%Y%m%d-%H%M%S")}.txt', 'w', encoding="utf-8") as raw_file:
            logging.info(f"Saving raw response.")
            raw_file.write(response)

        with open(f'{LOGS_FOLDER}/{time.strftime("%Y%m%d-%H%M%S")}.json', 'w', encoding="utf-8") as parsed_file:
            logging.info(f"Saving parsed response.")
            parsed_file.write(json.dumps(parsed_response, indent=2))
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

    run_task()
