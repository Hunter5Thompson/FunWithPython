import cv2

# Erstelle VideoCapture-Objekt, um das Video von der Webcam abzugreifen
cap = cv2.VideoCapture(0)

# Schleife, die das Video in Echtzeit darstellt
while True:
    # Lese das nächste Frame aus dem Video ab
    ret, frame = cap.read()

    # Überprüfe, ob das Frame korrekt eingelesen wurde
    if not ret:
        break

    # Zeige das Frame in einem Fenster namens "Video" an
    cv2.imshow('Video', frame)

    # Warte auf die Eingabe einer Taste (hier: 1 Millisekunde)
    # Um das Fenster zu schließen, drücke "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Beende die Schleife und gebe die Ressourcen frei
cap.release()
cv2.destroyAllWindows()
