def game_comment_prompt(game_state: list[dict], n_prev_states: int = 3) -> str:
    current_state_str = get_state_str(game_state[-1])
    previous_states_str = ""
    for i in range(n_prev_states):
        previous_states_str += f"{get_state_str(game_state[-2 - i])}\n\n"

    return f"""Given the following game state, provide an appropriate, one-sentence, concise game commentary to entertain the audience that is natural and does not delve into too many details. Consider not only the current game state but also the previous three game states. This comment will be used as part of the live commentary system, along with other past and future messages. Outputs are in the specified JSON format between the code blocks (```json and ```).

# Game info
Game genre: 1v1 2D fighting game

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
    return f"""- Time left: {game_state["time_left"]}/1000
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
