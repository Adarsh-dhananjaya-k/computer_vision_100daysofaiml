import numpy as np 
import cv2 as cv 

def read_photos_and_videos(path,is_video=False):

    if is_video:
        return cv.VideoCapture(path)
    else:
        return cv.imread(path)

def find_couturs(img):
    # conver the image to grey scale 
    grey_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow(" grey image ",grey_scale)
    
    # buluring the image for better edge dections 
    blur_image = cv.blur(grey_scale,(2,2),cv.BORDER_ISOLATED)
    cv.imshow("blur image ",blur_image)
    
    # finding the edges in the image using canny 
    canny_image = cv.Canny(blur_image,125,124)
    cv.imshow("Canny Edge", canny_image)
    
    ret,threshold = cv.threshold(grey_scale,125,255,cv.THRESH_BINARY)
    cv.imshow("threshold image  ", threshold)
    
    blank_image = np.zeros(img.shape,dtype='uint32')

    contours,hierachy = cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    print(f'{len(contours)}')
    cv.drawContours(blank_image,contours,-1,(0,0,255),1)
    cv.imshow(" contours image draw ")

    cv.waitKey(0)




if __name__=='__main__':
    
    img = read_photos_and_videos('Resources/Photos/cats.jpg')
    cv.imshow('cat ',img ) 
    find_couturs(img)











