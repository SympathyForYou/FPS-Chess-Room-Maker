from config import IMAGE_PATHS, SHINY_ROOM_NAME, NORMAL_ROOM_NAME, DESCRIPTION
import pyautogui  # (Third-Party) Used for automation (clicking, typing)
import logging    # (Built-in) Used to print classy messages
import time       # (Built-in) Used for the measure_time decorator
import sys        # (Built-in) Used to add --yes / --no cmd arguments


class ImageRecognition:  # This is more of a folder than a class
    """
    This class contains functions related to finding images on the screen.
    """

    def is_on_screen(image: str, confidence: float=0.6) -> bool:
        """
        Takes a screenshot of your entire screen each couple moments and attempts to find the given image.
        :param image: The path of the image you want to find.
        :param confidence: How much you want you want your image to match before it's a result -- From 0.1 to 1 -- I recommand between 0.6 and 0.8.
        :return: bool
        """
        try:  # Attempts to find the image if it can't, it throws an error
            if pyautogui.locateOnScreen(image, confidence=confidence):
                return True
        except pyautogui.ImageNotFoundException:
            return False  # Returns false (It didn't find)


    def find_and_click(image: str, confidence: float=0.7, clicks: int=1) -> bool:
        """
        Attempts to find your image and clicks in the middle of it.
        :param image: The path of the image you want to find.
        :param confidence: How much you want you want your image to match before it's a result -- From 0.1 to 1 -- I recommand between 0.6 and 0.8.
        :param clicks: How many times you want to click.
        :return: bool
        """
        attempts: int = 0

        while attempts < 35:  # KEEP AT 35 or it skips next stage after find_host_button
            try:
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
    - parsing arguments, 
    - measuring function time,
    - getting user input 
    - and typing.
    """

    def measure_time(func):
        """
        Decorator to measure a function's execution time.
        :param func: Function to measure.
        :return: Wrapper function that prints the execution time.
        """
        def wrapper(*args, **kwargs) -> None:
            # Start time
            start: float = time.time()
            result: any = func(*args, **kwargs)
            # End time
            end: float = time.time()
            # Printing the result
            print("-" * 20)
            print(f"The time your game took: {(end - start):.2f} seconds to complete")
            print("-" * 20)
            return result
        return wrapper


    def user_input() -> bool:
        """
        Takes user input via command line arguments or interactively.
        :return: bool
        """
        # Determine shiny_mode_flag based on the first command-line argument
        USER_ARGUMENT: list = sys.argv if len(sys.argv) > 0 else ""
        if len(USER_ARGUMENT) > 1 and USER_ARGUMENT[1] in {'--yes', '-y', '--no', '-n'}:
            return USER_ARGUMENT[1] in {'--yes', '-y'}
        
        # Determine shiny_mode_flag based on the interactive prompt
        while True:
            logging.info("Do you want to play Shiny Chess? (y/n)")
            USER_INPUT: str = input(">>> ").strip().lower()
            if USER_INPUT in {"y", "n"}:
                return USER_INPUT == "y"
            
            logging.info("Invalid input. Please enter 'y' or 'n'.")


    def clear_and_type(sentence: str) -> None:
        """
        Takes control of your keyboard and clears a text box and types new text.
        :param sentence: Text to type.
        :return: None
        """
        # Select all text
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        # Delete text
        pyautogui.press("backspace")
        # Type new text
        pyautogui.typewrite(sentence)


class Stage:  # This is more of a folder than a class
    """
    This class contains all stage functions the program must run to create a chess room.
    """
    
    def find_host_button(game_mode_flag: bool) -> None:
        """ 
        Clicks on the host button in main menu that leads to the create room menu.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        # Click on the Host Button
        if ImageRecognition.find_and_click(IMAGE_PATHS["host_text_in_main_menu"]):
            logging.info("Clicked Host Button")
        
        detect_stage()


    def set_room_name(game_mode_flag: bool) -> None:
        """
        Sets room's name based on the game_mode.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        # Set room name
        room_name = SHINY_ROOM_NAME if game_mode_flag else NORMAL_ROOM_NAME
        if ImageRecognition.find_and_click(IMAGE_PATHS["room_name_text_box"]):
            logging.info(f"Set room name to: {room_name}")
            Backend.clear_and_type(room_name)
        
        detect_stage()


    def set_description(game_mode_flag: bool) -> None:
        """
        Sets room's description.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        if ImageRecognition.find_and_click(IMAGE_PATHS["description_text_box"]):
            Backend.clear_and_type(DESCRIPTION)
            logging.info(f"Set description to: {DESCRIPTION}")
        
        detect_stage()


    def set_game_mode(game_mode_flag: bool) -> None:
        """
        Clicks on the shiny game-mode checkbox.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        # Set game-mode
        if game_mode_flag:
            ImageRecognition.find_and_click(IMAGE_PATHS["shiny_game_mode_checkbox"], confidence=0.95)
            logging.info("Activated Shiny Game Mode")
            
        detect_stage()


    def create_room(game_mode_flag: bool) -> None:
        """
        Clicks on the launch room button.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        # Creates a room
        if ImageRecognition.find_and_click(IMAGE_PATHS["create_room_button"]):
            logging.info("Lobby Launched")
        
        detect_stage()


    def close_invites(game_mode_flag: bool) -> None:
        """
        Clicks on the close friends invite window.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        # Close invites
        if ImageRecognition.find_and_click(IMAGE_PATHS["close_invites_button"]):
            logging.info("Closed invites window")
        
        detect_stage()


    def game_ended(game_mode_flag: bool) -> None:
        """
        Whenever someone wins / player leaves it quits to main menu.
        :param game_mode_flag: If True, sets up a shiny chess game. Otherwise, sets up a normal game.
        :return: None
        """
        from main import detect_stage
        pyautogui.hotkey("esc")
        if ImageRecognition.find_and_click(IMAGE_PATHS["return_to_main_menu_button"], clicks=2):
            logging.info("Restart game.")
        
        detect_stage()