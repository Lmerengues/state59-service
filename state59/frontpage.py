from django.http import HttpResponse

import json
from django.db import connections
from datetime import datetime

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]

def getsecond(date):

    now = datetime.now()
    date = date.replace(tzinfo=None)
    return (date - now).seconds

# def index(request):


#     cursor = connections['default'].cursor()
#     cursor.execute("select * from task")
#     raw = dictfetchall(cursor)
#     cursor.close()

#     newraw = []
#     for record in raw:
#         record["left"] = getsecond(record["tddl"])
#         record["tddl"] = datetime.strftime(record["tddl"],"%Y-%m-%d %H:%M:%S")
#     newraw = sorted(raw, key=lambda x:x["left"])

#     response = HttpResponse(json.dumps(newraw), content_type="application/json")
#     return response

def reply(request):
    ptype = request.GET['ptype']
    cursor = connections['default'].cursor()
    cursor.execute("select * from posts where ptype = %d",ptype)
    raw = dictfetchall(cursor)
    cursor.close()

    newraw = []
    for record in raw:
        record["left"] = getsecond(record["pdate"])
        record["pdate"] = datetime.strftime(record["pdate"],"%Y-%m-%d %H:%M:%S")
    newraw = sorted(raw, key=lambda x:x["left"])
    response = HttpResponse(json.dumps(newraw), content_type="application/json")
    return response
