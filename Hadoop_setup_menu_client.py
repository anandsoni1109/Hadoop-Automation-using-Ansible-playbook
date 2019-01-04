
# coding: utf-8

# In[ ]:



def speak(x):
    import speech_recognition as sr
    import pyttsx3
    import pyaudio
    engine=pyttsx3.init()
    engine.say(x)
    engine.runAndWait()


# In[ ]:


def recog():
    import speech_recognition as sr
    import pyttsx3    import pyaudio
    mic=sr.Microphone()
    rec=sr.Recognizer()
    with mic as source:
        print("say:")
        audio=rec.listen(source)
        text=rec.recognize_google(audio)
        return(text)


# In[ ]:


def send(cmd):
    import subprocess as sp
    import socket
    s=socket.socket()
    s.connect(("192.168.43.112",1235))
    s.send(cmd)


# In[ ]:



    


# In[ ]:





# In[ ]:


# capturing image for face learning(can be removed if already done)
import cv2
import numpy as np

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

# Initialize Webcam
cap = cv2.VideoCapture(0)
count = 0

# Collect 100 samples of your face from webcam input
while True:

    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Save file in specified directory with unique name
        file_name_path = 'E://faces3//user' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count == 200: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")


# In[ ]:


def login():
    import time
    b=[]
    ii=1
    while ii <=3:
        import cv2
        import numpy as np
        from os import listdir
        from os.path import isfile, join
        print(cv2.__version__)
        # Get the training data we previously made
        data_path = 'e://faces{}//'.format(ii)
        # a=listdir('d:/faces')
        # print(a)
        # """
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

        # Create arrays for training data and labels
        Training_Data, Labels = [], []

        # Open training images in our datapath
        # Create a numpy array for training data
        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)
        # 
        # Create a numpy array for both training data and labels
        Labels = np.asarray(Labels, dtype=np.int32)
        model=cv2.face_LBPHFaceRecognizer.create()
        # Initialize facial recognizer
        # model = cv2.face_LBPHFaceRecognizer.create()
        # model=cv2.f
        # NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

        # Let's train our model 
        model.train(np.asarray(Training_Data), np.asarray(Labels))

        if(ii==3):
            print('vivek please come in front of webcam for unlocking process')
            speak('vivek please come in front of webcam for Unlocking process')

        if(ii==2):
            print('Neha please come in front of webcam for unlocking process')
            speak(' Neha please come in front of webcam for Unlocking process')
        if(ii==1):
            print('Anand please come in front of webcam for face recognition')
            speak('Anand please come in front of webcam for Unlocking process')
        time.sleep(2)



        import cv2
        import numpy as np
        import webbrowser


        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        def face_detector(img, size=0.5):

            # Convert image to grayscale
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            if faces is ():
                return img, []

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                roi = img[y:y+h, x:x+w]
                roi = cv2.resize(roi, (200, 200))
            return img, roi


        # Open Webcam
        cap = cv2.VideoCapture(0)

        while True:

            ret, frame = cap.read()

            image, face = face_detector(frame)

            try:
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                # Pass face to prediction model
                # "results" comprises of a tuple containing the label and the confidence value
                results = model.predict(face)
                print(results)
                if results[1] < 500:
                    confidence = int( 100 * (1 - (results[1])/400) )
                    display_string = str(confidence) + '% Confident it is User'

                cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)

                if confidence > 75:
                    cv2.imshow('Face Recognition', image )
                    #webbrowser.open('')
                    b.append('y')
                    break
                else:
                    cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                    cv2.imshow('Face Recognition', image )

            except:
                cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.imshow('Face Recognition', image )
                pass

            if cv2.waitKey(1) == 13: #13 is the Enter Key
                break
        ii=ii+1
        cap.release()
        cv2.destroyAllWindows()

    print('Synergy Found')
    speak("you are successfully login in your tool")
    return(1)


# In[ ]:


def ping(a):
    import subprocess
    b=[]
    j=0
    for i in a:
        ping = subprocess.getstatusoutput('ping {} -n 2 '.format(a[j][0]))
        if ping[0] == 0:
            b.append(i)
        else :
            print("{} ip is not reachable . Do you still want to add this y/n".format(a[j][0]))
            speak("{} ip is not reachable . Do you still want to add this y/n".format(a[j][0]))
            kuch=input('')
            if kuch == 'y':
                b.append(i)
            else:
                pass
        j=j+1
    return(b)


# In[ ]:


import subprocess as sp
import socket
s=socket.socket()
import pickle
import getpass
import time
print("                    welcome to crontab                     ")
speak('welcome to crontab')
print("you can either login by password , or by your face image")
speak("you can either login by password , or by your face image")
print("tell system how you want to login")
speak("tell system how you want to login")
passwd='hello'
a=input('')
print(a)
print()
i=3
check=0
while i>0:
    i=i-1
    if 'password' in a:
        speak("enter your password")
        in_pass=getpass.getpass("enter your password")
        if in_pass==passwd:
            check=1
            speak('Hello anand how may i help you')

            break
        else:
            if i==0 : 
                print("shutting down .....")
                speak("you are not allowed to login")
                sendb('init 0')
            if i!=0 :
                print("please try again , you have only {} chance left".format(i))
                speak("please try again , you have only {} chance left".format(i))
    elif 'face' in a :
        b=login()
        i=0
        check=1
        break
    else:
        print('pardon please')
        speak('pardon please')
        a=input('')


if check==1:
    print("Here is the list of task system can perform")
    print("""
    1. Start HADOOP HDFS Cluster.
    2. Start HADOOP M-R Cluster.
    3. Setup NameNode (Master).
    4. Setup Data Nodes.
    5. Setup Job Tracker. 
    6. Setup Task Trackers.
    7. RESET HADOOP CLUSTERS.
    8. EXIT.
    """)
    namenodeon=0
    jton=0
 
    
    while True:
        print('choose what you want to do')
        speak('choose what you want to perform out of following')
        what_to_do=input('')
        print(what_to_do)
        ips=[]
        
        if '1' in what_to_do or 'one' in what_to_do:
            if namenodeon==1 :
                send('1'.encode())
            else :
                print("first setup hadoop master")
            
            
        if '2' in what_to_do or 'two' in what_to_do:
            if jton==1 :
                
                send('2'.encode())
            else :
                print("first setup hadoop master")
            
        
        
        if '3' in what_to_do or 'three' in what_to_do or 'third' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as master ')
            speak('please provide us with ip and password of system you want to add as master ')
            print('Enter your ip:')
            ip_firsttime=input('')
            ip_password=getpass.getpass("enter your password")
            extra.append(ip_firsttime)
            extra.append(ip_password)
            ips.append(extra)
            final_ips=ping(ips)
            namenodeon=1
            print(final_ips)
            send(b'3')
            
            send(pickle.dumps(final_ips))
        
        
        if '4' in what_to_do or 'four' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as slave ')
            speak('please provide us with ip and password of system you want to add as slave ')
            print('Enter your ip:')
            while True:
                print("enter ip and password of slave you want to add")
                ip_firsttime=input('')
                ip_password=getpass.getpass("enter your password")
                extra.append(ip_firsttime)
                extra.append(ip_password)
                ips.append(extra)
                extra=[]
                print("Do you want to add more slave y/n")
                speak("Do you want to add more slave")
                add_more_slave=input('')
                if add_more_slave=='y':
                    pass
                elif add_more_slave=='n':
                    break
                
            final_ips=ping(ips)
            print(final_ips)
            
            send(b'4')
        
            send(pickle.dumps(final_ips))
            
        if '5' in what_to_do or 'five' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as job tracker ')
            speak('please provide us with ip and password of system you want to add as job tracker ')
            print('Enter your ip:')
            ip_firsttime=input('')
            ip_password=getpass.getpass("enter your password")
            extra.append(ip_firsttime)
            extra.append(ip_password)
            ips.append(extra)
            jton=1
            final_ips=ping(ips)
            print(final_ips)
            
            send(b'5')
            time.sleep(0.5)
            send(pickle.dumps(final_ips))
        
        if '6' in what_to_do or 'six' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as task tracker ')
            speak('please provide us with ip and password of system you want to add as task tracker ')
            print('Enter your ip:')
            while True:
                print("enter ip and password of task tracker you want to add")
                ip_firsttime=input('')
                ip_password=getpass.getpass("enter your password")
                extra.append(ip_firsttime)
                extra.append(ip_password)
                ips.append(extra)
                extra=[]
                print("Do you want to add more task tracker y/n")
                speak("Do you want to add more task tracker")
                add_more_slave=input('')
                if add_more_slave=='y':
                    pass
                elif add_more_slave=='n':
                    break
                
            final_ips=ping(ips)
            print(final_ips)
            send(b'6')
            send(pickle.dumps(final_ips))
            
            
        if '7' in what_to_do or 'seven' in what_to_do:
            send(b'7')    
            
        if '8' in what_to_do or 'eight' in what_to_do:
            break
            
        
            


# In[ ]:




