from functions import move_and_click, clear_and_type, parse_arguments, measure_time  # Explicit imports
from config import BUTTON_POSITIONS, DESCRIPTION, NORMAL_ROOM_NAME, SHINY_ROOM_NAME # Config
import logging  # Used to log print messages
import time  # Used to make the program wait


# The main flow of the program is here
@measure_time
def create_lobby(shiny_mode: bool) -> None:
    """
    Creates a game lobby based on the shiny_mode flag.

    :param shiny_mode: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
    :return: None
    """
    # Click on the Host Button (Three times to un-focus from konsole)
    for _ in range(3):
        move_and_click(BUTTON_POSITIONS["host_button"])
    logging.info("Clicked Host Button to create a lobby")
    time.sleep(3.4)


    # Set room name based on game-mode
    room_name = SHINY_ROOM_NAME if shiny_mode else NORMAL_ROOM_NAME
    clear_and_type("room_name_text_box", 18, room_name)
    logging.info(f"Set room name to: {room_name}")


    # Set description
    move_and_click(BUTTON_POSITIONS["description_text_box"])
    clear_and_type("description_text_box", 14, DESCRIPTION)
    logging.info(f"Typed description: {DESCRIPTION}")

    # Set game-mode
    if shiny_mode:
        move_and_click(BUTTON_POSITIONS["shiny_pieces_button"])
        logging.info("Activated Shiny Game Mode")

    # Creates a room
    move_and_click(BUTTON_POSITIONS["create_room_button"])
    logging.info("Lobby Launched")

    # Close Invites
    time.sleep(1.9)
    move_and_click(BUTTON_POSITIONS["close_invite_button"])
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

    create_lobby(shiny_mode)

# Main call
if __name__ == "__main__":
    main()