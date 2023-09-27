import json
import os.path
import time

from src.config import OUTPUTS_DIR_PATH


def sleep(seconds: int) -> None:
    """Sleep for a given number of seconds."""
    time.sleep(seconds)


def parse_json(json_str: str) -> dict:
    """Parse JSON string."""
    if "```json" in json_str and "```" in json_str:
        json_str = json_str.split("```json")[1]
        json_str = json_str.split("```")[0]
    if "```" in json_str and "```" in json_str:
        json_str = json_str.split("```")[1]
        json_str = json_str.split("```")[0]
    return json.loads(json_str)


def save_text_to_file(text: str, file_path: str) -> None:
    """Save text to file."""
    if not os.path.exists(OUTPUTS_DIR_PATH):
        os.makedirs(OUTPUTS_DIR_PATH)
    with open(os.path.join(OUTPUTS_DIR_PATH, file_path), 'w') as f:
        if ".json" in file_path:
            f.write(json.dumps(parse_json(text), indent=2))
        else:
            f.write(text)
