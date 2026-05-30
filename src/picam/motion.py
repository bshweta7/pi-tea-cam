import cv2
import numpy as np

DIFF_THRESHOLD = 25
BLUR_KERNEL_SIZE = (5, 5)


def prepare_frame(frame: np.ndarray) -> np.ndarray:
    """Convert a camera frame to grayscale and blur it for motion comparison."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    return cv2.GaussianBlur(gray, ksize=BLUR_KERNEL_SIZE, sigmaX=0)


def calculate_motion_score(previous_frame: np.ndarray, current_frame: np.ndarray) -> float:
    """Calculate percent of pixels that changed between two prepared frames."""
    diff = cv2.absdiff(previous_frame, current_frame)
    _, thresholded = cv2.threshold(diff, DIFF_THRESHOLD, 255, cv2.THRESH_BINARY)

    changed_pixels = cv2.countNonZero(thresholded)
    total_pixels = thresholded.shape[0] * thresholded.shape[1]

    return changed_pixels / total_pixels

