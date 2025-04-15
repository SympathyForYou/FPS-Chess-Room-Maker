from config import IMAGE_PATHS
import logging  # (Built-in) Used to print classy messages
from functions import (
    ImageRecognition,
    Backend,
    Stage,
)

# Function used to detect the current stage of the game
def detect_stage() -> int:
    """
    Takes a look at your screen using is_on_screen() and figures out what stage you are on.
    :return: An integer corresponding to the looping sequnce of stages.
    """
    while True:
        if ImageRecognition.is_on_screen(IMAGE_PATHS["host_text_in_main_menu"]):
            return 0
        if ImageRecognition.is_on_screen(IMAGE_PATHS["room_name_text_box"]):
            return 1
        if ImageRecognition.is_on_screen(IMAGE_PATHS["description_text_box"]):
            return 2
        if ImageRecognition.is_on_screen(IMAGE_PATHS["shiny_game_mode_checkbox"], confidence=0.95):
            return 3
        if ImageRecognition.is_on_screen(IMAGE_PATHS["create_room_button"]):
            return 4
        if ImageRecognition.is_on_screen(IMAGE_PATHS["close_invites_button"]):
            return 5
        if ImageRecognition.is_on_screen(IMAGE_PATHS["player_left"]):
            logging.info("Player Left")
            return 6
        if ImageRecognition.is_on_screen(IMAGE_PATHS["white_wins"]):
            logging.info("White Won")
            return 6
        if ImageRecognition.is_on_screen(IMAGE_PATHS["black_wins"]):
            logging.info("Black Won")
            return 6
        if ImageRecognition.is_on_screen(IMAGE_PATHS["pending_connection_failure"]):
            logging.info("Connection Failed")
            return 7

# The main flow of the program is here
@Backend.measure_time
def create_lobby(game_mode_flag: bool) -> None:
    """
    Creates a lobby by looping through a few functions -- Based on game_mode_flag and define_stage function.
    :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
    :return: None
    """
    WIN_LOSS_SCENARIO: int = 6
     
    logging.info("Detecting stage...")
    current_stage: int = detect_stage() # Get current stage

    functions: list = [
        Stage.find_host_button,
        Stage.set_room_name,
        Stage.set_description,
        Stage.set_game_mode,
        Stage.create_room,
        Stage.close_invites,
        ]

    logging.info("Creating lobby...")
    # Looping through stages
    if current_stage < WIN_LOSS_SCENARIO:
        for func in functions[current_stage:]:
                func(game_mode_flag)

    # Game Over
    else:
        Stage.game_ended(game_mode_flag)


def main() -> None:
    logging.info("Macro ON")
    USER_INPUT: str = Backend.user_input()  # So the program won't ask for another input when looping once
    while True:  # This program doesn't have a concrete way to stop
        create_lobby(USER_INPUT)


if __name__ == "__main__":
    main()
