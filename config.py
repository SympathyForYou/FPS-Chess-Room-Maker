import logging

# ROOM_CONFIG
DESCRIPTION: str = "Bafoon"  # The room description
SHINY_ROOM_NAME: str = "Shiny Pokemon!"  # Room name for shiny game
NORMAL_ROOM_NAME: str = "aim-bot"  # Room name for normal game
SHAKESPEARE_POEM: str = '''O, fairest of days, how dost thou shine so bright? ... (truncated for brevity)'''  # An o'l good poem


# Coordinates of interest
BUTTON_POSITIONS = {
    "host_button": (1185, 812),
    "shiny_pieces_button": (1222, 592),
    "room_name_text_box": (1282, 318),
    "description_text_box": (1184, 659),
    "create_room_button": (715, 782),
    "close_invite_button": (1509, 855)
}


# Basic Config Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)