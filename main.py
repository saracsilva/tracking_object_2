import cv2

# Getting the background
background = cv2.imread("background.png")
# Transform the background to grayscale and blur it
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
background = cv2.GaussianBlur(background, (21,21),0)

video = cv2.VideoCapture("Different_Bouncing_Ball_References.mp4")

while True:
    status, frame = video.read()
    # Transform the video to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)


    #The difference between the background and the gray frame
    diff = cv2.absdiff(background, gray)
    #remove the noise part of the frame
    thresh = cv2.threshold(diff, 30,255,cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts, res = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #draw a contour
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        #draw the contour
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("All contours", frame)
    #cv2.imshow("Thresh Video", thresh)
    #cv2.imshow("Diff Video", diff)
    #cv2.imshow("Gray Video", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()