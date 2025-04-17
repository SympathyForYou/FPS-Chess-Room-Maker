from config import IMAGE_PATHS
from logging import info  # (Built-in) Used to print classy messages
from functions import (
    ImageRecognition,
    Backend,
    RoomSetup,
)


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
        if ImageRecognition.is_on_screen(IMAGE_PATHS["white_wins"]):
            info("White Won")
            return 6
        if ImageRecognition.is_on_screen(IMAGE_PATHS["black_wins"]):
            info("Black Won")
            return 6
        if ImageRecognition.is_on_screen(IMAGE_PATHS["player_left"]):
            info("Player Left")
            return 6
        if ImageRecognition.is_on_screen(IMAGE_PATHS["pending_connection_failure"]):
            info("Connection Failed")
            return 7


# The main flow of the program is here
@Backend.measure_time
def main() -> None:
    """
    Creates a lobby by looping through a few functions -- Based on game_mode_flag and define_stage function.
    :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
    """
    info("Macro ON")
    
    USER_INPUT: str = Backend.user_input()
    WIN_LOSS_SCENARIO: int = 6

    while True:  # This program doesn't have a concrete way to stop
        info("Detecting stage...")
        current_stage: int = detect_stage() # Get current stage

        FUNCTIONS: tuple = (
            RoomSetup.find_host_button,
            RoomSetup.set_room_name,
            RoomSetup.set_description,
            RoomSetup.set_game_mode,
            RoomSetup.create_room,
            RoomSetup.close_invites,
        )
        
        IMAGES: tuple = (
            IMAGE_PATHS["host_text_in_main_menu"],
            IMAGE_PATHS["room_name_text_box"],
            IMAGE_PATHS["description_text_box"],
            IMAGE_PATHS["shiny_game_mode_checkbox"],
            IMAGE_PATHS["create_room_button"],
            IMAGE_PATHS["close_invites_button"],
        )

        info("Creating lobby...")
        # Looping through room creating stages
        if current_stage < WIN_LOSS_SCENARIO:
            for func, image in zip(FUNCTIONS[current_stage:], IMAGES[current_stage:]):
                func(image, USER_INPUT) 

        # Game Over
        else:
            RoomSetup.game_ended(IMAGE_PATHS["return_to_main_menu_button"], USER_INPUT)


if __name__ == "__main__":
    main()
