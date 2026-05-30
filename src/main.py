import time

from picam.camera import create_camera
from picam.motion import calculate_motion_score, prepare_frame

CAPTURE_INTERVAL_SECONDS = 2


def main() -> None:
    print("Starting Pi Tea Cam...")

    camera = create_camera()

    try:

        frame_number = 0
        previous_frame = None

        while True:
            raw_frame = camera.capture_array()
            current_frame = prepare_frame(raw_frame)

            # Skip first frame
            if previous_frame is not None:
                motion_score = calculate_motion_score(previous_frame, current_frame)
                print(f"Frame {frame_number} | Motion score: {motion_score:.4f}")

            previous_frame = current_frame
            frame_number += 1

            time.sleep(CAPTURE_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("Stopping Pi Tea Cam...")

    finally:
        camera.stop()


if __name__ == "__main__":
    main()
