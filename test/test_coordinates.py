# Imports
import pyautogui
import time

# Used to store last coordinates
last_coordinates: tuple[int, int] = (0, 0)

# Prints the coordinates of the mouse once then prints again if they change
while True:
    coordinates: tuple[int, int] = pyautogui.position()
    if coordinates == last_coordinates:
        pass
    else:
        print(coordinates)
    last_coordinates = coordinates
    time.sleep(1)