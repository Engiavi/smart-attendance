import cv2
import pyzbar.pyzbar as pyzbar
img=cv2.imread('avi.png')
wbcam=cv2.VideoCapture(0)
"""decodeob=pyzbar.decode(img)
    #print( decodeob)

    for obj in decodeob:
        print("Data:",obj.data)"""


while True:
        _,frame=wbcam.read()
        cv2.imshow("Frame",frame)

        decodeob=pyzbar.decode(frame)
       # print( decodeob)

        for obj in decodeob:
           # print(obj.data.decode('utf-8'))
            if(obj)>=1:
                import webbrowser
                webbrowser.open(obj.data.decode('utf-8'))
        
        key=cv2.waitKey(1)
        if key=='g':
            break
