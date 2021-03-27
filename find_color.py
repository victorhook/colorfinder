import cv2
import os
import pyautogui
import pyscreenshot as ImageGrab
import pyperclip


SCREENSHOT_SIZE = 1

# Get cursor position
cursor = pyautogui.position()

# Take a super-tiny screenshot at cursor position
im = ImageGrab.grab(bbox=(cursor.x, cursor.y,
                          cursor.x+SCREENSHOT_SIZE,
                          cursor.y+SCREENSHOT_SIZE))

# Save the screenshot
IMG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fullscreen.png")
im.save(IMG_PATH)

# Read the image to get the pixel values
img = cv2.imread(IMG_PATH)[0][0]

# Turn the pixel values to a hex string
hexified = ''.join([hex(val).replace('0x', '').zfill(2) for val in img])
hexified = '#' + hexified

# Add the hex string to the clipboard
pyperclip.copy(hexified)
