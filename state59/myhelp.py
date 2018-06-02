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
    cursor.execute("select unickName, uavatarurl, htitle, hddl, hmoney, pageviews, accepted_label, help.uid from help, help_accept, Users where help.hno = help_accept.hhno and help.uid = Users.uid and help_accept.uid = %s", (uid,))
    raw = dictfetchall(cursor)
    cursor.close()
    for data in raw:
        if data['accepted_label'] == 0:
            data['accepted_label_text'] = '未通过'
        elif data['accepted_label'] == 1:
            data['accepted_label_text'] = '已通过'
    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response




