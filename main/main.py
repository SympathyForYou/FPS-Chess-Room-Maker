import pyautogui

from functions import is_on_screen, find_and_click, clear_and_type, parse_arguments, measure_time  # Explicit imports
from config import IMAGE_PATHS, DESCRIPTION, NORMAL_ROOM_NAME, SHINY_ROOM_NAME # Config
import logging  # Used to log print messages


# The main flow of the program is here
@measure_time
def create_lobby(shiny_mode: bool) -> None:
    """
    Creates a game lobby based on the shiny_mode flag.

    :param shiny_mode: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
    :return: None
    """
    # Find main menu
    while True:
        if is_on_screen(IMAGE_PATHS['main'], 0.5):
            break
        elif is_on_screen(IMAGE_PATHS['left'], 0.7):
            logging.info("Player left")
            pyautogui.hotkey('esc')
            find_and_click(IMAGE_PATHS['menu'], confidence=0.7, times=2)
            create_lobby(shiny_mode)

    # Click on the Host Button (Three times to un-focus from konsole)
    find_and_click(IMAGE_PATHS['host'])
    logging.info("Clicked Host Button")


    # Set room name based on game-mode
    room_name = SHINY_ROOM_NAME if shiny_mode else NORMAL_ROOM_NAME
    find_and_click(IMAGE_PATHS['room_name'])
    clear_and_type(room_name)
    logging.info(f"Set room name to: {room_name}")


    # Set description
    find_and_click(IMAGE_PATHS['description'])
    clear_and_type(DESCRIPTION)
    logging.info(f"Set description to: {DESCRIPTION}")

    # Set game-mode
    if shiny_mode:
        find_and_click(IMAGE_PATHS['shiny'], confidence=0.95)
        logging.info("Activated Shiny Game Mode")

    # Creates a room
    find_and_click(IMAGE_PATHS['create_room'])
    logging.info("Lobby Launched")

    # Close invites
    logging.info("Invites Found")
    find_and_click(IMAGE_PATHS['close'])
    logging.info("Closed invites window")

def get_shiny_mode_from_input() -> bool:
    """
    Prompts the user interactively to determine whether to enable shiny mode.

    :return: True if shiny mode is enabled; False otherwise.
    """
    while True:
        user_input = input("Shiny Chess? (y/n): ").strip().lower()
        if user_input in {'y', 'n'}:
            return user_input == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")


def main() -> None:
    """
    Main entry point for the program. Parses arguments and creates a lobby.
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
if __name__ == '__main__':
    main()