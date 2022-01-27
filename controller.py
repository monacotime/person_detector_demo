import cv2
from pose import MPPose

class Controller:
    def __init__(self) -> None:
        self.camera = cv2.VideoCapture(0)
        self.pose = MPPose()
        pass

    def gen_frames(self):
        while True:
            success, frame = self.camera.read()
            if not success:
                break
            else:
                frame = self.pose.handle_pose(frame)
                yield self.package_frame(frame)

    def package_frame(self, frame):
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        return (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')