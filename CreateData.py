import cv2
import numpy as np
import time
import os
from pynput import keyboard

#obs virtual cam seems to be 2 and webcam is 0
cap = cv2.VideoCapture(2)
file_name = "data/training_data.npy"
file_name2 = "data/target_data.npy"


keys = keyboard.Key
###################################

def on_press(key):
    global keys
    try:
        keys = key.char
    except AttributeError:
        keys = "W"

def on_release(key):
  global keys
  keys = "W"


listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

##############################


def get_data():
    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets

def save_data(image_data, targets):
    np.save(file_name,image_data)
    np.save(file_name2, targets)

image_data, targets = get_data()
print("Press esc to start and h to stop.")
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            print("Starting! in 3 seconds")
            time.sleep(3)
            break

count = 0

while True:

    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.Canny(img,100,250)
    img = img[120:500,50:750]
    img = cv2.resize(img,(224,224))
    #cv2.imshow("Video", img)
    #cv2.waitKey(1)
    count += 1
    last_time = time.time()

    #convert to numpy array
    img = np.array(img)
    image_data.append(img)

    if keys == 'a':
        targets.append('A')
        print("A - LEFT")
    elif keys == 'd':
        targets.append("D")
        print("D - Right!")
    elif keys == 'z':
        targets.append("Z")
        print("HONK and FIRE - Z button")
    else:
        targets.append("W")
        print("Nothing! W")


    #uncomment to show video

    if keys == 'h':
        break
    #print('Loop took {} seconds'.format(time.time()-last_time))
save_data(image_data,targets)



