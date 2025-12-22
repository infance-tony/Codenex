import cv2
# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image (or capture from video)
image = cv2.imread('test.jpg')
# Or for video:
# cap = cv2.VideoCapture('path_to_your_video.mp4')

# Resize the image to new dimensions
new_width = 500
new_height = 500
image = cv2.resize(image, (new_width, new_height))

# Convert the image to grayscale (Haar cascade works better with grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces and count them
count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    count += 1

# Display the resulting image
cv2.imshow('Detected Heads', image)
print(f"Number of heads detected: {count}")

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
