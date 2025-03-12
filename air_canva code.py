# Import necessary packages.
import cv2
import numpy as np

# Define various colors
colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]

# Select a default color
color = colors[0]

# Minimum allowed area for the contour
min_area = 800  # Adjusted for sharper tip detection

# Create videocapture object
cap = cv2.VideoCapture(0)

width = int(cap.get(3))
height = int(cap.get(4))

# Create a blank canvas
canvas = np.zeros((height, width, 3), np.uint8)

# Color range for detecting blue color (adjust as needed)
lower_bound = np.array([100, 150, 50])  # Lower bound for blue
upper_bound = np.array([140, 255, 255])  # Upper bound for blue

# Define a 10x10 kernel
kernel = np.ones((10, 10), np.uint8)

previous_center_point = 0

while True:
    # Read each frame from webcam
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Convert the frame BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a binary segmented mask of blue color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Add dilation to increase segmented area
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Find all the contours of the segmented mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Get the biggest contour from all detected contours
        cmax = max(contours, key=cv2.contourArea)

        # Find the area of the contour
        area = cv2.contourArea(cmax)

        if area > min_area:
            # Find center point of the contour
            M = cv2.moments(cmax)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Drawing a circle at the tip of the pen
                cv2.circle(frame, (cX, cY), 8, (0, 0, 255), 2)

                # If it's the first detection, check for color selection
                if previous_center_point == 0:
                    if cY < 65:
                        if 20 < cX < 120:
                            canvas = np.zeros((height, width, 3), np.uint8)
                        elif 140 < cX < 220:
                            color = colors[0]
                        elif 240 < cX < 320:
                            color = colors[1]
                        elif 340 < cX < 420:
                            color = colors[2]
                        elif 440 < cX < 520:
                            color = colors[3]
                        elif 540 < cX < 620:
                            color = colors[4]

                # Draw line between previous and current points
                if previous_center_point != 0:
                    cv2.line(canvas, previous_center_point, (cX, cY), color, 2)

                previous_center_point = (cX, cY)
            else:
                previous_center_point = 0

    # Merging canvas with frame
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, canvas_binary = cv2.threshold(canvas_gray, 20, 255, cv2.THRESH_BINARY_INV)
    canvas_binary = cv2.cvtColor(canvas_binary, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, canvas_binary)
    frame = cv2.bitwise_or(frame, canvas)

    # Drawing color selection buttons
    cv2.rectangle(frame, (20, 1), (120, 65), (122, 122, 122), -1)
    cv2.rectangle(frame, (140, 1), (220, 65), colors[0], -1)
    cv2.rectangle(frame, (240, 1), (320, 65), colors[1], -1)
    cv2.rectangle(frame, (340, 1), (420, 65), colors[2], -1)
    cv2.rectangle(frame, (440, 1), (520, 65), colors[3], -1)
    cv2.rectangle(frame, (540, 1), (620, 65), colors[4], -1)
    cv2.putText(frame, "CLEAR", (30, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, "BLUE", (155, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, "VIOLET", (255, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, "GREEN", (355, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, "RED", (465, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, "YELLOW", (555, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    # Show the frame
    cv2.imshow("Frame", frame)
    cv2.imshow("Canvas", canvas)

    # Exit on 'q' press
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
