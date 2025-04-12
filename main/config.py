from os import path  # Used to find images folder regardless of where the script is run from
import logging  # Used to log each action of the program
# ROOM_CONFIG
DESCRIPTION: str = "Bafoon"  # The room description
SHINY_ROOM_NAME: str = "Shiny Pokemon!"  # Room name for shiny game
NORMAL_ROOM_NAME: str = "aim-bot"  # Room name for normal game
SHAKESPEARE_POEM: str = (
    """O, fairest of days, how dost thou shine so bright? ... (truncated for brevity)"""  # An o'l good poem
)

# Gets the absolute path of the images 
absolute_images_path = str(path.abspath(path.join(path.dirname(__file__), path.pardir, 'images')))

# Saved Images
IMAGE_PATHS: dict[str, str] = {
    'main'        : absolute_images_path + '/' + 'main_menu'          + '.png',
    'create'      : absolute_images_path + '/' + 'create_menu'        + '.png',
    'close'       : absolute_images_path + '/' + 'close_button'       + '.png',
    'waiting'     : absolute_images_path + '/' + 'waiting_for_player' + '.png',
    'left'        : absolute_images_path + '/' + 'player_left'        + '.png',
    'menu'        : absolute_images_path + '/' + 'main_menu_button'   + '.png',
    'host'        : absolute_images_path + '/' + 'host'               + '.png',
    'room_name'   : absolute_images_path + '/' + 'room_name'          + '.png',
    'description' : absolute_images_path + '/' + 'description'        + '.png',
    'shiny'       : absolute_images_path + '/' + 'shiny'              + '.png',
    'create_room' : absolute_images_path + '/' + 'create_room_button' + '.png',
    'white'       : absolute_images_path + '/' + 'white_wins'         + '.png',
    'black'       : absolute_images_path + '/' + 'black_wins'         + '.png',
    'invite'      : absolute_images_path + '/' + 'invite_button'      + '.png',
    'host_left'   : absolute_images_path + '/' + 'host_left'          + '.png',
    'failure'     : absolute_images_path + '/' + 'connection_failure' + '.png'
}

# Basic Config Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
