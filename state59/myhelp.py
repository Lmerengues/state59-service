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


def index(request):
    uid = request.GET['uid']
    cursor = connections['default'].cursor()
    cursor.execute("select unickName, uavatarurl, htitle, hddl, hmoney, ismoney, pageviews, accepted_label, help.uid from help, help_accept, Users where help.hno = help_accept.hhno and help.uid = Users.uid and help_accept.uid = %s", (uid,))
    raw = dictfetchall(cursor)
    cursor.close()
    for data in raw:
        if data['ismoney'] == 1:
            data['hmoney'] = str(round(1.0*int(data['hmoney'])/100,2)) + '元'
        data['hddl'] = datetime.datetime.strftime(data['hddl'],'%Y-%m-%d %H:%M:%S')
    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response




