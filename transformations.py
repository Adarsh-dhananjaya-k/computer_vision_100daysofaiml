import numpy as np 
import cv2 as cv 


def read_photos_and_videos(path,is_video=False):

    if is_video:
        return cv.VideoCapture(path)
    else:
        return cv.imread(path)
    
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


def rotation_image(img ,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (height//2,width//2)

    rototeMat = cv.getRotationMatrix2D(rotPoint,angle,.5)
    demension = (width,height)
    return cv.warpAffine(img,rototeMat,demension)

def resize_filpping_crop_image(img):
    resizing_img = cv.resize(img,(50,50),interpolation=cv.INTER_CUBIC)
    cv.imshow("resized_image ", resizing_img)
    cv.waitKey(1000)
    filped_img = cv.flip(img,0)
    cv.imshow("filed image ", filped_img)
    cv.waitKey(1000)

    croped_image = img[200:450,200:339]
    cv.imshow("resized_image ", croped_image)
    cv.waitKey(1000)

if __name__=='__main__':
    
    img = read_photos_and_videos('Resources/Photos/cats.jpg')
    cv.imshow('cat ',img )
    translated_image = translate(img,-100,200)
    cv.imshow("transalted_image",translated_image)
    cv.waitKey(1000)
    rotote_img= rotation_image(img,45)
    cv.imshow("rotated_image",rotote_img)
    cv.waitKey(1000)
    resize_filpping_crop_image(img)