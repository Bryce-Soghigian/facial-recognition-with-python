import face_recognition
import urllib3
import numpy as np
import cv2




"""


=================================================

Facial recogniton at my door
Have a voice command that will take the picture.
after we get the picture we upload it to my server
then we pass the url to the check if valid user function
if valid user returns true we send an unlock signal to the door
else send a phone notification with twillo saying they failed to unlock the door
after the door is closed lock it behind me

===================================================



    picture_of_me = face_recognition.load_image_file("./images/me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]


unknown_picture = face_recognition.load_image_file("./images/unknownfalse.png")
unknown_encoding = face_recognition.face_encodings(unknown_picture)[0]

results = face_recognition.compare_faces([my_face_encoding],unknown_encoding)


if results[0]== True:
    print("THAT IS BRYCE")
else:
    print("FALSE THAT IS not me")
"""
def check_if_valid_face(img_url):
    #encodes the image that is valid
    valid_user = face_recognition.load_image_file("./images/me.jpg")
    valid_encoding = face_recognition.face_encodings(valid_user)[0]

    #Encoding the image from the web
    resp = urllib3.urlopen(img_url)
    image = np.asarray(bytearray(resp.read()),dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #Encodes unknown image
    unknown_pic = face_recognition.load_image_file(image)
    unknown_encoding = face_recognition.face_encodings(unknown_pic)[0]
    #Results of the facial comparison
    results = face_recognition.compare_faces([valid_encoding],unknown_encoding)
    print(f"results:{results}")
    if results[0]==True:
        return True
    else:
        return False


check_if_valid_face("https://avatars3.githubusercontent.com/u/49734722?s=400&u=a69054f55a814d8fc7b39fe7b528d6b17b22af3e&v=4")




