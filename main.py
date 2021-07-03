import cv2
import dropbox
import time
import random

start_time = time.time()

def main():
    num = 1
    while True :
        if time.time()-start_time >= 5 : 
          series = takePic()
          num = num + 1
          uploadFiles(series,num)
            

def uploadFiles(series,num):
    access_token = "0DNWXwlFR2cAAAAAAAAAAe-nE-ssqiO9wpmwKuOdzhySSc6UV5A-t89drsBQCaqR"
    file_from = series
    file_to = "/img" + str(num) + ".png"
    transfer = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        transfer.files_upload(f.read(),file_to)
    print("The picture is transferred.")

def takePic():
    cam = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = cam.read()
        img = "img.png"
        cv2.imwrite(img,frame)
        result = False
        return img
    cam.release()
    cv2.destroyAllWindows()


main()