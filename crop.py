import cv2


img = cv2.imread('shuriken.jpg')
print(img.shape)
# 카드의 크기는 436 X 648 (px)
# border의 크기는 5px

width, height, chennal = img.shape
start_x, end_x = (width // 2) - (436 // 2) + 5, (width // 2) + (436 // 2) - 5 
start_y, end_y = (height // 2) - (648 // 2) + 5, (height // 2) + (648 // 2) - 5 

cropped = img[start_y-1 : end_y-1, start_x-1: end_x-1]
cv2.imwrite('shuriken.jpg',  cropped)