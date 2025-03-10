from functions import *  # Custom made functions
import logging
import time

shake: str = '''O, fairest of days, how dost thou shine so bright? A radiant sun doth cast its golden light, Upon the verdant fields, where wildflowers sway, And gentle breezes whisper secrets of the day. The trees, like sentinels of earth and sky, Stand watchful, their leaves rustling with a sigh, As if they too could feel the weight of time, And all the tales that in their boughs do climb. The rivers flow, a winding path of blue, Reflecting sunbeams, as the waters anew, Do carve their course, a testament to might, And in their depths, a mirrored sky takes flight. O, mortal hearts, how fleeting are thy joys? Like autumn leaves, they wither, fade, and lose Their vibrant hue, yet in their fall, they find A beauty that doth touch the heart and mind. For in the cycle of life, we find our fate, A dance of birth, of growth, of love, of hate, And in the end, a peaceful, silent sleep, Where dreams and memories our souls do keep. Thus let us cherish every moment we share, And in the beauty of the world, find love and care, For though our time is short, our impact grand, We leave behind a legacy, a lasting stand. So let the sun shine bright, the stars appear, And in their light, may our true selves be clear, For in the end, it is not years we live, But life in those years, that truly we give. And when the final curtain falls, and night Descends upon our mortal, fleeting light, May our hearts be filled with peace, our souls with cheer, And in the silence, may our love be near. For love, like time, is infinite and true, A bond that ties us all, in all we do, A flame that burns, a beacon in the night, Guiding us forward, through life's plodding flight. Thus let us hold on to love, to hope, to light, And in their warmth, may our spirits take flight, For in the darkness, there is still a way, To find the beauty, come what may. And so we journey on, through joy and strife, Through every moment, a piece of life, A tapestry woven, rich and bold and bright, A story told in threads of love and light. For in the end, it is not what we have, But what we give, that truly makes us brave, Not wealth, nor power, nor fame, nor might, But love, kindness, and the light we hold tight. Thus let us shine, like stars in the midnight sky, Reflecting love, and spreading it on by, For in its radiance, we find our peaceful nest, A home where hearts can rest, and be at best. And when the world is dark, and fears assail, Let love be our shield, our guiding gale, That lifts us up, and carries us through the night, To a dawn where hope and joy take flight. For love is the answer, the key to all, The bond that heals, the light that stands tall, In every heart, a spark doth glow, A flame of love, that only grows. So let us tend this fire, and let it shine, A beacon in the darkness, a love divine, That guides us home, through every stormy night, To a place of peace, where love is the light.'''

# Top Variables
description: str = "Bafoon"  # The room description
shiny_room_name: str = "Shiny Pokemon!"  # Room name for shiny game
normal_room: str = "aim-bot"  # Room name for normal game


# Coordinates of interest
button_positions = {
    "Host Button": (1185, 812),
    "Shiny Pieces Button": (1222, 592),
    "Room Name Text Box": (1282, 318),
    "Description Text Box": (1184, 659),
    "Create Room Button": (715, 782),
    "Close Invite Button": (1509, 855)
}


# Basic Config Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# The main flow of the program is here
def main() -> None:
    # Click on the Host Button (Three times to un-focus from konsole)
    for _ in range(3):
        move_and_click(button_positions["Host Button"])
    logging.info("Created lobby")
    time.sleep(3.4)

    if shiny_chess_bool:
        # Activates Shiny Pieces
        move_and_click(button_positions["Shiny Pieces Button"])
        logging.info("Selected Shiny Game-mode")
        # Selects the text box clears and types the Room Name
        clear_and_type("Room Name Text Box", 18, shiny_room_name)
        logging.info(f"Typed room name: {shiny_room_name}")
    else:
        # Selects the box clears and types the Room Name
        clear_and_type("Room Name Text Box", 18, normal_room)
        logging.info(f"Typed room name: {normal_room}")

    # Opens text box clears and types Description
    clear_and_tye("Description Text Box", 14, description)
    logging.info(f"Typed description: {description}")
    # Creates a room
    move_and_click(button_positions["Create Room Button"])
    logging.info("Lobby Launched")
    # Close Invites
    time.sleep(1.9)
    move_and_click(button_positions["Close Invite Button"])
    logging.info("Closed invites")


# Main call
if __name__ == "__main__":
    args = parse_arguments()

    # Determine shiny_chess_bool based on command-line arguments
    if args.yes:
        shiny_chess_bool: bool = True
    elif args.no:
        shiny_chess_bool: bool = False
    else:
        # Interactive input if neither -y nor -n is provided
        while True:
            shiny_chess = input("Shiny Chess? (y/n): ").strip().lower()
            if len(shiny_chess) == 1 and shiny_chess in {'y', 'n'}:
                break
            print("Invalid input. Please enter 'y' or 'n'.")
        shiny_chess_bool: bool = (shiny_chess == 'y')

    # Call the main function with the determined shiny_chess_bool value
    main()