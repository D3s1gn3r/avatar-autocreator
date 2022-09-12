import cv2
import sys
from os.path import exists


if __name__ == '__main__':
    if len(sys.argv) > 2 and exists(sys.argv[1]):
        imageName = sys.argv[1]
        imageAvatarName = sys.argv[2]

        # image data
        img = cv2.imread(imageName)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgHeight, imgWidth, _ = img.shape

        # dataset
        faces = cv2.CascadeClassifier('haarcascade_faces.xml')

        # founded faces
        results = faces.detectMultiScale(grayImg, scaleFactor=1.4, minNeighbors=1)
        if (len(results)):
            results = [results[0]]

            for (x, y, w, h) in results:
                rectangeResizeX = round(w*0.35)
                rectangeResizeY = round(h*0.75)

                if x - rectangeResizeX < 0:
                    x1 = 0
                else:
                    x1 = x - rectangeResizeX

                if x + w + rectangeResizeX > imgWidth:
                    x2 = imgWidth
                else:
                    x2 = x + w + rectangeResizeX

                if y - rectangeResizeY < 0:
                    y1 = 0
                else:
                    y1 = y-rectangeResizeY

                if y + h + rectangeResizeY > imgHeight:
                    y2 = imgHeight
                else:
                    y2 = y + h + rectangeResizeY


                crop = img[y1:y2, x1:x2]
                cv2.imwrite(imageAvatarName, crop)
