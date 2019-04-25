import cv2

img = cv2.imread("dashka.jpg", 0)

print(img.shape, img.ndim)

resized_img = cv2.resize(img,(int(img.shape[1]/4), int(img.shape[0]/4)))

cv2.imshow("Dashka",resized_img)
cv2.imwrite("Resized_dashka.jpg", resized_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()