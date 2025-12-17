import cv2
import numpy as np
from math import hypot
import screen_brightness_control as sbc

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

# ==============================
# VOLUME SETUP (Pycaw - Python 3.13 compatible)
# ==============================
devices = AudioUtilities.GetSpeakers()  # returns MMDevice
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))

min_vol, max_vol, _ = volume.GetVolumeRange()

# ==============================
# WEBCAM SETUP
# ==============================
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not accessible")
    exit()

# ==============================
# HSV COLOR RANGES
# ==============================
# RED (Thumb)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# BLUE (Index)
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# ==============================
# HELPER FUNCTION TO FIND CENTER
# ==============================
def get_center(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 600:
            x, y, w, h = cv2.boundingRect(c)
            return (x + w // 2, y + h // 2)
    return None

# ==============================
# MAIN LOOP
# ==============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    thumb = get_center(red_mask)
    index = get_center(blue_mask)

    if thumb and index:
        # Draw markers and line
        cv2.circle(frame, thumb, 10, (0, 0, 255), -1)
        cv2.circle(frame, index, 10, (255, 0, 0), -1)
        cv2.line(frame, thumb, index, (0, 255, 0), 3)

        # Distance between thumb and index
        distance = hypot(index[0] - thumb[0],
                         index[1] - thumb[1])

        mid_x = (thumb[0] + index[0]) // 2

        # ==========================
        # RIGHT SIDE → VOLUME
        # ==========================
        if mid_x > w // 2:
            vol = np.interp(distance, [40, 250],
                            [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)

            vol_percent = int(np.interp(distance, [40, 250], [0, 100]))
            cv2.putText(frame, f"Volume: {vol_percent}%",
                        (40, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, (255, 0, 0), 3)

        # ==========================
        # LEFT SIDE → BRIGHTNESS
        # ==========================
        else:
            brightness = int(np.interp(distance, [40, 250], [0, 100]))
            sbc.set_brightness(brightness)

            cv2.putText(frame, f"Brightness: {brightness}%",
                        (40, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, (0, 255, 0), 3)

    cv2.imshow("Gesture Volume & Brightness Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ==============================
# CLEANUP
# ==============================
cap.release()
cv2.destroyAllWindows()
