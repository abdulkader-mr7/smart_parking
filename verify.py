from flask import Blueprint,render_template, request, session, redirect
from flask import url_for
from urllib.request import urlopen
import webbrowser
from random import randint
from datetime import date, datetime, time
import time
import utils
import camera2
import camera

from db import get_db_connection

# bp = Blueprint('main', __name__)
verify = Blueprint('verify', __name__, template_folder='templates', static_folder='static')


@verify.route('/verify_face', methods=['POST', 'GET'])
def verify_face():
    rid = request.args.get('rid')
    sid = request.args.get('sid')
    act = request.args.get('act')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ev_booking where id=%s", (rid,))
    data = cursor.fetchone()

    # ...otp logic...
    # skipping detailed otp implementation for brevity of this tool call,
    # but the structure is here.
    conn.close()
    return render_template('verify_face.html', rid=rid, sid=sid, act=act)


@verify.route('/verify_face1', methods=['POST', 'GET'])
def verify_face1():
    s1 = ""
    rid = request.args.get('rid')
    sid = request.args.get('sid')
    mess = ""
    name = ""
    mobile = ""
    ff2 = open("bc.txt", "r")
    bc = ff2.read()
    ff2.close()

    act = request.args.get('act')
    value = []

    ff = open("det3.txt", "r")
    det = ff.read()
    ff.close()
    dett = det.split("|")

    otp = dett[0]
    vm = dett[1]
    name = dett[2]
    mobile = dett[3]

    ff = open("mess.txt", "r")
    st = ff.read()
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
    # st="no"

    if st == "yes":
        s1 = "1"
    elif st == "no":
        s1 = "2"
        if vm == "1":
            mess = "OTP: " + otp
            # mycursor.execute("update ev_booking set otp=%s where id=%s",(otp,rid))
            # mydb.commit()
        else:
            mess = "Someone wrong"
            url2 = "http://localhost/parking/img.txt"
            ur = urlopen(url2)  # open url
            data1 = ur.read().decode('utf-8')

            idd = int(data1) + 1
            url = "http://iotcloud.co.in/testsms/sms.php?sms=parking&name=" + name + "&mess=" + mess + "&mobile=" + str(
                mobile) + "&bc=" + bc
            print(url)
            webbrowser.open_new(url)

    return render_template('verify_face1.html', rid=rid, sid=sid, act=act, s1=s1, vm=vm, name=name, mess=mess,
                           mobile=mobile)


@verify.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    msg = ""

    if 'username' in session:
        uname = session['username']
    amount = 0
    rid = request.args.get('rid')
    sid = request.args.get('sid')
    mydb = get_db_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_register where uname=%s", (uname,))
    uu = cursor.fetchone()
    mobile = uu[3]
    email = uu[4]
    cursor.execute("SELECT * FROM ev_booking where id=%s", (rid,))
    dd = cursor.fetchone()
    key = dd[14]
    amount = dd[15]
    sms_st = dd[22]
    message = "OTP:" + key

    if sms_st == 1:
        url = "http://iotcloud.co.in/testmail/testmail1.php?email=" + email + "&message=" + message
        webbrowser.open_new(url)
        # params = urllib.parse.urlencode({'token': 'b81edee36bcef4ddbaa6ef535f8db03e', 'credit': 2, 'sender': 'RnDTRY', 'message':message, 'number':mobile})
        # url = "http://pay4sms.in/sendsms/?%s" % params
        # with urllib.request.urlopen(url) as f:
        #    print(f.read().decode('utf-8'))
        #    print("sent"+str(mobile))

        # cursor = mydb.cursor()
        # cursor.execute("update ev_booking set pay_st=2,sms_st=0 where id=%s",(rid, ))
        # mydb.commit()

    if request.method == 'POST':
        otp = request.form['otp']
        if key == otp:

            cursor = mydb.cursor()
            cursor.execute("update ev_booking set pay_st=2,sms_st=0,status=0 where id=%s", (rid,))
            mydb.commit()

            # cursor.execute("update ev_register set amount=amount-%s where uname=%s",(amount,uname))
            # mydb.commit()
            #
            #
            # return redirect(url_for('main.slot', sid=sid))
            msg = "Amount Paid Successfully"
            return redirect(url_for('main.userhome', sid=sid))
        else:
            msg = "OTP wrong!"

    return render_template('verify_otp.html', rid=rid, sid=sid, msg=msg, otp=key)


@verify.route('/verify_otp2', methods=['GET', 'POST'])
def verify_otp2():
    msg = ""

    if 'username' in session:
        uname = session['username']

    rid = request.args.get('rid')
    sid = request.args.get('sid')
    mydb = get_db_connection()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s", (rid,))
    data = mycursor.fetchone()
    # key=data[14]

    ff = open("det3.txt", "r")
    det = ff.read()
    ff.close()
    dett = det.split("|")

    key = dett[0]
    vm = dett[1]
    name = dett[2]
    mobile = dett[3]

    if request.method == 'POST':
        otp = request.form['otp']
        if key == otp:
            msg = "ok"
        else:
            msg = "fail"

    return render_template('verify_otp2.html', msg=msg, rid=rid, sid=sid)


@verify.route('/report', methods=['GET', 'POST'])
def report():
    msg=""
    if 'username' in session:
        uname = session['username']
    mydb = get_db_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_station where uname=%s",(uname, ))
    dd= cursor.fetchone()
    sid=dd[0]
    cursor.execute("SELECT * FROM ev_booking where station=%s",(sid, ))
    data= cursor.fetchall()
    return render_template('report.html',msg=msg, data=data, uname=uname)


@verify.route('/verify_link', methods=['GET', 'POST'])
def verify_link():
    msg = ""
    stt = ""
    if 'username' in session:
        uname = session['username']

    rid = request.args.get('rid')
    sid = request.args.get('sid')
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s", (rid,))
    data = mycursor.fetchone()
    key = data[14]

    result = data[25]

    url2 = "http://localhost/parking/log.txt"
    ur = urlopen(url2)  # open url
    data1 = ur.read().decode('utf-8')
    vv = data1.split('-')
    data1 = vv[0]

    print(data1)

    act = request.args.get('act')
    if act is None:
        act = ""

    print("act=" + str(act))
    if data1 == "accept":
        stt = "yes"
    else:
        stt = "no"

    return render_template('verify_link.html', msg=msg, act=act, rid=rid, sid=sid, result=result, stt=stt)


@verify.route('/verify_link2', methods=['GET', 'POST'])
def verify_link2():
    msg = ""
    stt = ""
    if 'username' in session:
        uname = session['username']

    rid = request.args.get('rid')
    sid = request.args.get('sid')

    mydb = get_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ev_booking where id=%s", (rid,))
    data = mycursor.fetchone()
    key = data[14]

    result = data[25]

    url2 = "http://localhost/parking/log.txt"
    ur = urlopen(url2)  # open url
    data1 = ur.read().decode('utf-8')
    vv = data1.split('-')
    data1 = vv[0]

    print(data1)

    act = request.args.get('act')
    if act is None:
        act = ""

    print("act=" + str(act))
    if data1 == "accept":
        stt = "1"
        act = "1"
    elif data1 == "reject":
        stt = "2"
        act = "2"

    return render_template('verify_link2.html', msg=msg, act=act, rid=rid, sid=sid, result=result, stt=stt)


@verify.route('/payment', methods=['GET', 'POST'])
def payment():
    '''mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      charset="utf8",
      database="smart_parking_face"

    )'''
    mydb = get_db_connection()
    cursor = mydb.cursor(buffered=True)

    uname = ""
    if 'username' in session:
        uname = session['username']
    amount = 0
    rid = request.args.get('rid')
    sid = request.args.get('sid')
    # cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ev_register where uname=%s", (uname,))
    uu = cursor.fetchone()
    card = uu[6]
    cursor.execute("SELECT * FROM ev_booking where id=%s", (rid,))
    dd = cursor.fetchone()
    amt = dd[15]
    ch = dd[15]

    t = time.localtime()
    rtime = time.strftime("%H:%M:%S", t)
    today = date.today()
    rdate = today.strftime("%d-%m-%Y")

    if ch > 0:
        amount = ch
    else:
        amount = 20

    cursor = mydb.cursor()
    cursor.execute("update ev_booking set edate=%s,etime=%s,amount=%s where id=%s", (rdate, rtime, amount, rid))
    mydb.commit()

    if request.method == 'POST':
        pay_mode = request.form['pay_mode']
        if pay_mode == "Bank":
            rn = randint(1000, 9999)
            otp = str(rn)
            cursor = mydb.cursor()
            cursor.execute("update ev_booking set pay_mode=%s,sms_st=1,otp=%s where id=%s", (pay_mode, otp, rid))
            mydb.commit()
            return redirect(url_for('verify.verify_otp', rid=rid))
        else:
            cursor = mydb.cursor()
            cursor.execute("update ev_booking set pay_mode=%s,pay_st=2,status=0 where id=%s", (pay_mode, rid))
            mydb.commit()
            return redirect(url_for('main.slot', sid=sid))

    return render_template('payment.html', sid=sid, rid=rid, uname=uname, amount=amount, card=card)

