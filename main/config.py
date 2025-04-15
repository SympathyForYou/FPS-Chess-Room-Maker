from os import path  # (Built-in) Used to find images folder regardless of where the script is run from
import logging       # (Built-in) Used to print classy messages 

# ROOM_CONFIG
DESCRIPTION: str = "Bafoon"              # The room description
SHINY_ROOM_NAME: str = "Shiny Pokemon!"  # Room name for shiny game
NORMAL_ROOM_NAME: str = "aim-bot"        # Room name for normal game
SHAKESPEARE_POEM: str = """O, fairest of days, how dost thou shine so bright? ... (truncated for brevity)"""  # An o'l good poem

# Gets the absolute path of the images 
absolute_images_path = str(path.abspath(path.join(path.dirname(__file__), path.pardir, 'images')))

# Saved Images
IMAGE_PATHS: dict[str, str] = {  # Ordered by use
    'host_text_in_main_menu'     : absolute_images_path + '/' + 'host_text_in_main_menu'     + '.png',
    'room_name_text_box'         : absolute_images_path + '/' + 'default_room_name_text'     + '.png',
    'description_text_box'       : absolute_images_path + '/' + 'default_description_text'   + '.png',
    'shiny_game_mode_checkbox'   : absolute_images_path + '/' + 'shiny_checkbox'             + '.png',
    'create_room_button'         : absolute_images_path + '/' + 'create_room_button'         + '.png',
    'close_invites_button'       : absolute_images_path + '/' + 'close_button'               + '.png',
    'player_left'                : absolute_images_path + '/' + 'player_left'                + '.png',
    'white_wins'                 : absolute_images_path + '/' + 'white_wins'                 + '.png',
    'black_wins'                 : absolute_images_path + '/' + 'black_wins'                 + '.png',
    'pending_connection_failure' : absolute_images_path + '/' + 'pending_connection_failure' + '.png',
    'host_left'                  : absolute_images_path + '/' + 'host_left'                  + '.png',
    'return_to_main_menu_button' : absolute_images_path + '/' + 'main_menu_button'           + '.png',
}

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)