import cv2

def enhance(image):

    image = cv2.GaussianBlur(image,(5,5),0)

    image = cv2.equalizeHist(image)

    return image
