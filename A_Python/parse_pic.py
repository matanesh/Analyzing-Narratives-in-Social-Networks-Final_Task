# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
vid = cv2.VideoCapture("../ocean8/ocean_8_movie.mkv")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):
    
    # reading from frame
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()
    success, frame = vid.read()



    if success:
        # continue creating images until video remains
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()