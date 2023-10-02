
import os
import pyscreenshot
import keyboard
import cv2
from utils.grab_screen import grab_screen
from PIL import Image, ImageGrab
import mss
import numpy as np
 

def object_detection(window):
    
    blueMan = cv2.imread(r'C:\Users\seca\Documents\Python Work\Images for opencv\blue uncropped.png', cv2.IMREAD_UNCHANGED )

    redMan = cv2.imread(r'C:\Users\seca\Documents\Python Work\Images for opencv\Red uncropped.png', cv2.IMREAD_UNCHANGED)

    ball = cv2.imread(r'C:\Users\seca\Documents\Python Work\Images for opencv\ball.png', cv2.IMREAD_UNCHANGED ) # Using grayscale for this algorithm

    field = cv2.imread(r'C:\Users\seca\Documents\Python Work\Images for opencv\red detection.png', cv2.IMREAD_UNCHANGED) ###

    result = cv2.matchTemplate(window, redMan, cv2.TM_CCOEFF_NORMED) # changed

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    ball_w = ball.shape[1]
    ball_h = ball.shape[0]

    red_w = redMan.shape[1]
    red_h = redMan.shape[0]

    blue_w = blueMan.shape[1]
    blue_h = blueMan.shape[0]


    cv2.rectangle(window, max_loc, (max_loc[0] + red_w, max_loc[1] + red_h), (0,255,255), 2) #changed

    #cv2.waitKey(0)
    
    threshold = .60

    yloc, xloc = np.where(result >= threshold)

    #print(len(xloc))

    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(window, (x, y), (x + red_w, y + red_h), (0,255,255), 2) #changed

    red_Rectangles = []

    for (x, y) in zip(xloc, yloc):
        red_Rectangles.append([int(x), int(y), int(red_w), int(red_h) ])  # If too low, duplicate. this line so its 2 per

    rectangles, weights = cv2.groupRectangles(red_Rectangles, 1, 0.2)

    for (x, y, w, h) in red_Rectangles:
        cv2.rectangle(window, (x, y), (x + red_w, y + red_h), (0,255,255), 2)  #changed what was this 2 again?

    #cv2.waitKey(1)
    
    cv2.imshow('Bot View', window)


count = 0

pic = 1

os.chdir(r"C:\Users\seca\Documents\Python Work\Images for opencv\img")

print(os.listdir())

my_path = str(r"C:\Users\seca\Documents\Python Work\Images for opencv\img\ ")
img_path = my_path

while not keyboard.is_pressed("q"):

    image = grab_screen(region=(1, 1, 1910, 966)) #1910 x 966 
    image = image[:, :, ::-1].copy() # convert from bgr to rgb

    #cv2.imshow('Bot View', image)
    cv2.waitKey(1)

    if count % 50 == 0:
        cv2.imwrite(f"{img_path}BotView{pic}.jpg", image)
        print(f"Saved Picture numder: {pic}")
        pic += 1

    count += 1

    if keyboard.is_pressed("/"):
        
        print("You are currently in: " + str(os.getcwd()) + " Delete all img files? ")

        cv2.waitKey(0)

        if keyboard.is_pressed("y") or keyboard.is_pressed("Y"):
            dir = os.listdir()
            
            for item in dir:
                if item.endswith(".jpg"):
                    os.remove(item)
                    print("removing")
            break
        
        if keyboard.is_pressed("n") or keyboard.is_pressed("N"):

            continue

    
    #cv2.imshow('Bot View', image)
    
    object_detection(image)
