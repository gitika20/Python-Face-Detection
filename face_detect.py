import cv2,time

# create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capturing video using webcam 
cap = cv2.VideoCapture(0)
check, frame = cap.read()

print(check)
print(frame)
time.sleep(3) 
while True:
    # To read the frame
    s, img = cap.read()

    # Converting the image as grayscale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Search coordinates of the faces
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.1,minNeighbors=4)

    # Rectange is drawn around face detected
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Capture', img)

    # To exit press Esc key
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
      
cap.release()