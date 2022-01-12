import time

import pymysql
from flask import Flask, make_response, jsonify
from flask import render_template
import http.client
import json
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LCW6+kd5f'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://xiaoban_dev:LCW6+kd5f@10.108.160.143:3340/xiaoban?serverTimezone=Asia/Shanghai'  # 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)

import pymysql











import requests

xbk = "eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDE4ODM3MTUsInVzZXJJZCI6Ind1amlheGluZ0Bjb3JwLm5ldGVhc2UuY29tIiwicm9sZUlkIjozMiwicHJvZHVjdElkIjo0LCJuaWNrbmFtZSI6IuatpiJ9.ZJ_zdGDC8NpZTW843HmvaDyUlW7WusGcdosHEKegSYE"

cookie = 'OUTFOX_SEARCH_USER_ID_NCOO=1405845668.1002636; OUTFOX_SEARCH_USER_ID="1105122743@10.105.137.202"; _ga=GA1.2.606080555.1636362389; UM_distinctid=17cfed301aa7cd-0bccc5aad1b59d-1c306851-1fa400-17cfed301ab77c; experimentation_subject_id=ImEwNjdjNDY1LTdmYTktNDg3Mi1iMDQ0LWQ3MTRlY2YwZGM5NSI%3D--ac51f6e3c951e8226ef9f73f77fb9577802786c5; wap_abtest=5; _ntes_nnid=8a82b78c85ef1123d303970c932d2381,1637477089730; mp_MA-BF02-71D44E7C0390_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fc.youdao.com%2Finspire%2Fdownload.html%22%2C%22updatedTime%22%3A%201638271303970%2C%22sessionStartTime%22%3A%201638271296077%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22f11c213a-7074-4685-9c92-d7643b6124c3%22%2C%22persistedTime%22%3A%201637048943929%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%228d0bc9192c28057a9996372b32f99c6059ea1325%22%2C%22time%22%3A%201638271303971%7D%2C%22sessionUuid%22%3A%20%223a4a8383-f2c9-4d42-8858-26f393cb3b0b%22%7D; hb_MA-B0D8-94CBE089C042_source=www.google.com.hk; mp_MA-A5CB-3A8CE4190A3F_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fmanhattan-stable.inner.youdao.com%2F%23%2Fuser%2Finfo%2FU2FsdGVkX19HA45cVRkxeeZn1wCbF13u1gWjZKWgv0gICgxR33RrHtPRFaDWqopA%22%2C%22updatedTime%22%3A%201638859486344%2C%22sessionStartTime%22%3A%201638859486342%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%203%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22a3993541-736e-49e5-8832-5c225f27179d%22%2C%22persistedTime%22%3A%201638519037892%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201638859486344%7D%2C%22sessionUuid%22%3A%20%227f576556-21be-4577-80c6-90f67b989458%22%2C%22user_id%22%3A%20%22wujiaxing%40corp.netease.com%22%7D; DICT_FORCE=true; hb_MA-BB84-AB2D0288F3F5_source=jira.inner.youdao.com; NTES_YD_SESS=9oDWEjsXOJfMjfe45wLOMvfktdEwVw5J1ptcFykqztyb_q13_H8IY.wMde7YEPaW1dHJeck3FdMZoW3TSBEqycXkSufRIiAlTr0SF0voUM02EkjiqFVGaP9SrLi1WYP6CEB7.DOnPbC8KiIktegsfAvT.a0G090.KFbCYa5x8q5af3GqtvoDjLpn0d8z6XCg1yzxh39aaUM.cEXTJmtfTetrc.q.7e1F_9BhlaFgLGqcT; S_INFO=1640169967|0|0&60##|19801250393; P_INFO=19801250393|1640169967|1|youdaodict|00&99|bej&1640058201&youdaodict#bej&null#10#0#0|&0|null|19801250393; DICT_SESS=v2|wyPLhCpiemJ4nfYMk4TK0gLOMQShfTZ0puRHpB0MwBROY0LkWRHQL0kfP4U5nflY0YGRHQu6LOERqZ0MwK6Lkf0O5nMYGRMQu0; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1640169967353||61.135.255.83||urs-phoneyd.11cfd7e893a24e37b@163.com||Y5hMTBn4TuReynMzm0HzERYWhHlAO4PBRzYhMYGOLeK0pu6LJ4OfP4Rkm6MJy0HeK0l5nM64kfJLR6F0HOfPLqu0; DICT_LOGIN=7||1640169967358; yuid=1640261706455||447d9c503a3741ed81453e4843e6b264; OSMS_corp=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5NzhiODZjOGJmNGIxMWVhYjVkMzVjZjNmYzk2YTcyYyIsImlzcyI6Imh0dHBzOi8vbG9naW4ubmV0ZWFzZS5jb20vY29ubmVjdCIsImV4cCI6MTY0MDI3MzA1NiwiYXV0aF90aW1lIjoxNjQwMjQ1NTA2LCJpYXQiOjE2NDAyNzI0NTYsInN1YiI6Ind1amlheGluZyJ9._R3G0jARbABG8UHrT40u4raSjb4n9dtapJOZ-OZKrWk; OSMS_bindAccount=dkcglTSxoIuCoW7JPX_w6hV8ZKMehNNksfArMwkVC58=; mp_MA-BB84-AB2D0288F3F5_hubble=%7B%22sessionReferrer%22%3A%20%22%22%2C%22updatedTime%22%3A%201640272591490%2C%22sessionStartTime%22%3A%201640272439497%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%209%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22d5f43fb240973ef6588dbb4bbe7273e049935385%22%2C%22persistedTime%22%3A%201637032896261%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_u_login%22%2C%22time%22%3A%201640272591490%7D%2C%22sessionUuid%22%3A%20%22634f61609d85445eb540e71fcd1a26e87d1046bf%22%2C%22user_id%22%3A%20%22wujiaxing%40corp.netease.com%22%7D; CourseopSessionId=Bk003fs1vzq1AZ+dMHGOtVe2zCEpCuA0UTX8TAneCQIioB6nzCcfdiB0+NWjSdcK1+wk9eme1Qz/+GNWvUPyV1EW2m3HS0/QYp2ePxcFcxo='


# 正式课
@app.route('/', methods=['GET', 'POST'])
def Index():
    return render_template('index.html')


@app.route('/d', methods=['GET', 'POST'])
def D():
    return render_template('delete.html')


@app.route('/q', methods=['GET', 'POST'])
def Q():
    return render_template('query.html')


@app.route('/s', methods=['GET', 'POST'])
def S():
    return render_template('shang.html')


@app.route('/22', methods=['GET', 'POST'])
def bianli():
    data = request.get_data()
    print(data)
    json_re = json.loads(data)
    name = json_re['text1']
    userid = ["urs-phoneyd.d1edb864ff4a4208b@163.com",
              "urs-phoneyd.88fcea851d5448a7b@163.com",
              "urs-phoneyd.11cfd7e893a24e37b@163.com",
              "urs-phoneyd.57a07dd3681441798@163.com"]
    ids = 1
    for i in userid:
        addxbc(name, i, ids)
        ids += 1
    return "tian"



def addxbc(name, i, ids):
    url = "http://10.109.1.135:8888/order/order?encrption=xbk_order"

    payload = json.dumps({
        "id": ids,
        "courses": [
            {
                "id": name,
                "title": "【百折不挠3】三阶体验课"
            }
        ],
        "finishTime": "2021-02-25 11:00:00",
        "status": 11,
        "userId": i,
        "userNickname": "啊请修改昵称",
        "mobile": "18031712521"
    })
    headers = {
        'xbk-token': xbk,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return "添加成功"

@app.route('/23', methods=['GET', 'POST'])
def AddClass():
    pid = Getcode()
    jpk = Findnew()
    conn = http.client.HTTPSConnection("courseop1.inner.youdao.com")
    payload = ''
    headers = {
        'cookie': cookie
    }
    conn.request("GET", "/user/coursePrivilege/adds?sseParamId=" + pid, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return {'jpk': jpk}


def Getcode():
    jpk = Findnew()
    conn = http.client.HTTPSConnection("courseop1.inner.youdao.com")
    payload = json.dumps({
        "reportAddrs": "wujx02@rd.netease.com",
        "userIds": [
            "urs-phoneyd.88fcea851d5448a7b@163.com",
            "urs-phoneyd.11cfd7e893a24e37b@163.com",
            "urs-phoneyd.57a07dd3681441798@163.com"
        ],
        "courseId": jpk,
        "insider": False
    })
    headers = {
        'cookie': cookie,
        'Content-Type': 'application/json'
    }
    conn.request("PUT", "/sse/param", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    datacontent = last['data']
    return datacontent


# 获取对应创建课程的课程ID

@app.route('/4')
def chengxian():
    id = GetList()
    return {'id': id}


def GetList():
    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = ''
    headers = {
        'xbk-token': xbk
    }
    conn.request("GET", "/courseop/api/formalCourse/getList?current=1&pageSize=20&size=20", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    datacontent = last['data']
    courseid = datacontent['courseList'][0]
    keid = courseid['courseId']
    return str(keid)


@app.route('/1')
def CreateCourse():  # put application's code here
    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = json.dumps({
        "courseName": "2.0.2",
        "subjectId": 0,
        "faceToAge": "[3]",
        "liveType": 2,
        "deductLessonPeriod": 1,
        "effectAttendanceTime": 5,
        "firstCharge": 5,
        "background": "",
        "cover": "",
        "lessonPeriod": None
    })
    headers = {
        'xbk-token': xbk,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/courseop/api/formalCourse/saveOrUpdate", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    print(result)
    last = json.loads(result)
    code = last['code']
    return code


@app.route('/5')
def CreateSx():
    kcourse = CreateCourse()
    ckj = Ckj()
    sj = Shangjia()
    ke = GetList()
    if kcourse == 200 and ckj == 200 and sj == 200:
        return {"result": ke}
    else:
        return {"result": "创建失败"}


# 创建课节成功
def Ckj():
    kid = GetList()
    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = json.dumps(
        {
            "lessonList": [
                {
                    "name": "第一节课",
                    "courseId": kid,
                    "lessonWeight": 1
                }
            ]
        }
    )
    headers = {
        'xbk-token': xbk,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/courseop/api/lesson/saveOrUpdateFormalCourse", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    code = last['code']
    return code


@app.route('/2')
def Delete():
    import http.client
    keid = GetList()
    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = ''
    headers = {
        'xbk-token': xbk
    }

    conn.request("DELETE", "/courseop/api/formalCourse/delete?courseId=" + keid, payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)

    if last["code"] == 200:
        return {'id': keid}
    else:
        return "删除失败"


# 批量删除课权
global count


@app.route('/6', methods=['POST'])
def PiD():
    data = request.get_data()
    json_re = json.loads(data)
    name = json_re['text1']
    num = json_re['text2']

    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = ''
    headers = {
        'xbk-token': xbk
    }
    conn.request("GET", "/courseop/api/formalCourse/getList?current=1&pageSize=20&size=20", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    datacontent = last['data']
    coursedate = datacontent['courseList']

    count = 0
    while coursedate:
        for i in coursedate:
            count += 1
            ct = i['creator']
            if ct == name:
                d = Delete()

            else:
                continue
            if count == int(num):
                break
        break

    return {"count": str(count)}


@app.route('/3')
def Shangjia():
    keid = GetList()
    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = ''
    headers = {
        'xbk-token': xbk,
    }
    conn.request("POST", "/courseop/api/formalCourse/putOn?courseId=" + keid, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    last = json.loads(data)
    code = last['code']
    return code

@app.route('/33',methods=['POST'])
def upadate():
    data = request.get_data()
    json_re = json.loads(data)
    liveid = json_re['text3']
    db = pymysql.connect(
        host='10.108.160.143',
        port=3340,
        user='xiaoban_dev',
        password='LCW6+kd5f',
        database='xiaoban',
        charset='utf8',
    )
    cursor = db.cursor()
    pretime = altertime()

    sql = 'update xb_live set start_time =\''+pretime+'\' where live_id='+liveid

    result =cursor.execute(sql)

    db.commit()
    cursor.close()
    db.close()

    return {'result':"成功"}

def altertime():
    # 格式化成2016-03-20 11:45:39形式
    # conding:utf-8
    import time
    ticksnow = int(time.time())
    tickspre = int(time.time()) - 600
    # 转换为localtime
    timeArray = time.localtime(tickspre)
    timeno = time.localtime(ticksnow)
    # 获取到开课的时间
    starttime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return starttime




global name
@app.route('/21', methods=['POST','GET'])
def CK():
    data = request.get_data()
    json_re = json.loads(data)
    name = json_re['text1']
    name1 = json_re['text2']
    url = "https://ares.inner.youdao.com/ares/api/class/arrange"
    payload = json.dumps({
        "name": name1,
        "maxStudent": 3,
        "studentUp": 1,
        "date": "2023-12-30 15:35:53",
        "weekday": 64,
        "timeRange": [
            "2021-12-24 03:00:00",
            "2021-12-24 06:00:00"
        ],
        "idList": [],
        "courseId": name,
        "studentIdList": [],
        "firstDate": 1703865600000,
        "startTime": "0300",
        "endTime": "0600"
    })
    headers = {
        'xbk-token': xbk,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    conn = http.client.HTTPSConnection("xbkcourse6.inner.youdao.com")
    payload = ''
    headers = {
        'xbk-token': xbk
    }
    conn.request("GET", "/courseop/api/class/page?current=1&pageSize=20&size=20&courseId=" + name, payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    datacontent = last['data']
    sl = datacontent['records']
    return {'result' : name1}



@app.route('/33', methods=['POST'])
def piYue():
    data = request.get_data()
    json_re = json.loads(data)
    name = json_re['text1']
    cid = getCid()
    korderid = cid[0]
    names = cid[1]
    userid = cid[2]

    for i in range(len(name)):
        yk = yueke(names[i], name, korderid[i], userid[i])
    return yk


def yueke(k, name, v, u):
    url = "https://ares.inner.youdao.com/ares/api/classArrange/submit"

    payload = json.dumps({
        "nickname": k,
        "phone": "",
        "time": {
            "09:00~10:10": [
                "周一09:00~10:10"
            ]
        },
        "courseId": name,
        "studentUserId": u,
        "keCourseOrderId": v,
        "intentPeriodList": [
            {
                "weekday": 1,
                "startPeriod": "0900",
                "endPeriod": "1010"
            }
        ]
    })
    headers = {
        'xbk-token': xbk,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return '约课成功'


@app.route('/34', methods=['POST'])
def getCid():
    data = request.get_data()
    json_re = json.loads(data)
    name = json_re['text1']
    url = "https://xbkcourse5.inner.youdao.com/courseop/api/order/getList?keCourseIdOrName=&localCourseIdOrName=" + name + "&current=1&size=10&status=2"

    payload = {}
    headers = {
        'xbk-token': xbk
    }
    result = []
    name = []
    uuid = []
    response = requests.request("GET", url, headers=headers, data=payload)
    res = json.loads(response.text)
    data = res['data']
    orid = data['orderList']

    for i in orid:
        result.append(i['id'])
        name.append(i['nickname'])
        uuid.append(i['userId'])

    return result, name, uuid


# 创建精品课课程
def Cjp():
    import http.client

    conn = http.client.HTTPSConnection("courseop1.inner.youdao.com")
    payload = ''
    headers = {
        'cookie': cookie
    }
    conn.request("PUT", "/course/course/copy?courseId=37910", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    code = last['data']
    return str(code)


# 课程发布
@app.route('/10')
def Fb():
    jpkid = Cjp()

    conn = http.client.HTTPSConnection("courseop1.inner.youdao.com")
    payload = ''
    headers = {
        'cookie': cookie
    }
    conn.request("PUT", "/course/course/publish?id=" + jpkid, payload, headers)
    res = conn.getresponse()
    data = res.read()

    return {"jpk": jpkid}


# 获取最新的精品课课程
def Findnew():
    conn = http.client.HTTPSConnection("courseop1.inner.youdao.com")
    payload = json.dumps({
        "categoryId": None,
        "keyword": "qa-wjx",
        "teacherKeyword": "",
        "pager": {
            "pageNo": 1,
            "pageSize": 10
        },
        "sorts": [
            {
                "field": "courseId",
                "ascOrDesc": False
            }
        ]
    })
    headers = {
        'cookie': cookie,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/course/course/edit", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    last = json.loads(result)
    code = last['data']
    fistcourse = code['courses'][0]
    return str(fistcourse['courseId'])


# 关联课程
@app.route('/11')
def GL():
    xbkid = GetList()
    jpkid = Findnew()
    conn = http.client.HTTPSConnection("xbkcourse5.inner.youdao.com")
    payload = json.dumps({
        "courseId": xbkid,
        "keCourseId": [
            jpkid
        ],
        "keCourseIdList": [
            jpkid
        ]
    })
    headers = {
        'xbk-token': xbk,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/courseop/api/course/mapToKe", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    return {"result": xbkid, "result2": jpkid}


@app.route('/7')
def SJ():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='wjxtest')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select userid,name from job")
    cursor.nextset()
    obj = cursor.fetchall()
    list = []
    for i in obj:
        list.append([i['userid'], i['name']])
    print(list)
    conn.commit()
    cursor.close()
    conn.close()
    return str(list)


if __name__ == '__main__':
    app.config.from_object('config')

    app.run()
