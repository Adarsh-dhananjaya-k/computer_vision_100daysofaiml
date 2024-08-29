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
    cv.dilate(canny,(2,2))
    cv.waitKey(2000)


if __name__ == "__main__":
    image = cv.imread("/Users/adarsh/open_cv/Resources/Photos/cat.jpg")
    convert_to_grayScale(image)
    create_blur(image)
    Edge_cascade(image)
