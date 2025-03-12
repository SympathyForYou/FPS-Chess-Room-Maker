import time

from config import BUTTON_POSITIONS # Used to connect dictionary to function
from typing import Tuple, Callable, Any, Dict  # Used to create a tuple type hint
import pyautogui  # Used to move the cursor
import argparse  # Used to add --yes / --no argument for game-mode selection


def move_and_click(position: Tuple[int, int]) -> None:
    """
    Moves the mouse to the specified coordinates and clicks.

    :param position: (x, y) coordinates on the screen.
    :return: None
    """
    pyautogui.moveTo(position)
    pyautogui.click()


def clear_and_type(key: str, count: int, name: str) -> None:
    """
      Clears a text box and types new text.

      :param key: Text box key from BUTTON_POSITIONS.
      :param count: Number of backspace presses.
      :param name: Text to type.
      """
    move_and_click(BUTTON_POSITIONS[key])
    pyautogui.press('backspace', presses=count)
    pyautogui.typewrite(name)


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for Shiny Chess mode.

    Returns:
        Parsed arguments with --yes or --no flags.
    """
    parser = argparse.ArgumentParser(description="Chess game settings")
    parser.add_argument('-y', '--yes', action='store_true', help="Automatically set Shiny Chess to yes")
    parser.add_argument('-n', '--no', action='store_true', help="Automatically set Shiny Chess to no")
    return parser.parse_args()


def measure_time(func) -> Callable[[tuple[Any, ...], dict[str, Any]], None]:
    """
    Decorator to measure a function's execution time.

    :param func: Function to measure.
    """
    def wrapper(*args, **kwargs) -> None:
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time it took to execute {str(func).split(' ')[1]}: {(end - start):.2f} seconds")
    return wrapper