# -*- coding: UTF-8 -*-
from django.http import HttpResponse

import json
from django.db import connections

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]


def index(request):
    hno = request.GET['hno']
    cursor = connections['default'].cursor()
    cursor.execute("select hno, unickName, uavatarurl, mobile, wechatnum, message, accepted_label from help_accept, Users where help_accept.uid = Users.uid and hhno = %s", (hno,))
    raw = dictfetchall(cursor)
    cursor.close()
    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response

def accept(request):
    hno = request.GET['itemid']
    hhno = request.GET['hno']
    cursor = connections['default'].cursor()
    cursor.execute("select accepted_label from help_accept where hhno = %s", (hhno,))
    raw = dictfetchall(cursor)
    cursor.close()
    flag = 0
    for data in raw:
        if data['accepted_label'] == 1:
            flag = 1
            break
    if flag != 1:
        cursor = connections['default'].cursor()
        cursor.execute("update help_accept set accepted_label = 1 where hno = %s", (hno,))
        cursor.close()

    cursor = connections['default'].cursor()
    cursor.execute("select hno, unickName, uavatarurl, mobile, wechatnum, message, accepted_label from help_accept, Users where help_accept.uid = Users.uid and hhno = %s", (hhno,))
    raw = dictfetchall(cursor)
    cursor.close()
    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response



