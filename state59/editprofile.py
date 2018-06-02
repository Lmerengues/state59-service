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
    #raw = {"id":1,"text":"xxx"}
    #?uid=ouSgl0a6qmKFcqO5RFiV8Rc-n0fc
    cursor = connections['default'].cursor()
    cursor.execute("select unickName, ugender, uavatarurl from Users where uid = %s", (uid,))
    raw = dictfetchall(cursor)
    cursor.close()

    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response




