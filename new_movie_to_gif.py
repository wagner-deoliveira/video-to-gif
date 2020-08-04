from moviepy.editor import *
from pygifsicle import optimize

# import subprocess

# gif_video = "Triaxis.mp4"
# output = "Triaxis_compressed.mp4"
# subprocess.run('ffmeg -i ' + gif_video + ' -vcodec libx264 -crf 22' + output)

path = 'Triaxis.gif'
clip = (VideoFileClip('Triaxis.mp4')
        .subclip()
        .resize(0.3))
clip.write_gif(path)

# importing libraries
import cv2

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('Triaxis.gif')

# Check if camera opened successfully
if (cap.isOpened() == False):
        print("Error opening video file")

# Read until video is completed
while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

                # Display the resulting frame
                cv2.imshow('Frame', frame)

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

        # Break the loop
        else:
                break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

optimize(path)
