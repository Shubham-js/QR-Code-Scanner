import cv2
from pyzbar.pyzbar import decode
#telling python to capture viceo feed from default camera as 0 is passed in arguement.
capture = cv2.VideoCapture(0)
recieved = None
while True:
    _, frame=capture.read()

    #grab the frame and if there is a QR code then decode it
    decoded_data=decode(frame)
    try:
        data = decoded_data[0][0]
        if(data!=recieved):
            print(data)
            recieved=data
    except:
        pass
    cv2.imshow('Shubham Scanner', frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break





