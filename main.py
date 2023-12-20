from cvzone.HandTrackingModule import HandDetector
import cv2
import random
import cvzone
import time


# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Initiate game class with constructor, random point location and update functions
class reactionGameClass:
    def __init__(self, pathCheckPoint):
        self.points = []
        self.imgCheckPoint = cv2.imread(pathCheckPoint, cv2.IMREAD_UNCHANGED)
        self.hCheckpoint, self.wCheckPoint, _ = self.imgCheckPoint.shape
        self.checkPoint = 0, 0
        self.randomCheckPointLocation()
        self.score = 0
        
    def randomCheckPointLocation(self):
        self.checkPoint = random.randint(100, 1000), random.randint(200, 400) #random x and y points

    def update(self, imgMain, currentHead):
        cx, cy = currentHead
        self.points.append([cx, cy])
        rx,ry = self.checkPoint

        # Check if current point (index finger) within the check point (apple) area, i.e. touched the apple
        if rx - self.wCheckPoint // 2 < cx < rx + self.wCheckPoint // 2 and \
                ry - self.hCheckpoint // 2 < cy < ry + self.hCheckpoint//2: 
            self.randomCheckPointLocation() # Update the check point location
            self.score += 1 # Increment the scoreboard 

        if self.points:
            cv2.circle(imgMain, self.points[-1], 20, (0, 255, 0), cv2.FILLED) # Draw circle on current points (index finger)

        imgMain = cvzone.overlayPNG(imgMain, self.imgCheckPoint, (rx - self.wCheckPoint // 2, ry - self.hCheckpoint // 2, 
                                                                  rx - self.wCheckPoint // 2, ry + self.hCheckpoint // 2)) # Draw check point (apple)
        return imgMain
            

game = reactionGameClass("apple.png")
max_time = 10 # Set max time
start_time = time.time()

# Continuously get frames from the webcam
while True:
    curr_time = time.time() - start_time if time.time() - start_time < max_time else max_time
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img = cv2.flip(img, 1) # Mirror the image because otherwise its flipped and difficult to play
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=False, flipType=True)

    # Check if any hands are detected and if timer is not finished
    if hands and curr_time < max_time: 
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        pointIndex1 = lmList1[8][0:2] # Get index finger points
        img = game.update(img, pointIndex1) # Update the game with index finger points

        if len(hands) == 2:
            # Information for the second hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            pointIndex2 = lmList2[8][0:2] # Get index finger points
            img = game.update(img, pointIndex2) # Update the game with index finger points

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    key = cv2.waitKey(1)

    if key == ord('q'): # Quit game
        break

    if curr_time == max_time:
        cvzone.putTextRect(img, f"Game Over", [500, 350], scale = 3, thickness = 3, offset = 10, colorR = (0, 0, 255)) # Display text once timer is done
        if key == ord('r'): # Restart game 
            start_time = time.time()
            curr_time = 0
            game.score = 0

    cvzone.putTextRect(img, f"Score: {game.score}", [50, 80], scale = 3, thickness = 3, offset = 10, colorR = (0, 255, 0)) # Display score
    cvzone.putTextRect(img, f"Timer: {max_time - int(curr_time)}", [50, 160], scale = 3, thickness = 3, offset = 10, colorR = (0, 255, 0)) # Display timer

    # Display the image in a window
    cv2.imshow("Image", img)
    

cap.release()
cv2.destroyAllWindows()