# Imports
from typing import Tuple  # Used to create a tuple type hint
from main import button_positions  # Used to connect dictionary to function
import pyautogui  # Used to move the cursor
import argparse  # Used to add --yes / --no argument for game-mode selection


def move_and_click(position: Tuple[int, int]) -> None:
    """
    Moves the mouse to the specified coordinates and performs a single click.

    This function uses the pyautogui library to move the mouse pointer to the given screen coordinates
    and simulate a single mouse click.

    Parameters:
        position (tuple[int, int]): A tuple containing two integers representing the (x, y) coordinates
                                    on the screen. For example, (0, 0) represents the top-left corner.

    :return: None
    """

    pyautogui.moveTo(position)
    pyautogui.click()


def clear_and_type(key: str, count: int, name: str) -> None:
    """
    Clears a text box and types new text using pyautogui.

    This function automates the process of interacting with a text box. It clicks on the specified text box, deletes
    a specified number of characters using backspace, and then types the provided text. The pyautogui library is used
    to perform these actions.

    Parameters:
        key (str): The key used to retrieve the coordinates of the text box from a dictionary.
        count (int): The number of times to press backspace to delete characters from the text box.
        name (str): The new text to type into the text box.

    :return: None
    """

    move_and_click(button_positions[key])
    pyautogui.press('backspace', presses=count)
    pyautogui.typewrite(name)


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments to determine user preferences for launching the chess game.

    This function uses the argparse library to read and interpret command-line arguments provided by the user.
    It allows the user to specify whether Shiny Chess mode should be enabled (`--yes`, `-y`) or disabled
    (`--no`, `-n`).

    Returns:
        argparse.Namespace: An object containing the parsed arguments as attributes. For example,
                            if `--yes` is passed, the returned object will have `yes=True` and `no=False`.
    """

    parser = argparse.ArgumentParser(description="Chess game settings")
    parser.add_argument('-y', '--yes', action='store_true', help="Automatically set Shiny Chess to yes")
    parser.add_argument('-n', '--no', action='store_true', help="Automatically set Shiny Chess to no")
    return parser.parse_args()
