from typing import Tuple, Callable, Any, Dict  # Used to create a tuple type hint
import pyautogui  # Used to move the cursor
import argparse  # Used to add --yes / --no argument for game-mode selection
import time


def is_on_screen(image, confidence=0.6) -> bool | None:
    """
    It takes a screenshot of the entire screen each couple moments and tries to find the given image
    :param image: The path of the image you want to find
    :param confidence: How much you want your image on screen to resemble your own image to be considered a match (0.1 - 1)
    :return: True or False
    """

    try:  # Tries to find the image if it can't, it throws an error
        if pyautogui.locateOnScreen(image, confidence=confidence) is not None:
            return True
    except pyautogui.ImageNotFoundException:
        return False  # Returns false (It didn't find)


def find_on_screen(image, confidence=0.7) -> None:
    """
    Based on is_on_screen() function. It loops until it finds the desired image
    :param image: "The path of the image you want to find"
    :param confidence: "How much you want your image on screen to resemble your own image to be considered a match (0.1 - 1)"
    :return: None
    """
    while True:
        time.sleep(1)
        if not is_on_screen(image, confidence=confidence):
            pass
        else:
            break


def find_and_click(image, confidence=0.7, times=1) -> bool:
    """
    Finds an image and clicks in the middle of it.
    :param image: "The path of the image you want to find"
    :param confidence: "How much you want your image on screen to resemble your own image to be considered a match (0.1 - 1)"
    :param times: How many times you want to click.
    :return: A bool
    """
    tries = 0
    while tries < 20:
        try:
            x, y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            for i in range(times):
                pyautogui.moveTo(x, y)
                pyautogui.click()
            return True
        except pyautogui.ImageNotFoundException:
            pass
        tries += 1
        # print(tries)
    return False


def clear_and_type(name) -> None:
    """
    Clears a text box and types new text.
    :param name: Text to type.
    :return: None
    """
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    pyautogui.press("backspace")
    pyautogui.typewrite(name)


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for Shiny Chess mode.
    :returns: Parsed arguments with --yes or --no flags.
    """
    parser = argparse.ArgumentParser(description="Chess game settings")
    parser.add_argument(
        "-y", "--yes", action="store_true", help="Automatically set Shiny Chess to yes"
    )
    parser.add_argument(
        "-n", "--no", action="store_true", help="Automatically set Shiny Chess to no"
    )
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
        print(
            f"Time it took to execute {str(func).split(' ')[1]}: {(end - start):.2f} seconds"
        )

    return wrapper
