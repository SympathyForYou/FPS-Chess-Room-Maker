from config import IMAGE_PATHS, DESCRIPTION, NORMAL_ROOM_NAME, SHINY_ROOM_NAME  # Config
import pyautogui  # Used for mouse / keyboard inputs
import logging  # Used to log print messages
import time  # Used to make the program wait
from functions import (
    is_on_screen,
    find_and_click,
    clear_and_type,
    parse_arguments,
    measure_time,
)


def find_host_button() -> None:
    """
    Clicks on the host button that leads to the create room menu.
    :return: None
    """
    # Click on the Host Button
    if find_and_click(IMAGE_PATHS["host"]):
        logging.info("Clicked Host Button")
    else:
        main()


def set_room_name(shiny_mode) -> None:
    """
    Sets room's name based on the shiny flag.
    :param shiny_mode: See get_shiny_mode_from_input function.
    :return: None
    """
    # Set room name
    room_name = SHINY_ROOM_NAME if shiny_mode else NORMAL_ROOM_NAME
    if find_and_click(IMAGE_PATHS["room_name"]):
        clear_and_type(room_name)
        logging.info(f"Set room name to: {room_name}")
    else:
        main()


def set_description() -> None:
    """
    Sets room's description.
    :return: None
    """
    if find_and_click(IMAGE_PATHS["description"]):
        clear_and_type(DESCRIPTION)
        logging.info(f"Set description to: {DESCRIPTION}")
    else:
        main()


def set_game_mode(shiny_mode) -> None:
    """
    Clicks on the shiny game-mode checkbox.
    :param shiny_mode: See get_shiny_mode_from_input function.
    :return: None
    """
    # Set game-mode
    if shiny_mode:
        if find_and_click(IMAGE_PATHS["shiny"], confidence=0.95):
            logging.info("Activated Shiny Game Mode")
        else:
            main()


def create_room() -> None:
    """
    Clicks on the launch room button.
    :return: None
    """
    # Creates a room
    if find_and_click(IMAGE_PATHS["create_room"]):
        logging.info("Lobby Launched")
    else:
        main()


def close_invites() -> None:
    """
    Closes the friends invite window.
    :return: None
    """
    # Close invites
    if find_and_click(IMAGE_PATHS["close"]):
        logging.info("Closed invites window")
    else:
        main()


def game_ended(shiny_mode) -> None:
    """
    Whenever someone wins / player leaves it quits to main menu.
    :param shiny_mode: See get_shiny_mode_from_input function.
    :return: None
    """
    # Set description
    pyautogui.hotkey("esc")
    if find_and_click(IMAGE_PATHS["menu"], times=2):
        create_lobby(shiny_mode)
        logging.info("Restart game.")
    else:
        main()


def define_stage() -> int:
    """
    Takes a look at your screen using is_on_screen(image) and figures out what stage you on.
    :return: An integer corresponding to the current stage your game is that gets plugged into a list.
    """
    while True:
        if is_on_screen(IMAGE_PATHS["host"]):
            return 0
        elif is_on_screen(IMAGE_PATHS["room_name"]):
            return 1
        elif is_on_screen(IMAGE_PATHS["description"]):
            return 2
        elif is_on_screen(IMAGE_PATHS["shiny"], 0.95):
            return 3
        elif is_on_screen(IMAGE_PATHS["create_room"]):
            return 4
        elif is_on_screen(IMAGE_PATHS["close"]):
            return 5
        elif is_on_screen(IMAGE_PATHS["left"]):
            logging.info("Player Left")
            return 7
        elif is_on_screen(IMAGE_PATHS["white"]):
            logging.info("White Won")
            return 7
        elif is_on_screen(IMAGE_PATHS["black"]):
            logging.info("Black Won")
            return 7
        elif is_on_screen(IMAGE_PATHS["failure"]):
            logging.info("Connection Failed")
            return 8
        elif is_on_screen(IMAGE_PATHS["host_left"]):
            return 8
        # print("full rotation")


# The main flow of the program is here
@measure_time
def create_lobby(shiny_mode: bool) -> None:
    """
    Creates a game lobby based on the shiny_mode flag and current_stage function.
    :param shiny_mode: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
    :return: None
    """

    # Functions to loop through
    functions = [
        find_host_button,
        set_room_name,
        set_description,
        set_game_mode,
        create_room,
        close_invites,
    ]
    current_stage = define_stage()

    # print(current_stage) -- Debug
    # Looping sequence
    if current_stage < 7:
        for func in functions[current_stage:]:
            # print(functions[current_stage].__name__) -- Debug
            func_name = func.__name__

            if func_name not in ["set_room_name", "set_game_mode", "game_ended"]:
                time.sleep(0.2)
                func()
            else:
                func(shiny_mode)
    # If host left or failure
    elif current_stage == 8:
        print("press esc")
        pyautogui.press("esc")
    # Game Over
    else:
        game_ended(shiny_mode)


def get_shiny_mode_from_input() -> bool:
    """
    Prompts the user interactively to determine whether to enable shiny mode.
    :return: True if shiny mode is enabled; False otherwise.
    """
    while True:
        user_input = input("Shiny Chess? (y/n): ").strip().lower()
        if user_input in {"y", "n"}:
            return user_input == "y"
        print("Invalid input. Please enter 'y' or 'n'.")


def main() -> None:
    """
    Main entry point for the program. Parses arguments and creates a lobby.
    :return: None
    """
    args = parse_arguments()

    # Determine shiny_mode based on command-line arguments
    if args.yes:
        shiny_mode = True
    elif args.no:
        shiny_mode = False
    else:
        shiny_mode = get_shiny_mode_from_input()

    logging.info("Macro ON")
    while True:
        create_lobby(shiny_mode)


# Main call
if __name__ == "__main__":
    main()
