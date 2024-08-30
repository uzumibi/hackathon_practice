import time

import cv2

from testapp.gpt.gpt_response import get_gpt

W = 640
H = 480
cap = cv2.VideoCapture()
cap.open("http://192.168.0.6:4747/video")
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, H)
cap.set(cv2.CAP_PROP_FPS, 30)


def show_frame(frame):
    cv2.imshow("frame", frame)
    _, buffer = cv2.imencode(".jpg", frame)
    get_gpt(buffer.tobytes())


# Initialize timing variables
last_display_time = time.time()
display_interval = 5  # interval in seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to retrieve frame.")
        break

    current_time = time.time()

    # Check if it's time to display a new frame
    if current_time - last_display_time >= display_interval:
        show_frame(frame)
        last_display_time = current_time

    # Check for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
