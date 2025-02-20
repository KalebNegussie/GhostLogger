#  GhostLogger-Keylogger Project

## Overview
This is a simple keylogger implemented in Python using the `pynput` library to capture keystrokes and log them to a file. The script also tracks the active window title and logs it whenever the user switches between applications.

## Features
- Logs all keystrokes typed by the user.
- Detects and logs changes in the active window.
- Replaces special keys like `space`, `enter`, and `backspace` with appropriate symbols.
- Outputs captured keystrokes to a log file (`log1.txt`).

## Prerequisites
Ensure you have Python installed on your system. You will also need the following dependencies:

```sh
pip install pynput pywin32
```

## Installation & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/KalebNegussie/keylogger-project.git
   cd keylogger-project
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python keylogger.py
   ```

## How It Works
- The script uses `pynput.keyboard.Listener` to listen for key presses.
- It retrieves the currently active window using the `win32gui` module.
- If the user switches to a new window, the script logs the new window title before continuing to capture keystrokes.
- Keystrokes are logged to `log1.txt` in real-time.

## Disclaimer
This project is intended for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission before deploying this script.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
[Your Name]

## Contributing
Feel free to fork this repository and submit pull requests with improvements or feature additions.
