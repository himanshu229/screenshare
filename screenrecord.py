# from flask import Flask, Response
# import mss
# import cv2
# import numpy as np

# app = Flask(__name__)

# def capture_screen():
#     with mss.mss() as sct:
#         monitor = sct.monitors[1]
#         while True:
#             img = np.array(sct.grab(monitor))
#             frame = cv2.imencode('.jpg', img)[1].tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/screen')
# def screen_stream():
#     return Response(capture_screen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, Response
import mss
import cv2
import numpy as np
import qrcode

app = Flask(__name__)

# Function to capture the screen
def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary monitor
        while True:
            img = np.array(sct.grab(monitor))  # Grab the screen
            frame = cv2.imencode('.jpg', img)[1].tobytes()  # Encode the frame as JPEG
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Flask route for screen streaming
@app.route('/screen')
def screen_stream():
    return Response(capture_screen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Generate a QR code for the IP address of the server
def generate_qr_code(ip_address):
    qr = qrcode.make(ip_address)
    qr.show()

if __name__ == "__main__":
    # Define the server's IP address and port
    ip_address = "http://192.168.1.10:5000"
    print(f"Server running at: {ip_address}")

    # Generate and display the QR code
    generate_qr_code(ip_address)

    # Start the Flask server
    app.run(host='0.0.0.0', port=5000)


# netstat -ano | findstr :5000
#taskkill /PID 1234 /F
