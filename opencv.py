import cv2

# Haar Cascade dosyasını yüklüyorum
face_cascade = cv2.CascadeClassifier('C:\GoruntuIslemeOgreniyorum\Herhangi_bir_yuz_tanima\yuzCascade.xml')

if face_cascade.empty():
    print("Haar Cascade dosyası yüklenemedi!")
    exit()

# Kamerayı başlatıyorum
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        print("Kameradan görüntü alınamadı!")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Yuz Tanima', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
