import glob
import cv2

files = glob.glob("*.jpg")
for elem in files:
    img = cv2.imread(elem, 1)
    resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    cv2.imshow(elem, resized_img)
    cv2.imwrite("resized_"+elem, resized_img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

