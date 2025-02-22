# Import required libraries
import cv2



class ObjectTracker:
    def __init__(self):
        """Initialize the object tracker using OpenCV's CSRT tracker."""
        self.tracker = cv2.TrackerCSRT.create()
        self.cap = cv2.VideoCapture(0)  # Open webcam



    def select_object(self):
        """Allow the user to manually select an object in the frame."""
        if not self.cap.isOpened():
            print("Error: Unable to access webcam")
            return False

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Unable to capture video")
                return False
            frame1 = frame.copy()
            cv2.putText(frame, "Press 'S' to select object | 'Q' to exit", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.imshow('Frame', frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == ord('Q'):
                return False  # Exit
            if key == ord('s') or key == ord('S'):
                cv2.destroyAllWindows()
                # Select the ROI
                while True:
                    try:
                        cv2.putText(frame1, "'Enter' to confirm selection | Press 'C' to cancel selection", (50, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        selected_box = cv2.selectROI("Select Object", frame1, fromCenter=False, showCrosshair=True)
                        self.tracker.init(frame1, selected_box) # Initialize the tracker with the selected ROI
                        cv2.destroyWindow("Select Object")
                        return True  # Successfully selected an object
                    except:
                        print("You didn't select ROI please select it")



    def run_tracker(self):
        """Run the object tracker on the selected object."""
        if not self.select_object():
            self.cap.release()
            cv2.destroyAllWindows()
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Update tracker
            success, box = self.tracker.update(frame)

            # Draw bounding box
            if success:
                x, y, w, h = box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 255, 0), 2)
                cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            else:
                cv2.putText(frame, "Lost Track", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("Tracked Object", frame)

            # Exit on 'q' key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == ord('Q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    tracker = ObjectTracker()
    tracker.run_tracker()
