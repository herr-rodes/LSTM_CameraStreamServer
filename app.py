from flask import Flask
"""
from time import time

//Replace this with the actual frame grabbing wrawpper
class Camera(object):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frames[int(time()) % 3]
"""

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


"""
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
#Replace this with the hello world thingy        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
