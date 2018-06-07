# -*- coding: UTF-8 -*-
from django.http import HttpResponse

import json
from django.db import connections

import datetime
import time
import random
import string
import os

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]


def addhelp(request):


    title = request.GET['title']
    ddl = request.GET['ddl']
    tim = request.GET['time']
    typ = request.GET['typ']
    money = request.GET['money']
    detail = request.GET['detail']
    mobile = request.GET['mobile']
    wechat = request.GET['wechat']
    uid = request.GET['openid']

    datet = datetime.datetime(int(ddl.split('-')[0]),int(ddl.split('-')[1]),int(ddl.split('-')[2]),int(tim.split(':')[0]),int(tim.split(':')[1]))

    cursor = connections['default'].cursor()
    cursor.execute("insert into help values(null,%s,%s,%s,%s,%s,0,0,%s,%s,%s)",(title,datet,money,typ,detail,uid,mobile,wechat,))
    raw = dictfetchall(cursor)
    cursor.close()

    dict = {'status':1}
    resp = HttpResponse(json.dumps(dict), content_type="application/json")
    return resp



def addimage(request):
    
    f = request.FILES['img']
    
    t = str(time.time())
    img_path = "/var/www/html/state59/static/images/"
    err_str = ""
    #root_dir = img_path+''.join(random.sample(string.ascii_letters + string.digits, 16))
    root_dir = img_path+ t
    try:
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)
        else:
	    print "1"
        with open(root_dir + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        cursor = connections['default'].cursor()
        cursor.execute("insert into images values(null,%s)",("https://www.state59.com/static/images/"+t + '/' + f.name,))

        cursor.close()
    except Exception,e:
        err_str = e.message
    '''
    with open(root_dir + '/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    '''
    cursor = connections['default'].cursor()
    cursor.execute("select ino from images where iurl = %s",("https://www.state59.com/static/images/"+t + '/' + f.name,))
    raw = dictfetchall(cursor)
    cursor.close()
    
    if len(raw)==1:
        dict = {'ino':raw[0]['ino'],'status':1}
    else:    
        dict = {'status':0}

    resp = HttpResponse(json.dumps(dict), content_type="application/json")
    return resp

def addpost(request):

    title = request.GET['title']
    detail = request.GET['detail']
    typ = request.GET['typ']
    ino = request.GET['ino']
    openid = request.GET['openid']

    cursor = connections['default'].cursor()
    cursor.execute("insert into posts values(null,%s,%s,%s,%s,sysdate())",(title, detail,openid, typ,))
    cursor.close()

    cursor = connections['default'].cursor()
    cursor.execute("select * from posts where ptitle = %s and pdetail = %s",(title,detail,))
    post = dictfetchall(cursor)
    cursor.close()
    pno  = post[0]['pno']

    cursor = connections['default'].cursor()
    cursor.execute("insert into posts_image values(%s,%s)", (ino, pno,))
    cursor.close()

    dict = {'status': 1}
    resp = HttpResponse(json.dumps(dict), content_type="application/json")
    return resp
