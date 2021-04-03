import time 
import os 

while True: # do forever

    

    os.system('fswebcam -d /dev/video0 -r 1920x1080 -S 3 --jpeg 50 --save /home/pi/Desktop/images/saveimage/%H%M%S.jpg') # uses Fswebcam to take picture

    time.sleep(10) # this line creates a 10 second delay before repeating the loop
    
    os.system('fswebcam -d /dev/video4 -r 1920x1080 -S 3 --jpeg 50 --save /home/pi/Desktop/images/saveimage/%H%M%S.jpg') # takes picture with second camera
    
    time.sleep(10) # 10 second
    
    # python3 /home/pi/Desktop/images/image.py to run in terminal
