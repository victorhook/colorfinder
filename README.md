# Colorfinder
This small script gets the color where the cursor is positioned on the screen and puts it as a hex-string in the clipboard.

## Setup
Clone the project and run
`pip install -r requirements.txt`

Then you're ready to go!
`python3 find_color.py`

You could also have a simple bash script like the following:
```
#!/bin/bash

VIRTUAL_ENV='PATH_TO_YOUR_ENV'
PATH="$VIRTUAL_ENV/bin:$PATH"
python3 'PATH_TO_THIS_DIR'/find_color.py
```

And then bind the script to a keybinding and voila, only 1 click is now required to find out the color of anything on the screen!


## Dependencies
The script uses the following libraries
- `pyscreenshot` - to take the screenshot at the cursor
- `opencv-python` - to get the color value of the image
- `pyautogui` - to get the cursor position
- `pyperclip` - to put the hex string in the clipboard