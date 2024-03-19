import face_recognition as fr
import cv2
img1 = fr.load_image_file("C:\\Users\\KHUSHI SHARMA\\PycharmProjects\\Face_Recoginition_Project\\img1.jpg")
cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
landmarks= fr.face_landmarks(img1)[0]
print(landmarks)
top, right, bottom, left = location;
face = img1[top:bottom,left:right]
img_draw.line(landmarks["Left_eye"])
img_draw.line(landmarks["Right_eye"])
cv2.imshow("Face.....",face);
cv2.waitKey(0)

