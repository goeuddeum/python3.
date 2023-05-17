import cv2

img = cv2.imread('../img/blank_500.jpg')

cv2.rectangle(img, (495, 230), (90, 150), (0,50,100) )   
cv2.putText(img, "goeuddeum", (97, 200), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0))  

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()