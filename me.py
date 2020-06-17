import face_recognition
#Encoding picture of me
picture_of_me = face_recognition.load_image_file("./images/me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]


unknown_picture = face_recognition.load_image_file("./images/unknowntrue.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_picture)[0]

results = face_recognition.compare_faces([my_face_encoding],unknown_encoding)


if results[0]== True:
    print("THAT IS BRYCE")
else:
    print("FALSE THAT IS not me")




