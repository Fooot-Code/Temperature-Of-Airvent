
import cv2
import pytesseract
from PIL import ImageGrab
import pygetwindow as gw
import numpy as np

# Find the window by title
window_title = "DroidCam Client"  # Change this to the title of your window
window = gw.getWindowsWithTitle(window_title)[0]
print(window)
# Get the window's bounding box


while True:
    # Capture the screen within the bounding box
    bbox = (window.left, window.top + 73, window.right, window.bottom - 154)
    screenshot = ImageGrab.grab(bbox=bbox)
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to do OCR on the frame
    numbers = pytesseract.image_to_string(gray, config='--psm 6 digits')

    # Display the resulting frame
    cv2.putText(frame, numbers, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close windows
cv2.destroyAllWindows()
