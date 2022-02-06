import cv2
import numpy as np
import time
import os
from pynput import keyboard

#obs virtual cam seems to be 2 and webcam is 0
cap = cv2.VideoCapture(2)
file_name = "/home/cwy/Code/Fall-Guys-AI-mas/data/training_data.npy"
file_name2 = "/home/cwy/Code/Fall-Guys-AI-mas/data/target_data.npy"

keys = keyboard.Key
###################################

def on_press(key):
    global keys
    keys = key.char

def on_release(key):
  pass


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
while True:
    print("Waiting...press 'B' to start!")
    time.sleep(2)

    if keys=="b":
        print("Starting")
        break

count = 0

while True:
    count += 1
    last_time = time.time()
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img,100,250)
    #img = cv2.resize(img,(224,224))

    #convert to numpy array
    img = np.array(img)
    image_data.append(img)

    if keys == 'a' or 'd':
        print("Appended keys")
        targets.append(keys)


    #uncomment to show video
    cv2.imshow("Video",img)
    if keys == 'h':
    #if cv2.waitKey(1) & 0xFF ==ord('h'):
        break
    print('Loop took {} seconds'.format(time.time()-last_time))
save_data(image_data,targets)
