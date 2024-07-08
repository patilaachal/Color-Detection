import cv2
import numpy as np

# Function to get RGB color from a pixel
def get_color_name(R, G, B):
    if R > 200 and G < 50 and B < 50:
        return "Red"
    elif R < 50 and G > 200 and B < 50:
        return "Green"
    elif R < 50 and G < 50 and B > 200:
        return "Blue"
    else:
        return "Unknown"

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the RGB color of the pixel
        b, g, r = img[y, x]
        print(f"R={r}, G={g}, B={b}")
        print("Color:", get_color_name(r, g, b))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"{r},{g},{b}", (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

# Load an image
img = cv2.imread(r"C:\Users\dhand\OneDrive\Desktop\img.jpg")  # Use raw string literal or forward slashes

# Display the image
cv2.imshow('image', img)

# Set mouse callback function for window
cv2.setMouseCallback('image', click_event)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()