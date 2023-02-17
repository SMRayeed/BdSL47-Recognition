# -*- coding: utf-8 -*-


import cv2
import mediapipe as mp
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#D:\test
#output_folder = "E:\\BSL Kaggle\\BSL Dataset\\36\\Output"
output_folder = "E:\\x\\Output"
directory_path = output_folder
if not os.path.exists(directory_path):
    os.mkdir(directory_path)

import csv

file_type = ".csv"
csv_filename = output_folder + file_type
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Single Image Frame', 
                     'x00', 'y00', 'z00',
                     'x01', 'y01', 'z01',
                     'x02', 'y02', 'z02',
                     'x03', 'y03', 'z03',
                     'x04', 'y04', 'z04',
                     'x05', 'y05', 'z05',
                     'x06', 'y06', 'z06',
                     'x07', 'y07', 'z07',
                     'x08', 'y08', 'z08',
                     'x09', 'y09', 'z09',
                     'x10', 'y10', 'z10',
                     'x11', 'y11', 'z11',
                     'x12', 'y12', 'z12',
                     'x13', 'y13', 'z13',
                     'x14', 'y14', 'z14',
                     'x15', 'y15', 'z15',
                     'x16', 'y16', 'z16',
                     'x17', 'y17', 'z17',
                     'x18', 'y18', 'z18',
                     'x19', 'y19', 'z19',
                     'x20', 'y20', 'z20', 'Label'])
                     
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5)

filelist = [] 
fileDirectory = "E://x//"
imageFileType = ".jpg"
fileName = ""

for i in range(1, 101):
  #i = (str(i).zfill(3))
  fileName = fileDirectory + "x ("+ str(i) +")" + imageFileType 
  filelist.append(fileName)
  

for idx, files in enumerate(filelist):
    image = cv2.flip(cv2.imread(files), 1)
    
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    print('Handedness:', results.multi_handedness)
    
    if not results.multi_hand_landmarks :
        continue
    
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()

    
    for hand_landmarks in results.multi_hand_landmarks:
        
        with open(csv_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([files,
                             hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y, hand_landmarks.landmark[0].z,
                             hand_landmarks.landmark[1].x, hand_landmarks.landmark[1].y, hand_landmarks.landmark[1].z,
                             hand_landmarks.landmark[2].x, hand_landmarks.landmark[2].y, hand_landmarks.landmark[2].z,
                             hand_landmarks.landmark[3].x, hand_landmarks.landmark[3].y, hand_landmarks.landmark[3].z,
                             hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y, hand_landmarks.landmark[4].z,
                             hand_landmarks.landmark[5].x, hand_landmarks.landmark[5].y, hand_landmarks.landmark[5].z,
                             hand_landmarks.landmark[6].x, hand_landmarks.landmark[6].y, hand_landmarks.landmark[6].z,
                             hand_landmarks.landmark[7].x, hand_landmarks.landmark[7].y, hand_landmarks.landmark[7].z,
                             hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y, hand_landmarks.landmark[8].z,
                             hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y, hand_landmarks.landmark[9].z,
                             hand_landmarks.landmark[10].x, hand_landmarks.landmark[10].y, hand_landmarks.landmark[10].z,
                             hand_landmarks.landmark[11].x, hand_landmarks.landmark[11].y, hand_landmarks.landmark[11].z,
                             hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y, hand_landmarks.landmark[12].z,
                             hand_landmarks.landmark[13].x, hand_landmarks.landmark[13].y, hand_landmarks.landmark[13].z,
                             hand_landmarks.landmark[14].x, hand_landmarks.landmark[14].y, hand_landmarks.landmark[14].z,
                             hand_landmarks.landmark[15].x, hand_landmarks.landmark[15].y, hand_landmarks.landmark[15].z,
                             hand_landmarks.landmark[16].x, hand_landmarks.landmark[16].y, hand_landmarks.landmark[16].z,
                             hand_landmarks.landmark[17].x, hand_landmarks.landmark[17].y, hand_landmarks.landmark[17].z,
                             hand_landmarks.landmark[18].x, hand_landmarks.landmark[18].y, hand_landmarks.landmark[18].z,
                             hand_landmarks.landmark[19].x, hand_landmarks.landmark[19].y, hand_landmarks.landmark[19].z,
                             hand_landmarks.landmark[20].x, hand_landmarks.landmark[20].y, hand_landmarks.landmark[20].z, 
                             9])

        print('Hand Keypoints :', hand_landmarks)

        print(
            f'Index finger tip coordinates: (',
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
        )
        mp_drawing.draw_landmarks(annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    cv2.imwrite(os.path.join(directory_path , 'Output Image -' + str(idx+1) + '.jpg'), cv2.flip(annotated_image, 1))

hands.close()