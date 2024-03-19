import cv2
import face_recognition as fr

img1 = fr.load_image_file("C:\\Users\\KHUSHI SHARMA\\PycharmProjects\\Face_Recoginition_Project\\img1.jpg")
img2 = fr.load_image_file("C:\\Users\\KHUSHI SHARMA\\PycharmProjects\\Face_Recoginition_Project\\img3.jpg")
x = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
y = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
enc1 = fr.face_encodings(x)[0]
enc2 = fr.face_encodings(y)[0]
res = fr.compare_faces([enc1], enc2, tolerance=0.1)
print(res)
