import cv2

src = cv2.imread(r"C:\Users\Administrator\Pictures\Camera Roll\th.jpg")

im_encode_str = cv2.imencode('.jpg', src)[1].tostring()

print(im_encode_str);

with open('C:\\Users\\Administrator\\Pictures\\Camera Roll\\test3.jpeg', 'rb') as fp:
    image = fp.read()

# cv.imshow("opencv-python", src)
# cv.waitKey(0)

cap = cv2.VideoCapture(0)
# while 1:
#     ret, frame = cap.read()
#     cv2.imshow("cap", frame)
#     if cv2.waitKey(100) & 0xff == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


def GetView():

    name="myPhoto"
    var =0
    while 1:
        ret, frame = cap.read()
        cv2.imshow("cap", frame)
        cv2.imwrite(str(var)+".jpg",frame);

        var = var+1
        if cv2.waitKey(1000) & 0xff == ord('q'):
            break



#GetView();