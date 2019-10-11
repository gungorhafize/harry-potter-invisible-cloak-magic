import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Red color
    low_red = np.array([0, 0, 0])
    high_red = np.array([2, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    # Blue color
    low_blue = np.array([84, 0, 0])
    high_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    low_green = np.array([36, 0, 0])
    high_green = np.array([70, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    final_frame = cv2.hconcat((frame, blue, green, red, result))
    cv2.imshow('frame', final_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break