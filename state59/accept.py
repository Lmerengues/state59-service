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
    hhno = request.GET['hhno']
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
        cursor.execute("update help set finished_label = 1 where hno = %s", (hhno,))
        cursor.close()

    cursor = connections['default'].cursor()
    cursor.execute("select hno, unickName, uavatarurl, mobile, wechatnum, message, accepted_label from help_accept, Users where help_accept.uid = Users.uid and hhno = %s", (hhno,))
    raw = dictfetchall(cursor)
    cursor.close()
    for data in raw:
        if data['accepted_label'] == 0:
            data['accepted_label_text'] = '接受'
        elif data['accepted_label'] == 1:
            data['accepted_label_text'] = '已接受'
    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response



