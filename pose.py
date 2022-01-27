import cv2
import mediapipe as mp

class MPPose:
    def __init__(self) -> None:
        self.mp_drawing = mp.solutions.drawing_utils 
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.pose = mp.solutions.pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        pass

    def handle_pose(self, image):
        return self.draw_pose(image, self.get_landmarks(image))

    def get_landmarks(self, image) -> None:
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return self.pose.process(image)

    def draw_pose(self, image, results):
        image.flags.writeable = True
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        self.mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp.solutions.pose.POSE_CONNECTIONS,
            landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())
        return image