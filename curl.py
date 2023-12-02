import cv2   #cv2.__version__ = 4.8.1
import mediapipe as mp  #mp.__version__ = 0.10.8
import numpy as np  #np.__version__ = 1.24.4
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# VIDEO FEED
# Make Detections
"""
cap = cv2.VideoCapture(0) #open webcam

# setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose: #Pose accesing our pose estimation model, confidence = acuracy rate

    while cap.isOpened():
        ret, frame = cap.read()  #read our frame
        frame = cv2.flip(frame,1)
        # default opencv format of bgr
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # pass image to mediapipe we want our image to be in the format rgb 
        image.flags.writeable = False 
        
        # Make detection

        results = pose.process(image) #using pose
        
        # Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66),thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,66,230),thickness=2, circle_radius=2)
                                  ) # easily draw landmarks, second parameter give all different landmarks.  third parameters connection, fourth parameter bones  
        # print(results.pose_landmarks)
        # print(mp_pose.POSE_CONNECTIONS)


        # print(results)

        cv2.imshow("Mediapipe Feed", image) #show frame

        if cv2.waitKey(10) & 0XFF == ord('q'):  # input q from keyboard close window and quit loop
            break

    cap.release()
    cv2.destroyAllWindows()

"""

#

"""
cap = cv2.VideoCapture(0) #open webcam

# setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose: #Pose accesing our pose estimation model, confidence = acuracy rate

    while cap.isOpened():
        ret, frame = cap.read()  #read our frame
        frame = cv2.flip(frame,1)
        # default opencv format of bgr
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # pass image to mediapipe we want our image to be in the format rgb 
        image.flags.writeable = False 
        
        # Make detection

        results = pose.process(image) #using pose
        
        # Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 

        # Extract Landmarks

        try:
            landmarks = results.pose_landmarks.landmark  # give us our actual landmarks  len(landmarks) = 33 0..32 all body points. we can use this points
            # print(landmarks)

            # Get cordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        
            # Calculate angle 
            angle = calculate_angle(shoulder, elbow, wrist)

            # Visualize
            cv2.putText(image,str(angle),
                        tuple(np.multiply(elbow, [640, 480]).astype(int)),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2, cv2.LINE_AA
                                    )

        except:
            pass


        # for lndmrk in mp_pose.PoseLandmark:
        #     print(lndmrk)
       
        # print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])
        # print(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value])
        # print(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
       
        # print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER])
        # print(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW])
        # print(landmarks[mp_pose.PoseLandmark.LEFT_WRIST])
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66),thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,66,230),thickness=2, circle_radius=2)
                                  ) # easily draw landmarks, second parameter give all different landmarks.  third parameters connection, fourth parameter bones  
        # print(results.pose_landmarks)
        # print(mp_pose.POSE_CONNECTIONS)


        def calculate_angle(a,b,c):  # 11 13 15 points shoulder elbow wrist
            a = np.array(a) # first
            b = np.array(b) # mid
            c = np.array(c) # end points 

            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0]) 
            angle = np.abs(radians*180.0/np.pi)  # calculate our radians for pur particular joint and angle 
            
            if angle > 180.0:
                angle = 360 - angle

            return angle

        # print(shoulder)
        # print(results)

        print(calculate_angle(shoulder, elbow, wrist))
        

        cv2.imshow("Mediapipe Feed", image) #show frame

        if cv2.waitKey(10) & 0XFF == ord('q'):  # input q from keyboard close window and quit loop
            break

    cap.release()
    cv2.destroyAllWindows()

"""



cap = cv2.VideoCapture(0) #open webcam

# curl counter
counter = 0
stage = None

# setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose: #Pose accesing our pose estimation model, confidence = acuracy rate

    while cap.isOpened():
        ret, frame = cap.read()  #read our frame
        frame = cv2.flip(frame,1)
        # default opencv format of bgr
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # pass image to mediapipe we want our image to be in the format rgb 
        image.flags.writeable = False 
        
        # Make detection

        results = pose.process(image) #using pose
        
        # Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 

        # Extract Landmarks

        try:
            landmarks = results.pose_landmarks.landmark  # give us our actual landmarks  len(landmarks) = 33 0..32 all body points. we can use this points
            # print(landmarks)

            # Get cordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        
            # Calculate angle 
            angle = calculate_angle(shoulder, elbow, wrist)

            # Visualize
            cv2.putText(image,str(angle),
                        tuple(np.multiply(elbow, [640, 480]).astype(int)),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2, cv2.LINE_AA
                                    )

            # Curl counter logic
            if angle > 160:
                stage = "down"
            if angle < 30 and stage == "down":
                stage = "up"
                counter += 1
                print(counter)

        except:
            pass


        # Render Curl Counter
        # Setup status box
        cv2.rectangle(image, (0,0), (255,73), (245,117,16), -1)  #2-start points, 3-end points, 4-rectangle colors, -1 fill in  

        # Rep data
        cv2.putText(image, 'REPS', (15,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        
        cv2.putText(image, str(counter), (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

        # STAGE data
        cv2.putText(image, 'STAGE', (65,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        
        cv2.putText(image, stage, (60,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
       
       
        # for lndmrk in mp_pose.PoseLandmark:
        #     print(lndmrk)
       
        # print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])
       
        # print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER])

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66),thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,66,230),thickness=2, circle_radius=2)
                                  ) # easily draw landmarks, second parameter give all different landmarks.  third parameters connection, fourth parameter bones  
        # print(results.pose_landmarks)
        # print(mp_pose.POSE_CONNECTIONS)


        def calculate_angle(a,b,c):  # 11 13 15 points shoulder elbow wrist
            a = np.array(a) # first
            b = np.array(b) # mid
            c = np.array(c) # end points 

            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0]) 
            angle = np.abs(radians*180.0/np.pi)  # calculate our radians for pur particular joint and angle 
            
            if angle > 180.0:
                angle = 360 - angle

            return angle

        # print(shoulder)
        # print(results)
        

        cv2.imshow("Mediapipe Feed", image) #show frame

        if cv2.waitKey(10) & 0XFF == ord('q'):  # input q from keyboard close window and quit loop
            break

    cap.release()
    cv2.destroyAllWindows()
