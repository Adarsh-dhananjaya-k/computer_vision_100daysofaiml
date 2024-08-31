import cv2 as cv

def convert_to_grayScale(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray scale image ", gray)
    cv.waitKey(1000)


def create_blur(image):
    blur = cv.GaussianBlur(image, (3, 3), cv.BORDER_DEFAULT)
    cv.imshow("blur image", blur)
    cv.waitKey(1000)


def Edge_cascade(image):
    canny = cv.Canny(image,125,175)
    cv.imshow("Canny Edge", canny)

    dilated_image = cv.dilate(canny,(2,2),iterations=2)
    cv.imshow("dilated image",dilated_image)
    cv.waitKey(1000)
    
    eroded_image = cv.erode(canny,(3,3),iterations=3)
    cv.imshow("eroded_image",eroded_image)
    cv.waitKey(0)
    
    # cropping image 
    cropped_image  = canny[50:200,200:300]
    cv.imshow(cropped_image)
    cv.waitKey(0)

if __name__ == "__main__":
    image = cv.imread("/Users/adarsh/open_cv/Resources/Photos/cat.jpg")
    convert_to_grayScale(image)
    create_blur(image)
    Edge_cascade(image)
