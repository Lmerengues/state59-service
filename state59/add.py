# -*- coding: UTF-8 -*-
from django.http import HttpResponse

import json
from django.db import connections

import datetime

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]


def addhelp(request):
    title = request.GET['title']
    ddl = request.GET['ddl']
    tim = request.GET['tim']
    typ = request.GET['typ']
    money = request.GET['money']
    detail = request.GET['detail']
    mobile = request.GET['mobile']
    wechat = request.GET['wechat']
    uid = request.GET['openid']

    cursor = connections['default'].cursor()
    cursor.execute("insert into help values(null,%s,sysdate(),%s,%s,%s,0,0,%s,%s,%s)",title,money,typ,detail,uid,mobile,wechat)
    raw = dictfetchall(cursor)
    cursor.close()

    dict = {'status':1}
    resp = HttpResponse(json.dumps(dict), content_type="application/json")
    return resp