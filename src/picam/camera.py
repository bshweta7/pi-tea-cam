from picamera2 import Picamera2


def create_camera() -> Picamera2:
    camera = Picamera2()
    camera.start()
    return camera
