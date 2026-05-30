import time

from picam.camera import create_camera

CAPTURE_INTERVAL_SECONDS = 2


def main() -> None:
    print("Starting Pi Tea Cam...")

    camera = create_camera()

    try:
        while True:
            frame = camera.capture_array()
            print(f"Captured frame: {frame.shape}")

            # TODO analyze motion score

            time.sleep(CAPTURE_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("Stopping Pi Tea Cam...")

    finally:
        camera.stop()


if __name__ == "__main__":
    main()
