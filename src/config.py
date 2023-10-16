from pathlib import Path

OUTPUTS_DIR_PATH = Path("outputs")
LOGS_FOLDER = Path("logs")
DATA_FOLDER = Path("data")

GAME_STATE_PATH = Path("Draw/game_log_converted.json")  # Change this for different game states
NUM_PREV_STATES = 2 # Change this for different number of previous states

PROMPT_COMPONENTS = [
    f"""# Game info
Game genre: 1v1 2D fighting game
Game scene: 960x640 (width x height)""",

    f"""# Constraints
- If both players are using same character, do not mention only the character name but also include `Player 1` or `Player 2` to avoid confusion""",

    f"""# Parameters
- `HP` is the health points of the player (max 400, starting from 400)
- `Energy` is the energy points of the player (max 300, starting from 0)
- `Position` is the position of the player in the game scene
- `Speed` is the speed of the player in the game scene (x is horizontal, y is vertical)
- `Direction` is the direction the player is facing
- `Character state` is the current state of the player (Stand -- the character is on the ground; Crouch -- the character is crouching; Air -- the character is in the air; Down -- the character is down, unable to control)
- `Action` is the current action of the player
- `Combo` is the current combo of the player""",
]
