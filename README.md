# Pi Tea Cam

A Raspberry Pi computer vision project that monitors a tea brewing setup and alerts the user when motion is detected.

The project is being developed incrementally, with each version focused on a single capability before additional complexity is introduced.

## Safety Disclaimer

This project is an experimental monitoring aid. Do not rely on it as the only way to monitor a stove, kettle, or other heat source. Please use responsibly. 

## Roadmap

### v1.0.0 - Motion Detection ✅

Goal: Detect motion and report it to the console.

Features:

* Capture frames from Raspberry Pi camera
* Calculate motion score using frame differences
* Print motion score and detection status
* Basic threshold configuration

Success Criteria:

* Reliably distinguishes between "no motion" and "motion"
* Runs entirely on the Raspberry Pi

Status: Complete


### v1.1.0 - Dashboard

Goal: Make a local dashboard for monitoring system status.

Features:

* Create a local web interface that is accessible by devices on the same network
* Display current motion score and detection status

Success Criteria:

* User can see motion scores without connecting to the Raspberry Pi console 


### v1.2.0 - Controls

Goal: Allow user to fine tune and start/stop monitoring from the dashboard

Features:
* Start and stop monitoring from a local web interface
* Adjust threshold and cooldown settings
* Display current monitoring status and threshold values

Success Criteria:
* User can start, monitor, and tune the system without editing code directly

### v1.3.0 - Audio Alerts

Goal: Notify the user when motion is detected.

Features:

* Trigger alert when motion exceeds threshold
* Play alert sound on connected device
* Configurable alert settings

Success Criteria:

* User can walk away from the tea station and still receive notification

### v1.4.0 - Local Livestream

Goal: Enable the user to view the camera feed from another device on the local network.

Features:

* Local web page showing camera feed
* Frame overlays showing motion metrics
* Option to enable or disable debug overlays

Success Criteria:
* User can visually monitor the tea station from a phone or laptop on the same network


## Future Improvements

### Lite Mode (Future Concept)

A standalone appliance-style version that operates without a phone or dashboard.

**Potential Features:**
* Physical start/stop button connected to Raspberry Pi GPIO
* Dedicated speaker for local audio alerts
* Automatic startup on boot
* Simplified status indicators

### Additional Ideas
* Motion event logging
* Video clip recording
* Multiple monitoring profiles
* Remote notifications
* Smart plug integration

### Code Optimizations
* Reduce libcamera startup logging
* Investigate SDN tuning warning


## Notes

### Frame Preparation
* Convert to grayscale: enables easier calculation with a single number, instead of RGB. 
* Blur: gaussian blur with kernel size 5 to preserve enough granularity to detect bubbles, while still removing noise. Tested with real data to find optimal kernel size. 
* Difference: absolute difference between previous and current frame
* Threshold: Any values in difference matrix below the threshold convert to 0
* Motion Score: Percent of the pixels that changed
