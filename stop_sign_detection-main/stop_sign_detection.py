import cv2


stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')
image_path = r'WE3XG8QI_2_B_1_1.jpg'
image_path = r'STOP_sign.jpg'
img = cv2.imread(image_path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)

    if len(stop_sign_scaled) > 0:
        print("Helal!")  

    for (x, y, w, h) in stop_sign_scaled:
        stop_sign_rectangle = cv2.rectangle(img, (x, y),
                                            (x + w, y + h),
                                            (0, 255, 0), 3)

        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                     text="Stop Sign",
                                     org=(x, y + h + 30),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv2.LINE_4)

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Görüntü yüklenemedi: {image_path}")
