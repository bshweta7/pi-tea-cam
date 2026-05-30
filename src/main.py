import time

CAPTURE_INTERVAL_SECONDS = 2


def main() -> None:
    print("Starting Pi Tea Cam...")

    try:
        while True:
            print(f"Capture and Analyze Frame") # TODO

            time.sleep(CAPTURE_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("Stopping Pi Tea Cam...")


if __name__ == "__main__":
    main()
