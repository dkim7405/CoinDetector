import cv2
import numpy as np

class DetectCoin:

    def __init__(self, imagePath):
        self.windowName = "Detected"
        cv2.namedWindow(self.windowName, cv2.WINDOW_AUTOSIZE)
        self.useImage = cv2.imread(imagePath)
        self.finalImage = self.useImage.copy()
        self.originalImage = self.useImage.copy()

    def displayOriginal(self):
        cv2.imshow("Original", self.originalImage)

    def displayResult(self):
        cv2.imshow(self.windowName, self.finalImage)

    def detectCoin(self):
        self.preprocessImage()
        self.detectAndDrawCoins()
        self.displayResult()

    def preprocessImage(self):
        self.useImage = cv2.cvtColor(self.useImage, cv2.COLOR_BGR2GRAY)
        self.useImage = cv2.medianBlur(self.useImage, 5)
        self.useImage = self.thresholdImage(self.useImage, 140)
        cv2.imshow("Thresholded", self.useImage)
        self.useImage = self.detectHolesFromCoin(self.useImage)

    def detectAndDrawCoins(self):
        keypoints = self.detectCoinsUsingBlob()
        self.finalImage = self.drawCirclesForKeypoints(self.finalImage, keypoints)
        self.displayNumberOfCoins(len(keypoints))

    def detectCoinsUsingBlob(self):
        blobDetectorParams = cv2.SimpleBlobDetector_Params()
        blobDetectorParams.filterByCircularity = True
        blobDetectorParams.minCircularity = 0.4
        blobDetectorParams.maxCircularity = 1.0
        blobDetectorParams.filterByArea = False
        blobDetectorParams.filterByConvexity = False
        blobDetectorParams.filterByInertia = False
        blobDetectorParams.filterByColor = True
        blobDetectorParams.blobColor = 255

        blobDetector = cv2.SimpleBlobDetector_create(blobDetectorParams)
        return blobDetector.detect(self.useImage)

    def drawCirclesForKeypoints(self, imageToDrawCircles, keypoints):
        for keypoint in keypoints:
            x = int(keypoint.pt[0])
            y = int(keypoint.pt[1])
            r = int(keypoint.size / 2)
            cv2.circle(imageToDrawCircles, (x, y), r, (0, 0, 255), 3)
        return imageToDrawCircles

    def displayNumberOfCoins(self, numberOfCoins):
        textToDisplay = "Number of Coins: " + str(numberOfCoins)
        cv2.putText(self.finalImage, textToDisplay, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    def detectHolesFromCoin(self, imageToDetectHoles):
        simpleBlobDetector = cv2.SimpleBlobDetector_create()
        keypoints = simpleBlobDetector.detect(imageToDetectHoles)

        for keypoint in keypoints:
            x = int(keypoint.pt[0])
            y = int(keypoint.pt[1])
            r = int(keypoint.size / 2)
            cv2.circle(imageToDetectHoles, (x, y), r, (255, 255, 255), -1)

        return imageToDetectHoles

    def thresholdImage(self, imageToThreshold, thresholdValue):
        tV, threshedImg = cv2.threshold(imageToThreshold, thresholdValue, 255, cv2.THRESH_BINARY_INV)
        kernel1 = np.ones((5, 5), np.uint8)
        kernel2 = np.ones((3, 3), np.uint8)
        threshedImg = cv2.dilate(threshedImg, kernel1, iterations=1)
        threshedImg = cv2.dilate(threshedImg, kernel2, iterations=4)
        threshedImg = cv2.erode(threshedImg, kernel1, iterations=1)
        threshedImg = cv2.erode(threshedImg, kernel2, iterations=4)
        return threshedImg

if __name__ == "__main__":
    dc = DetectCoin("images/image.png")
    dc.detectCoin()
    dc.displayOriginal()

    while True:
        if cv2.waitKey(0):
            break