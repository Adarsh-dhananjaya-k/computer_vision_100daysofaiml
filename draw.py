import numpy as np 
import cv2 as cv 

def create_blank_image():
    blank_image = np.zeros((500,500,3), dtype='uint8')
    return blank_image 

def color_image_area(image):
    cv.imshow('blank_image',image)
    cv.waitKey(0)

    # changeing the color of the image to orange
    image[:]=0,100,225
    cv.imshow("green_image",image)

    cv.waitKey(0)

def create_shapes_on_image(image):
    # Draw rectangle shape 
    cv.rectangle(image,(0,0),(250,250),(250,0,0),cv.FILLED)
    cv.imshow("rectangle shape",image)

    # Draw the circle image 
    cv.circle(image,(250,250),200,(0,200,250),7)
    cv.imshow("circle",image)

    # Draw the line image
    cv.line(image,(100,200),(233,444),(20,200,100),5)
    cv.imshow("line",image)
    
    # Write the text in the image
    new_image = create_blank_image()
    cv.putText(new_image,"hello_cv_world",(25,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(10,200,20),2)
    cv.imshow("written text", new_image)
    cv.waitKey(2000)   


if __name__ == '__main__':
    image = create_blank_image()
    print(image.shape)
    create_shapes_on_image(image)
