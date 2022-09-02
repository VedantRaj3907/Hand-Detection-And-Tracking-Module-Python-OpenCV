
# HAND TRACKING AND DETECTION MODULE






## SAMPLE OUTPUT

![Logo](https://github.com/VedantRaj3907/Hand-Detection-And-Tracking-Module-Python-OpenCV/blob/main/Hand%20Dectection%20And%20Tracking/Images/hand_Track_1.jpg)



## INTRODUTION

- The Hand Tracking Module can be used by anyone.
- Who wants to use it in his/her project for detection hands and using them
- This Module uses mainly openCV (cv2) library of python for video and other detections

- ***First You need to install some modules to run this file***





## Installation

Go to your Cmd or Python Shell or Anaconda Prompt (if using spyder or Jupyter)

**You need to install 2 Libraries**
- OpenCV (cv2)
- mediapipe
```bash
  pip install opencv-python
  pip install mediapipe
```

:point_right: ***Once Both of them are install you are good to run the Script or can call it in your own project
:thumbsup:***


    
## Project Contains


- A Function called **FindHands()** to find your hand 21 Tips (Green Dots you can See) each has its unique Numbered Postion which you can use

- A Function called **FindPosition()** to find the accurate position of the points and drawing the hand landmarks (connecting all the points using a line) also creating circles on the Tips

- A Function called **CalcFPS()** to calculate the Frames you get which is displayed at the left-top most  corner

- A Function **FingersUp()** used to see how many fingers are opened and how many are closed (which is calculated using the first point of the tips of all the fingers)

- And a Temp **main()** to run the file


# Please Give Star :star: if you like the Project and visit other Projects to :heart:


