# Pi Tea Cam

A Raspberry Pi computer vision project that monitors a tea brewing setup and alerts the user when motion is detected.

The project is being developed incrementally, with each version focused on a single capability before additional complexity is introduced.

## Roadmap

### V1 - Motion Detection

Goal: Detect motion and report it to the console.

Features:

* Capture frames from Raspberry Pi camera
* Calculate motion score using frame differencing
* Print motion score and detection status
* Basic threshold configuration

Success Criteria:

* Reliably distinguishes between "no motion" and "motion"
* Runs entirely on the Raspberry Pi

### V2 - Audio Alerts

Goal: Notify the user when motion is detected.

Features:

* Play alert sound when motion exceeds threshold
* Cooldown period to avoid repeated alerts
* Configurable alert settings

Success Criteria:

* User can walk away from the tea station and still receive notification

### V3 - Local Livestream

Goal: Enable the user to view the camera feed from another device on the local network.

Features:

* Local web page showing camera feed
* Frame overlays showing motion metrics
* Option to enable or disable debug overlays

Success Criteria:

* User can monitor the tea station from a phone or laptop on the same network

### V4 - Monitoring Dashboard

Goal: Provide a simple local dashboard for viewing system status and tuning detection behavior.

Features:

* Display current motion score and detection status
* Show recent motion events
* Adjust threshold and cooldown settings
* Start or stop monitoring from the local web interface

Success Criteria:

* User can monitor and tune the system without editing code directly



## Future Improvements

- Reduce libcamera startup logging
- Investigate SDN tuning warning


## Notes

### Frame Preparation
* Convert to grayscale: enables easier calculation with a single number, instead of RGB. 
* Blur: gaussian blur with kernel size 5 to preserve enough granularity to detect bubbles, while still removing noise. Tested with real data to find optimal kernel size. 
* Difference: absolute difference between previous and current frame
* Threshold: Any values in difference matrix below the threshold convert to 0
* Motion Score: Percent of the pixels that changed


## Version Notes

### V1 Complete

- Camera capture working
- Motion score calculation implemented
- Threshold-based motion detection implemented
- Tested on Raspberry Pi
