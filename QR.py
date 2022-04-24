import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

listofdata = []

# enter file name to check the data


print('~~~~~~~"WELCOME TO QUICK-SCAN"~~~~~~~')
choice = 1
while (choice != "E" or choice != "e"):
    print('"I"==> TO INSPECT')
    print('"R"==> TO REGISTER THE DATA')
    print('"E"==> TO EXIT')
    choice = input('ENTER YOUR CHOICE : ')
    if choice == "I" or choice == "i":
        f = open("dataofQR.txt", "r+")
        mydatalist = f.read().splitlines()
        count1 = 0
        key1 = int(input('enter no of scans:'))

        while True:
            if count1 >= key1:
                break
            success, img = cap.read()
            for barcode in decode(img):

                    myData = barcode.data.decode('utf-8')
                    print('The scaned data is:')
                    print(myData)
                    count1 = count1+1


                    if myData in mydatalist:
                        print('valid')
                    else:
                        print('invalid')


                    pts = np.array([barcode.polygon],np.int32)
                    pts = pts.reshape((-1,1,2))
                    cv2.polylines(img,[pts],True,(171,130,255),5)
                    pts2 = barcode.rect
                    cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)


            cv2.imshow('Resultcam',img)
            cv2.waitKey(1)

    elif choice == "R" or choice == "r":
        f = open("dataofQR.txt", "r+")
        mydatalist = f.read().splitlines()
        count2 = 0
        key2 = int(input('enter no of scans:'))

        while True:
            if count2 >= key2:
                break

            success, img = cap.read()

            for barcode in decode(img):

                wrData = barcode.data.decode('utf-8')
                print('The scaned data is:')
                print(wrData)
                
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (132,112,255), 5)
                if wrData not in listofdata:
                    listofdata.append(wrData)
                    f.writelines(wrData +'\n')
                    count2 = count2+1

            cv2.imshow('Resultwcam', img)
            cv2.waitKey(1)
        f.close()
    else :
        print("~~~~~INVALID CHOICE~~~~~")
        print('PLEASE ENTER "I" OR "R" OR "E" \n\n\n')
