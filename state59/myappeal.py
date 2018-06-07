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
    uid = request.GET['uid']
    cursor = connections['default'].cursor()
    cursor.execute("select hno, htitle, hddl, hmoney, pageviews, finished_label from help where uid = %s", (uid,))
    raw = dictfetchall(cursor)
    cursor.close()
    for data in raw:
        if data['finished_label'] == 0:
            data['finished_label_text'] = '未接单'
        elif data['finished_label'] == 1:
            data['finished_label_text'] = '已接单'

    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response




