import mss
import numpy as np
from flask import Flask, Response, render_template_string
import cv2

# Flask app setup
app = Flask(__name__)

# HTML template for the client-side web interface
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desktop Stream</title>
</head>
<body style="margin: 0; padding: 0;">
    <img src="/stream" style="width: 100%; height: 100vh;" alt="Desktop Stream">
</body>
</html>
"""

# Function to capture desktop frames
def generate_frames():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary monitor
        while True:
            # Capture the screen
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)

            # Yield the frame as a response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# Route to serve the video stream
@app.route('/stream')
def stream():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template_string(html_template)

# Start the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
