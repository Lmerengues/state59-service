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

    #root_dir = img_path+''.join(random.sample(string.ascii_letters + string.digits, 16))
    root_dir = img_path+ "1"
    if not os.path.exists(root_dir):
        os.mkdirs(root_dir)
    else:
	print "1"	
    '''
    with open(root_dir + '/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    '''
    dict = {'status':root_dir}

    resp = HttpResponse(json.dumps(dict), content_type="application/json")
    return resp

