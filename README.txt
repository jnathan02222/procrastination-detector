Procrastinator Detector is a program that alerts the user when unproductive behavior is observed.

1. Clone this repo.
2. Record your screen for undesired behavior for a given amount of time (more results in greater accuracy). Repeat with desired behavior. 
3. Export each recording as a series of images, and place in the 'frames' folder. Try to keep the aspect ratio the same when exporting (eg. 16:9).
    a. Ensure that each frame of undesired behavior has "unproductive" in its file name. Likewise, ensure that desired behavior is labelled "productive."
5. Run model_trainer.py, allow the model to train.
6. Using the resulting file (), detector.py observes the user's screen and pushes notifications when undesired behavior is detected. 


Possible issues
-Missing frames folder
-No images
-Images of different sizes

-Missing model