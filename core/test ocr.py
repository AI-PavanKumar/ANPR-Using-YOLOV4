import cv2
import  pytesseract
test_license_plate=cv2.imread(r'C:\Users\pavan\PycharmProjects\ANPR-YoloV4\plate.PNG',-1)
print(test_license_plate)
cv2.imshow('image',test_license_plate)
resize_test_license_plate = cv2.resize(
    test_license_plate, None, fx = 2, fy = 2,
    interpolation = cv2.INTER_CUBIC)
grayscale_resize_test_license_plate = cv2.cvtColor(
    resize_test_license_plate, cv2.COLOR_BGR2GRAY)
gaussian_blur_license_plate = cv2.GaussianBlur(
    grayscale_resize_test_license_plate, (5, 5), 0)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
new_predicted_result_GWT2180 = pytesseract.image_to_string(gaussian_blur_license_plate, lang ='eng',

                                                            config ='--oem 3 -l eng --psm 6 -c tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')


filter_new_predicted_result_GWT2180 = "".join(new_predicted_result_GWT2180.split()).replace(":", "").replace("-", "")
print(filter_new_predicted_result_GWT2180)

cv2.waitKey(0)
cv2.destroyAllWindows()