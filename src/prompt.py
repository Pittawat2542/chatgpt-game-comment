COMPONENTS = [

    f"""# Game info
Game genre: 1v1 2D fighting game
Game scene: 960x640 (width x height)
Game duration: 60 seconds""",

    f"""# Constraints
- If both players are using same character, do not mention only the character name but also include `Player 1` or `Player 2` to avoid confusion""",

    f"""# Parameters
- `Time left` is the time left in the game in seconds
- `HP` is the health points of the player (max 400, starting from 400)
- `Energy` is the energy points of the player (max 300, starting from 0)
- `Position` is the position of the player in the game scene
- `Speed` is the speed of the player in the game scene (x is horizontal, y is vertical)
- `Direction` is the direction the player is facing
- `Character state` is the current state of the player (Stand -- the character is on the ground; Crouch -- the character is crouching; Air -- the character is in the air; Down -- the character is down, unable to control)
- `Action` is the current action of the player
- `Combo` is the current combo of the player""",

]

def game_comment_prompt(game_state: list[dict], n_prev_states: int = 3, component: int = 3) -> str:
    current_state_str = get_state_str(game_state[-1])
    previous_states_str = ""
    for i in range(n_prev_states):
        previous_states_str += f"{get_state_str(game_state[-2 - i])}\n\n"

    return f"""Given the following game state, provide an appropriate, one-sentence, concise game commentary to entertain the audience that is natural and does not delve into too many details. Consider not only the current game state but also the previous three game states. This comment will be used as part of the live commentary system, along with other past and future messages. Outputs are in the specified JSON format between the code blocks (```json and ```).

{"" if component == 0 else COMPONENTS[0]}

{"" if component == 1 else COMPONENTS[1]}

{"" if component == 2 else COMPONENTS[2]}

# Game states
## Current game state
{current_state_str}

## Previous game states
{previous_states_str}

# Output format:
```json
{{
"comment": "generated comment"
}}
```"""


def get_state_str(game_state: dict) -> str:
    return f"""- Time left: {game_state["time_left"]} second(s)
### Player 1
- Name: {game_state["player_1"]["character_name"]}
- HP: {game_state["player_1"]["hp"]}/400
- Energy: {game_state["player_1"]["energy"]}/300
- Position:  "left": {game_state["player_1"]["position"]["left"]}, "right": {game_state["player_1"]["position"]["right"]},  "top": {game_state["player_1"]["position"]["top"]}, "bottom": {game_state["player_1"]["position"]["bottom"]}
- Speed: "x": {game_state["player_1"]["speed"]["x"]}, "y": {game_state["player_1"]["speed"]["y"]}
- Direction: {game_state["player_1"]["direction"]}
- Character state: {game_state["player_1"]["state"]}
- Action: {game_state["player_1"]["action"]}
- Combo: {game_state["player_1"]["combo"]}

### Player 2
- Name: {game_state["player_2"]["character_name"]}
- HP: {game_state["player_2"]["hp"]}/400
- Energy: {game_state["player_2"]["energy"]}/300
- Position:  "left": {game_state["player_2"]["position"]["left"]}, "right": {game_state["player_2"]["position"]["right"]},  "top": {game_state["player_2"]["position"]["top"]}, "bottom": {game_state["player_2"]["position"]["bottom"]}
- Speed: "x": {game_state["player_2"]["speed"]["x"]}, "y": {game_state["player_2"]["speed"]["y"]}
- Direction: {game_state["player_2"]["direction"]}
- Character state: {game_state["player_2"]["state"]}
- Action: {game_state["player_2"]["action"]}
- Combo: {game_state["player_2"]["combo"]}"""
