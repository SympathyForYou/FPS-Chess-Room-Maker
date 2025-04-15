# FPS Chess Macro

![fps_chess](https://github.com/user-attachments/assets/fed8462f-7f7b-402b-9ac5-954d9c245de5)

## Overview
This macro takes control of your mouse and keyboard to automate the process of room creating insde FPS Chess.

Based on [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) Library and [Open-CV](https://opencv.org).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Troubleshooting](#troubleshooting)
- [How to Change Description & Room Name](#how-to-change-description--room-name)
- [Contributing](#contributing)
- [License](#license)


## Features

- Automatic room creation
- Custom room name and description
- Sleek game mode selection
- Automatic leave on game end

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/chess_macro.git
   ```
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script:
```
python main.py
```

## Options

- Interactive mode: `python main.py`
- Enable shiny game mode: `python main.py -y`
- Disable shiny game mode: `python main.py -n`

## Troubleshooting

- Ensure your game window is visible and not minimized.
- Check that your screen resolution matches the script's expectations. (1920 x 1080)

## How to Change Description & Room Name

1. Open [config.py](main/config.py) found in main using a text editor.
2. Make changes.
3. Save Changes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License -- See the [LICENSE](LICENSE) file for details.
