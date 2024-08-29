import cv2 as cv 

def read_photos_and_videos(path,is_video=False):

    if is_video:
        return cv.VideoCapture(path)
    else:
        return cv.imread(path)


######################################################################## Rescaling and resizing images and videos #########################################################################

def rescalesFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] + scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def resize_video():
    capture = read_photos_and_videos('Resources/Videos/dog.mp4',True)

    while True:
        isTrue, frame = capture.read()
        resized_frame =  rescalesFrame(frame,.2)
        cv.imshow('main',frame)
        cv.imshow('resized_frame',resized_frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    
    cv.destroyAllWindows()

def resize_image():
    img = read_photos_and_videos('Resources/Photos/cat.jpg')
    cv.imshow('cat ',img )
    resized_imag = rescalesFrame(img,.3)
    cv.imshow('cat image resizes ',resized_imag)
    cv.waitKey(0)

def changeResolution(width, height):
    capture = cv.VideoCapture(0)
    while True:
        isTrue,frame = capture.read()
        capture.set(3, width)
        capture.set(4, height)
        capture.set(10,300)
        cv.imshow('livestream',frame)


        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    # resizing images and video  
    # resize_video()
    # resize_image()
    
    #  changing the resolution of live image    
    changeResolution(20,10)