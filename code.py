#Python3.whatever
from PIL import Image #imports the python library for image manipulation
import face_recognition #imports the face_recognition library
import os
import sys
import io
import math
from pprint import pprint
os.chdir("/home/nate/Projects/GitHub/DealWithItPhotoMaker")
glasses = Image.open("marker.png").convert("RGBA")#Brings those nasty Shadezzz
Target = Image.open("barry obammy.jpg").convert("RGBA")#Brings in your victimage
target4recognition = face_recognition.api.load_image_file("barry obammy.jpg")# loads target into facial recognition
rawlocations = face_recognition.api.face_landmarks(target4recognition)

def somefunction(bullshit):
    listone = []
    listtwo = []
    listthree = []
    listfour = []
    for x in bullshit:
        for y in x:
            if y == "left_eye":
                for z in x[y]:
                    listone.append(z[0])
                    listtwo.append(z[1])
            if y == "right_eye":
                for z in x[y]:
                    listthree.append(z[0])
                    listfour.append(z[1])
    leftx = int(sum(listone)/len(listone))
    lefty = int(sum(listtwo)/len(listtwo))
    rightx = int(sum(listthree)/len(listthree))
    righty = int (sum(listfour)/len(listfour))
    toreturn = [leftx, lefty, rightx, righty]
    return toreturn
yolo = somefunction(rawlocations)#this function will return (lefteyex,lefteyey),(righteyex,righteyey)
pprint(yolo)
leftx = yolo[0]-64
lefty = yolo[1]-64
Target.paste(glasses,(leftx,lefty),glasses)
Target.show()
Target.save(testone)
#todo-- code to modify the glasses to be the correct size and orientation

#Target.paste(glasses,(x,y),glasses)
