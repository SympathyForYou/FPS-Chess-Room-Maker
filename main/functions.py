from logging import info  # (Built-in) Used to print classy messages
from time import time     # (Built-in) Used for the measure_time decorator
from sys import argv      # (Built-in) Used to add --yes / --no cmd arguments
import pyautogui          # (Third-Party) Used for automation (clicking, typing)


class RoomSetup:  # An actual class
    @staticmethod
    def _detect_stage() -> None:
        from main import detect_stage
        detect_stage()


    @staticmethod
    def _click_and_log(img_path: str, log_message: str, confidence: float=0.7, clicks: int=1) -> None:
        if ImageRecognition.find_and_click(img_path, confidence=confidence, clicks=clicks):
            info(log_message)

        RoomSetup._detect_stage()
    

    @staticmethod
    def find_host_button(img_path, game_mode_flag: bool) -> None:
        """ Clicks on the host button in main menu that leads to the create room menu."""

        RoomSetup._click_and_log(img_path, log_message="Clicked Host Button")


    @staticmethod
    def set_room_name(img_path, game_mode_flag: bool) -> None:
        """Sets room's name based on the game_mode."""
        from config import NORMAL_ROOM_NAME, SHINY_ROOM_NAME
        ROOM_NAME = SHINY_ROOM_NAME if game_mode_flag else NORMAL_ROOM_NAME
        if ImageRecognition.find_and_click(img_path):
            info(f"Set room namet to: {ROOM_NAME}")
            Backend.clear_and_type(ROOM_NAME)


    @staticmethod
    def set_description(img_path: str, game_mode_flag: bool) -> None:
        """Sets room's description."""
        from config import DESCRIPTION
        if ImageRecognition.find_and_click(img_path):
            info(f"Set description to: {DESCRIPTION}")
            Backend.clear_and_type(DESCRIPTION)
    

    @staticmethod
    def set_game_mode(img_path: str, game_mode_flag: bool) -> None:
        """Clicks on the shiny game-mode checkbox."""
        if game_mode_flag:
            RoomSetup._click_and_log(img_path, log_message="Activated Shiny Game Mode", confidence=0.95,)
        
        RoomSetup._detect_stage()


    @staticmethod
    def create_room(img_path: str, game_mode_flag: bool) -> None:
        """Clicks on the launch room button."""
        RoomSetup._click_and_log(img_path, log_message="Lobby Launched")


    @staticmethod
    def close_invites(img_path: str, game_mode_flag: bool) -> None:
        """Clicks on the close friends invite window."""
        RoomSetup._click_and_log(img_path, log_message="Closed invites window")
    

    @staticmethod
    def game_ended(img_path: str, game_mode_flag: bool) -> None:
        """Whenever someone wins / player leaves it quits to main menu."""
        pyautogui.hotkey("esc")
        RoomSetup._click_and_log(img_path, log_message="Restart game.", clicks=2)


class ImageRecognition:  # This is more of a folder than a class
        """
        This class contains functions related to finding images on the screen.
        """

        @staticmethod
        def is_on_screen(image: str, confidence: float=0.6) -> bool:
            """
            Takes a screenshot of your entire screen each couple moments and attempts to find the given image.
            :param image: The path of the image you want to find.
            :param confidence: How much you want you want your image to match before it's a result -- From 0.1 to 1 -- I recommand between 0.6 and 0.8.
            """
            try:  # Attempts to find the image if it can't, it throws an error
                if pyautogui.locateOnScreen(image, confidence=confidence):
                    return True
            except pyautogui.ImageNotFoundException:
                return False  # Returns false (It didn't find)


        @staticmethod
        def find_and_click(image: str, confidence: float=0.7, clicks: int=1) -> bool:
            """
            Attempts to find your image and clicks in the middle of it.
            :param image: The path of the image you want to find.
            :param confidence: How much you want you want your image to match before it's a result -- From 0.1 to 1 -- I recommand between 0.6 and 0.8.
            :param clicks: How many times you want to click.
            """
            attempts: int = 0

            while attempts < 35:  # KEEP AT 35 or it skips next stage after find_host_button (set_room_name)
                try:              # This has to due to the fact that a bad looping cycle might detect a later stage earlier then it should
                    # Get coordinates
                    x, y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
                    # Click on the image
                    for i in range(clicks):
                        pyautogui.moveTo(x, y)
                        pyautogui.click()
                    return True
                except pyautogui.ImageNotFoundException:
                    attempts += 1
            
            return False


class Backend:  # This is more of a folder than a class
    """
    Miscellaneous functions related to:
    - measuring function time,
    - getting user input,
    - and typing,
    """

    @staticmethod
    def measure_time(func):
        """
        Decorator to measure a function's execution time.
        """
        def wrapper(*args, **kwargs) -> None:
            # Start time
            start: float = time()
            result: any = func(*args, **kwargs)
            # End time
            end: float = time()
            # Printing the result
            print("-" * 20)
            print(f"The time your game took: {(end - start):.2f} seconds to complete")
            print("-" * 20)
            return result
        return wrapper


    @staticmethod
    def user_input() -> bool:
        """
        Takes user input via command line arguments or interactively.
        """
        # Determine shiny_mode_flag based on the first command-line argument
        USER_ARGUMENT: list = argv if len(argv) > 0 else ""
        if len(USER_ARGUMENT) > 1 and USER_ARGUMENT[1] in {'--yes', '-y', '--no', '-n'}:
            return USER_ARGUMENT[1] in {'--yes', '-y'}
        
        # Determine shiny_mode_flag based on the interactive prompt
        while True:
            info("Do you want to play Shiny Chess? (y/n)")
            USER_INPUT: str = input(">>> ").strip().lower()
            if USER_INPUT in {"y", "n"}:
                return USER_INPUT == "y"
            
            info("Invalid input. Please enter 'y' or 'n'.")


    @staticmethod
    def clear_and_type(sentence: str) -> None:
        """
        Takes control of your keyboard and clears a text box and types new text.
        :param sentence: Text to type.
        """
        # Select all text
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        # Delete text
        pyautogui.press("backspace")
        # Type new text
        pyautogui.typewrite(sentence)
