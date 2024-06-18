import cv2
import os

def capture_and_save_photo():
    # Open the default camera (usually the first one available)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Capture a single frame from the camera
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Close OpenCV window
    cv2.destroyAllWindows()

    # Check if the frame is captured successfully
    if ret:
        # Define the path to save the photo
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        photo_path = os.path.join(desktop_path, 'captured_photo.jpg')

        # Save the captured frame as a photo
        cv2.imwrite(photo_path, frame)
        
    else:
        print("Error: Failed to capture photo.")


if __name__ == "__main__":
    capture_and_save_photo()