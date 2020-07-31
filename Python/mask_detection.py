import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2

video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

np.set_printoptions(suppress=True)
labels = {
    0 : "mask",
    1 : "no mask"
    }

model = tensorflow.keras.models.load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

try:
    while True:
    
            check,frame = video.read()
            cv2.imwrite("test_photo.jpg",frame)
            image = Image.open('test_photo.jpg')
            #print("frame:\n",frame)
            #print("image:\n",image)

            face = cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 6)
            #print(face)
        
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)
    
            image_array = np.asarray(image)

            #image.show()

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array
            #print("normalized arrray:\n",normalized_image_array)
            #print("data:\n",data[0])

            #if prediction[0][0] > prediction[0][1]:
            #    print("mask")
            #else:
            #    print("No mask")
            

            for x,y,w,h in face:
                
                prediction = model.predict(data)
                ID = np.argmax(prediction)
                
                frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) if ID == 0 else (0,0,255))
                cv2.putText(frame,labels[ID],(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX ,1, (0,255,0) if ID == 0 else (0,0,255), 2, cv2.LINE_AA )

                print("%s:%.2f"%(labels[ID],np.max(prediction)*100))
                
            cv2.imshow("Video",frame)
           # print("mask:%.2f\nno mask:%.2f\n"%(prediction[0][0]*100,prediction[0][1]*100))
            
            key = cv2.waitKey(1)
            if(key == ord('q')):
                print("Exiting...")
                break
finally:
    video.release()
    cv2.destroyAllWindows()

