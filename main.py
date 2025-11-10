# main.py
###pip install opencv-contrib-python
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
from camera import VideoCamera
from camera2 import VideoCamera2
import os
import base64
import mysql.connector
import hashlib
import datetime
from datetime import date
import cv2
import numpy as np
import time
from random import seed
from random import randint
import shutil
import imagehash
import PIL.Image
from PIL import Image
from PIL import ImageTk
import stepic
import urllib.request
import urllib.parse
from urllib.request import urlopen
import webbrowser

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  charset="utf8",
  database="smart_parking_face"

)
app = Flask(__name__)
##session key
app.secret_key = 'abcdef'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=""

    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ev_register WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname

            cursor.execute('SELECT * FROM ev_register WHERE uname = %s', (uname, ))
            dd = cursor.fetchone()
            ff=open("name.txt","w")
            ff.write(dd[1])
            ff.close()
        
            return redirect(url_for('userhome'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html',msg=msg)

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    msg=""

    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ev_station WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password! or access not provided'
    return render_template('login2.html',msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT max(id)+1 FROM ev_register")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    
        
    if request.method=='POST':
        address=request.form['address']
        name=request.form['name']
        mobile=request.form['mobile']
        email=request.form['email']
        account=request.form['account']
        card=request.form['card']
        bank=request.form['bank']
        uname=request.form['uname']
        pass1=request.form['pass']

        cursor = mydb.cursor()
        sql = "INSERT INTO ev_register(id,name,address,mobile,email,account,card,bank,amount,uname,pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        val = (maxid,name,address,mobile,email,account,card,bank,'10000',uname,pass1)
        cursor.execute(sql, val)
        mydb.commit()            
        print(cursor.rowcount, "Registered Success")
        msg="sucess"
        return redirect(url_for('login'))

    return render_template('register.html',msg=msg)

@app.route('/reg_station', methods=['GET', 'POST'])
def reg_station():
    msg=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT max(id)+1 FROM ev_station")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    
        
    if request.method=='POST':
        stype=request.form['stype']
        name=request.form['name']
        area=request.form['area']
        city=request.form['city']
        lat=request.form['lat']
        lon=request.form['lon']
        uname=request.form['uname']
        pass1=request.form['pass']

        cursor = mydb.cursor()
        sql = "INSERT INTO ev_station(id,name,stype,num_charger,area,city,lat,lon,uname,pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        val = (maxid,name,stype,'10',area,city,lat,lon,uname,pass1)
        cursor.execute(sql, val)
        mydb.commit()            
        print(cursor.rowcount, "Registered Success")
        msg="sucess"
        return redirect(url_for('login2'))

    return render_template('reg_station.html',msg=msg)

@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    msg=""
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_register where uname=%s",(uname, ))
    data= cursor.fetchone()
    return render_template('userhome.html',msg=msg, data=data, uname=uname)

@app.route('/station', methods=['GET', 'POST'])
def station():
    msg=""
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station")
    data= cursor.fetchall()
    return render_template('station.html',msg=msg, data=data, uname=uname)

@app.route('/slot', methods=['GET', 'POST'])
def slot():
    msg=""
    ff=open("C:/wamp/www/parking/log.txt",'w')
    ff.write("")
    ff.close()
    act=""
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    s7=0
    s8=0
    s9=0
    s10=0
    if 'username' in session:
        uname = session['username']
    #if request.method=='GET':
    sid=request.args.get('sid')

    ff=open("mess.txt","r")
    st=ff.read()
    ff.close()
        
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where id=%s",(sid, ))
    dd= cursor.fetchone()
    station=dd[1]
    cursor.execute("SELECT * FROM ev_booking where station=%s and status=1",(sid, ))
    data= cursor.fetchall()

    for nn in data:
        if nn[5]==1:
            s1=1
        if nn[5]==2:
            s2=2
        if nn[5]==3:
            s3=3
        if nn[5]==4:
            s4=4
        if nn[5]==5:
            s5=5
        if nn[5]==6:
            s6=6
        if nn[5]==7:
            s7=7
        if nn[5]==8:
            s8=8
        if nn[5]==9:
            s9=9
        if nn[5]==10:
            s10=10
        
        
    
    act="ok"
    return render_template('slot.html',msg=msg,uname=uname,sid=sid,station=station,act=act,data=data,s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6,s7=s7,s8=s8,s9=s9,s10=s10)


@app.route('/select', methods=['GET', 'POST'])
def select():
    if 'username' in session:
        uname = session['username']
    sid=request.args.get('sid')
    rid=request.args.get('rid')
    if request.method=='POST':
        plan=request.form['plan']
        cursor = mydb.cursor()
        cursor.execute("update ev_booking set plan=%s,charge_st=1,charge_min=0,charge_sec=0 where id=%s",(plan, rid))
        mydb.commit()
        return redirect(url_for('slot',sid=sid))
        
    return render_template('select.html',sid=sid,rid=rid)


@app.route('/book', methods=['GET', 'POST'])
def book():
    msg=""
    act=""
    vid=""
    if 'username' in session:
        uname = session['username']
    sid=request.args.get('sid')
    slot=request.args.get('slot')
        
    #if request.method=='GET':
        #sid=request.args.get('sid')
        #slot=request.args.get('slot')
        
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where id=%s",(sid, ))
    dd= cursor.fetchone()
    station=dd[1]

    #cursor.execute("SELECT * FROM ev_booking where station=%s and status=1",(sid, ))
    #data= cursor.fetchall()
    
    if request.method=='POST':
        carno=request.form['carno']
        reserve=request.form['reserve']
        sid=request.form['sid']
        slot=request.form['slot']
        

        mycursor = mydb.cursor()
        mycursor.execute("SELECT max(id)+1 FROM ev_booking")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        t = time.localtime()
        rtime = time.strftime("%H:%M:%S", t)
        today= date.today()
        rdate= today.strftime("%d-%m-%Y")

        rn=randint(1, 10)
        cimage="c"+str(rn)+".jpg"
        cursor = mydb.cursor()
        sql = "INSERT INTO ev_booking(id,uname,station,carno,reserve,slot,cimage,rtime,rdate,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        val = (maxid,uname,sid,carno,reserve,slot,cimage,rtime,rdate,'1')
        cursor.execute(sql, val)
        mydb.commit()
        vid=str(maxid)
        print(cursor.rowcount, "Booked Success")
        #return redirect(url_for('slot',sid=sid))
        msg="ok"

    
    
    return render_template('book.html',msg=msg,uname=uname,vid=vid,sid=sid,slot=slot)

@app.route('/book2', methods=['GET', 'POST'])
def book2():
    msg=""
    act=""
    vid=request.args.get("vid")
    if 'username' in session:
        uname = session['username']

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ev_booking where id=%s",(vid,))
    sdata = mycursor.fetchone()
    sid=sdata[2]
    
    if request.method=='POST':
        verify_mode=request.form['verify_mode']
        mycursor.execute("update ev_booking set verify_mode=%s where id=%s",(verify_mode,vid))
        mydb.commit()
        msg="ok"

        
        
    return render_template('book2.html',msg=msg,uname=uname,vid=vid,sid=sid)

        
def getImagesAndLabels(path):

    
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids


@app.route('/add_photo',methods=['POST','GET'])
def add_photo():
    uname=""
    if 'username' in session:
        uname = session['username']
    vid = request.args.get('vid')
    ff1=open("photo.txt","w")
    ff1.write("2")
    ff1.close()

    #ff2=open("mask.txt","w")
    #ff2.write("face")
    #ff2.close()
    act = request.args.get('act')

    cursor = mydb.cursor()
    
    cursor.execute("SELECT * FROM ev_register where uname=%s",(uname,))
    value = cursor.fetchone()
    name=value[1]
    
    ff=open("user.txt","w")
    ff.write(name)
    ff.close()

    ff=open("user1.txt","w")
    ff.write(vid)
    ff.close()
    
  
    if request.method=='POST':
        vid=request.form['vid']
        fimg="v"+vid+".jpg"
        

        cursor.execute('delete from vt_face WHERE vid = %s', (vid, ))
        mydb.commit()

        

        ff=open("det.txt","r")
        v=ff.read()
        ff.close()
        vv=int(v)
        v1=vv-1
        vface1="User."+vid+"."+str(v1)+".jpg"
        i=2
        while i<vv:
            
            cursor.execute("SELECT max(id)+1 FROM vt_face")
            maxid = cursor.fetchone()[0]
            if maxid is None:
                maxid=1
            vface="User."+vid+"."+str(i)+".jpg"
            sql = "INSERT INTO vt_face(id, vid, vface) VALUES (%s, %s, %s)"
            val = (maxid, vid, vface)
            print(val)
            cursor.execute(sql,val)
            mydb.commit()
            i+=1

        
            
        cursor.execute('update ev_booking set fimg=%s WHERE id = %s', (vface1, vid))
        mydb.commit()
        shutil.copy('static/faces/f1.jpg', 'static/photo/'+vface1)

        
        ##########
        
        ##Training face
        # Path for face image database
        path = 'dataset'

        recognizer = cv2.face.LBPHFaceRecognizer_create()

        # function to get the images and label data
        

        print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        faces,ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))






        #################################################
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM vt_face where vid=%s",(vid, ))
        dt = cursor.fetchall()
        for rs in dt:
            ##Preprocess
            path="static/frame/"+rs[2]
            path2="static/process1/"+rs[2]
            mm2 = PIL.Image.open(path).convert('L')
            rz = mm2.resize((200,200), PIL.Image.ANTIALIAS)
            rz.save(path2)
            
            '''img = cv2.imread(path2) 
            dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
            path3="static/process2/"+rs[2]
            cv2.imwrite(path3, dst)'''
            #noice
            img = cv2.imread('static/process1/'+rs[2]) 
            dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
            fname2='ns_'+rs[2]
            cv2.imwrite("static/process1/"+fname2, dst)
            ######
            ##bin
            image = cv2.imread('static/process1/'+rs[2])
            original = image.copy()
            kmeans = kmeans_color_quantization(image, clusters=4)

            # Convert to grayscale, Gaussian blur, adaptive threshold
            gray = cv2.cvtColor(kmeans, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (3,3), 0)
            thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,2)
            
            # Draw largest enclosing circle onto a mask
            mask = np.zeros(original.shape[:2], dtype=np.uint8)
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
            for c in cnts:
                ((x, y), r) = cv2.minEnclosingCircle(c)
                cv2.circle(image, (int(x), int(y)), int(r), (36, 255, 12), 2)
                cv2.circle(mask, (int(x), int(y)), int(r), 255, -1)
                break
            
            # Bitwise-and for result
            result = cv2.bitwise_and(original, original, mask=mask)
            result[mask==0] = (0,0,0)

            
            ###cv2.imshow('thresh', thresh)
            ###cv2.imshow('result', result)
            ###cv2.imshow('mask', mask)
            ###cv2.imshow('kmeans', kmeans)
            ###cv2.imshow('image', image)
            ###cv2.waitKey()

            cv2.imwrite("static/process1/bin_"+rs[2], thresh)
            

            ###RPN - Segment
            img = cv2.imread('static/process1/'+rs[2])
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            
            kernel = np.ones((3,3),np.uint8)
            opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

            # sure background area
            sure_bg = cv2.dilate(opening,kernel,iterations=3)

            # Finding sure foreground area
            dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
            ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

            # Finding unknown region
            sure_fg = np.uint8(sure_fg)
            segment = cv2.subtract(sure_bg,sure_fg)
            img = Image.fromarray(img)
            segment = Image.fromarray(segment)
            path3="static/process2/fg_"+rs[2]
            segment.save(path3)
            ####
            img = cv2.imread('static/process2/fg_'+rs[2])
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            
            kernel = np.ones((3,3),np.uint8)
            opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

            # sure background area
            sure_bg = cv2.dilate(opening,kernel,iterations=3)

            # Finding sure foreground area
            dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
            ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

            # Finding unknown region
            sure_fg = np.uint8(sure_fg)
            segment = cv2.subtract(sure_bg,sure_fg)
            img = Image.fromarray(img)
            segment = Image.fromarray(segment)
            path3="static/process2/fg_"+rs[2]
            segment.save(path3)
            '''
            img = cv2.imread(path2)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # noise removal
            kernel = np.ones((3,3),np.uint8)
            opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

            # sure background area
            sure_bg = cv2.dilate(opening,kernel,iterations=3)

            # Finding sure foreground area
            dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
            ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

            # Finding unknown region
            sure_fg = np.uint8(sure_fg)
            segment = cv2.subtract(sure_bg,sure_fg)
            img = Image.fromarray(img)
            segment = Image.fromarray(segment)
            path3="static/process2/"+rs[2]
            segment.save(path3)
            '''
            #####
            image = cv2.imread(path2)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 50, 100)
            image = Image.fromarray(image)
            edged = Image.fromarray(edged)
            path4="static/process3/"+rs[2]
            edged.save(path4)
            ##
        ###
        cursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
        cnt = cursor.fetchone()[0]
        if cnt>10:
            return redirect(url_for('view_photo',vid=vid,act='success'))
        else:
            return redirect(url_for('message',vid=vid))
    
    cursor.execute("SELECT * FROM ev_register")
    data = cursor.fetchall()
    return render_template('add_photo.html',data=data, vid=vid)


@app.route('/view_photo',methods=['POST','GET'])
def view_photo():
    ff1=open("photo.txt","w")
    ff1.write("1")
    ff1.close()
    vid=""
    value=[]
    if request.method=='GET':
        vid = request.args.get('vid')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM vt_face where vid=%s",(vid, ))
        value = mycursor.fetchall()

    if request.method=='POST':
        print("Training")
        vid=request.form['vid']
        
        #shutil.copy('static/img/11.png', 'static/process4/'+rs[2])
       
        return redirect(url_for('view_photo1',vid=vid))
        
    return render_template('view_photo.html', result=value,vid=vid)



def kmeans_color_quantization(image, clusters=8, rounds=1):
    h, w = image.shape[:2]
    samples = np.zeros([h*w,3], dtype=np.float32)
    count = 0

    for x in range(h):
        for y in range(w):
            samples[count] = image[x][y]
            count += 1

    compactness, labels, centers = cv2.kmeans(samples,
            clusters, 
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
            rounds, 
            cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    return res.reshape((image.shape))


@app.route('/pro1',methods=['POST','GET'])
def pro1():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None:
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro1.html', value=value,vid=vid, act=act3,s1=s1)

@app.route('/pro2',methods=['POST','GET'])
def pro2():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None or act=='0':
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro2.html', value=value,vid=vid, act=act3,s1=s1)

@app.route('/pro3',methods=['POST','GET'])
def pro3():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None:
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro3.html', value=value,vid=vid, act=act3,s1=s1)

@app.route('/pro4',methods=['POST','GET'])
def pro4():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None:
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro4.html', value=value,vid=vid, act=act3,s1=s1)

@app.route('/pro5',methods=['POST','GET'])
def pro5():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None:
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro5.html', value=value,vid=vid, act=act3,s1=s1)

@app.route('/pro6',methods=['POST','GET'])
def pro6():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None:
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro6.html', value=value,vid=vid, act=act3,s1=s1)

@app.route('/pro7',methods=['POST','GET'])
def pro7():
    s1=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM vt_face where vid=%s",(vid, ))
    cnt = mycursor.fetchone()[0]

    if act is None:
        act=1
        
    act1=int(act)-1
    act2=int(act)+1
    act3=str(act2)
    
    n=10
    if act1<n:
        s1="1"
        mycursor.execute("SELECT * FROM vt_face where vid=%s limit %s,1",(vid, act1))
        value = mycursor.fetchone()
    else:
        s1="2"

    
    return render_template('pro7.html', value=value,vid=vid, act=act3,s1=s1)




@app.route('/tariff', methods=['GET', 'POST'])
def tariff():
    msg=""
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where uname=%s",(uname, ))
    data= cursor.fetchone()
    return render_template('tariff.html',msg=msg, data=data, uname=uname)

@app.route('/history', methods=['GET', 'POST'])
def history():
    msg=""
    
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_booking b,ev_station s where b.station=s.id and b.uname=%s",(uname, ))
    data= cursor.fetchall()
    
    
    return render_template('history.html',msg=msg, data=data, uname=uname)


@app.route('/verify_face',methods=['POST','GET'])
def verify_face():
    s1=""
    rid = request.args.get('rid')
    sid = request.args.get('sid')
    
    
    act = request.args.get('act')
    value=[]
    
        
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    data = mycursor.fetchone()

    vmode=data[24]
    un=data[1]

    mycursor.execute("SELECT * FROM ev_register where uname=%s",(un, ))
    dat1 = mycursor.fetchone()
    mobile=dat1[3]
    name=dat1[1]

    rn=randint(1000,9999)
    otp=str(rn)

    det=otp+"|"+str(vmode)+"|"+name+"|"+str(mobile)
    ff=open("det3.txt","w")
    ff.write(det)
    ff.close()


    
    return render_template('verify_face.html', rid=rid,sid=sid, act=act)

@app.route('/verify_face1',methods=['POST','GET'])
def verify_face1():
    s1=""
    rid = request.args.get('rid')
    sid = request.args.get('sid')
    mess=""
    name=""
    mobile=""
    ff2=open("bc.txt","r")
    bc=ff2.read()
    ff2.close()
        
    
    act = request.args.get('act')
    value=[]

    ff=open("det3.txt","r")
    det=ff.read()
    ff.close()
    dett=det.split("|")

    otp=dett[0]
    vm=dett[1]
    name=dett[2]
    mobile=dett[3]
    
    ff=open("mess.txt","r")
    st=ff.read()
    ff.close()
    
    '''mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    data = mycursor.fetchone()
    vmode=data[24]
    un=data[1]'''
    

    '''vm=""
    if vmode==1:
        vm="1"
    else:
        vm="2"'''

    '''mycursor.execute("SELECT * FROM ev_register where uname=%s",(un, ))
    dat1 = mycursor.fetchone()
    mobile=dat1[3]
    name=dat1[1]

    

    rn=randint(1000,9999)
    otp=str(rn)'''

    

    
    #########################################################################
    #st="no"

    if st=="yes":
        s1="1"
    elif st=="no":
        s1="2"
        if vm=="1":
            mess="OTP: "+otp
            #mycursor.execute("update ev_booking set otp=%s where id=%s",(otp,rid))
            #mydb.commit()
        else:
            mess="Someone wrong"
            url2="http://localhost/parking/img.txt"
            ur = urlopen(url2)#open url
            data1 = ur.read().decode('utf-8')

           
            idd=int(data1)+1
            url="http://iotcloud.co.in/testsms/sms.php?sms=parking&name="+name+"&mess="+mess+"&mobile="+str(mobile)+"&bc="+bc
            print(url)
            webbrowser.open_new(url)
    
    
    return render_template('verify_face1.html', rid=rid,sid=sid, act=act,s1=s1,vm=vm,name=name,mess=mess,mobile=mobile)

@app.route('/verify_otp2', methods=['GET', 'POST'])
def verify_otp2():
    msg=""
    
    if 'username' in session:
        uname = session['username']
    
    rid=request.args.get('rid')
    sid = request.args.get('sid')

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    data = mycursor.fetchone()
    #key=data[14]

    ff=open("det3.txt","r")
    det=ff.read()
    ff.close()
    dett=det.split("|")

    key=dett[0]
    vm=dett[1]
    name=dett[2]
    mobile=dett[3]

    if request.method=='POST':
        otp=request.form['otp']
        if key==otp:
            msg="ok"
        else:
            msg="fail"

    

    return render_template('verify_otp2.html',msg=msg,rid=rid,sid=sid)


@app.route('/verify_link', methods=['GET', 'POST'])
def verify_link():
    msg=""
    stt=""
    if 'username' in session:
        uname = session['username']
    
    rid=request.args.get('rid')
    sid = request.args.get('sid')

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    data = mycursor.fetchone()
    key=data[14]

    result=data[25]

    url2="http://localhost/parking/log.txt"
    ur = urlopen(url2)#open url
    data1 = ur.read().decode('utf-8')
    vv=data1.split('-')
    data1=vv[0]
    
    print(data1)
    
    act = request.args.get('act')
    if act is None:
        act=""
    
    print("act="+str(act))
    if data1=="accept":
        stt="yes"
    else:
        stt="no"
    

    return render_template('verify_link.html',msg=msg,act=act,rid=rid,sid=sid,result=result,stt=stt)

@app.route('/cap',methods=['POST','GET'])
def cap():
    msg=""

    ff2=open("bc.txt","r")
    bc=ff2.read()
    ff2.close()

    
    
    return render_template('cap.html',msg=msg,bc=bc)

@app.route('/verify_link2', methods=['GET', 'POST'])
def verify_link2():
    msg=""
    stt=""
    if 'username' in session:
        uname = session['username']
    
    rid=request.args.get('rid')
    sid = request.args.get('sid')

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    data = mycursor.fetchone()
    key=data[14]

    result=data[25]

    url2="http://localhost/parking/log.txt"
    ur = urlopen(url2)#open url
    data1 = ur.read().decode('utf-8')
    vv=data1.split('-')
    data1=vv[0]
    
    print(data1)
    
    act = request.args.get('act')
    if act is None:
        act=""
    
    print("act="+str(act))
    if data1=="accept":
        stt="1"
        act="1"
    elif data1=="reject":
        stt="2"
        act="2"
    

    return render_template('verify_link2.html',msg=msg,act=act,rid=rid,sid=sid,result=result,stt=stt)
    
@app.route('/home', methods=['GET', 'POST'])
def home():
    msg=""
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where uname=%s",(uname, ))
    data= cursor.fetchone()
    return render_template('home.html',msg=msg, data=data, uname=uname)

@app.route('/view', methods=['GET', 'POST'])
def view():
    msg=""
    if 'username' in session:
        uname = session['username']

    msg=""
    act=""
    rid=""
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    s7=0
    s8=0
    s9=0
    s10=0
    if 'username' in session:
        uname = session['username']
    #if request.method=='GET':
    act=request.args.get('act')
    if act=="pay":
        rid=request.args.get('rid')
        cursor = mydb.cursor()
        cursor.execute("update ev_booking set pay_st=2,status=0 where id=%s",(rid, ))
        mydb.commit()
        return redirect(url_for('view'))
    if act=="start":
        rid=request.args.get('rid')
        cursor = mydb.cursor()
        cursor.execute("update ev_booking set charge_st=2 where id=%s",(rid, ))
        mydb.commit()
        return redirect(url_for('view'))
        
        
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where uname=%s",(uname, ))
    dd= cursor.fetchone()
    station=dd[1]
    sid=dd[0]
    cursor.execute("SELECT * FROM ev_booking where station=%s and status=1",(sid, ))
    data= cursor.fetchall()

    for nn in data:
        if nn[5]==1:
            s1=1
        if nn[5]==2:
            s2=2
        if nn[5]==3:
            s3=3
        if nn[5]==4:
            s4=4
        if nn[5]==5:
            s5=5
        if nn[5]==6:
            s6=6
        if nn[5]==7:
            s7=7
        if nn[5]==8:
            s8=8
        if nn[5]==9:
            s9=9
        if nn[5]==10:
            s10=10
        
        
    
    act="ok"
    return render_template('view.html',msg=msg,uname=uname,sid=sid,station=station,act=act,data=data,s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6,s7=s7,s8=s8,s9=s9,s10=s10)



@app.route('/payment', methods=['GET', 'POST'])
def payment():
    '''mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      charset="utf8",
      database="smart_parking_face"

    )'''
        
    cursor = mydb.cursor(buffered=True)
    
    uname=""
    if 'username' in session:
        uname = session['username']
    amount=0
    rid=request.args.get('rid')
    sid=request.args.get('sid')
    #cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_register where uname=%s",(uname, ))
    uu= cursor.fetchone()
    card=uu[6]
    cursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    dd= cursor.fetchone()
    amt=dd[15]
    ch=dd[15]

    t = time.localtime()
    rtime = time.strftime("%H:%M:%S", t)
    today= date.today()
    rdate= today.strftime("%d-%m-%Y")

    if ch>0:
        amount=ch
    else:
        amount=20

    cursor = mydb.cursor()
    cursor.execute("update ev_booking set edate=%s,etime=%s,amount=%s where id=%s",(rdate,rtime,amount,rid))
    mydb.commit()

    if request.method=='POST':
        pay_mode=request.form['pay_mode']
        if pay_mode=="Bank":
            rn=randint(1000, 9999)
            otp=str(rn)
            cursor = mydb.cursor()
            cursor.execute("update ev_booking set pay_mode=%s,sms_st=1,otp=%s where id=%s",(pay_mode,otp,rid))
            mydb.commit()
            return redirect(url_for('verify_otp',rid=rid))
        else:
            cursor = mydb.cursor()
            cursor.execute("update ev_booking set pay_mode=%s,pay_st=2,status=0 where id=%s",(pay_mode,rid))
            mydb.commit()
            return redirect(url_for('slot',sid=sid))
            
        
    return render_template('payment.html',sid=sid,rid=rid, uname=uname,amount=amount,card=card)


    

    
@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    msg=""
    
    if 'username' in session:
        uname = session['username']
    amount=0
    rid=request.args.get('rid')
    sid=request.args.get('sid')
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_register where uname=%s",(uname, ))
    uu= cursor.fetchone()
    mobile=uu[3]
    email=uu[4]
    cursor.execute("SELECT * FROM ev_booking where id=%s",(rid, ))
    dd= cursor.fetchone()
    key=dd[14]
    amount=dd[15]
    sms_st=dd[22]
    message="OTP:"+key
    
    if sms_st==1:
        url="http://iotcloud.co.in/testmail/testmail1.php?email="+email+"&message="+message
        webbrowser.open_new(url)
        #params = urllib.parse.urlencode({'token': 'b81edee36bcef4ddbaa6ef535f8db03e', 'credit': 2, 'sender': 'RnDTRY', 'message':message, 'number':mobile})
        #url = "http://pay4sms.in/sendsms/?%s" % params
        #with urllib.request.urlopen(url) as f:
        #    print(f.read().decode('utf-8'))
        #    print("sent"+str(mobile))

        #cursor = mydb.cursor()
        #cursor.execute("update ev_booking set pay_st=2,sms_st=0 where id=%s",(rid, ))
        #mydb.commit()
                    
    if request.method=='POST':
        otp=request.form['otp']
        if key==otp:
            
            cursor = mydb.cursor()
            cursor.execute("update ev_booking set pay_st=2,sms_st=0,status=0 where id=%s",(rid, ))
            mydb.commit()
            
            #cursor.execute("update ev_register set amount=amount-%s where uname=%s",(amount,uname))
            #mydb.commit()
            #return redirect(url_for('slot',sid=sid))
            msg="Amount Paid Successfully"
        else:
            msg="OTP wrong!"
        
    return render_template('verify_otp.html',rid=rid,sid=sid,msg=msg,otp=key)

@app.route('/report', methods=['GET', 'POST'])
def report():
    msg=""
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where uname=%s",(uname, ))
    dd= cursor.fetchone()
    sid=dd[0]
    cursor.execute("SELECT * FROM ev_booking where station=%s",(sid, ))
    data= cursor.fetchall()
    return render_template('report.html',msg=msg, data=data, uname=uname)



@app.route('/map', methods=['GET', 'POST'])
def map():
    msg=""
    if 'username' in session:
        uname = session['username']
    if request.method=='GET':
        lat=request.args.get('lat')
        lon=request.args.get('lon')
    return render_template('map.html',msg=msg, lat=lat, lon=lon)


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

def gen(camera):
    
    while True:
        frame = camera.get_frame()
        
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
#############################################
def gen2(camera):
    
    while True:
        frame = camera.get_frame()
        
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
@app.route('/video_feed2')       
def video_feed2():
    return Response(gen2(VideoCamera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
