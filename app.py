from flask import Flask, render_template, Response
from controller import Controller


app = Flask(__name__)
controller = Controller()

@app.route('/')
def index():
    return "Server is running"

@app.route('/video_feed')
def video_feed():
    return Response(controller.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)