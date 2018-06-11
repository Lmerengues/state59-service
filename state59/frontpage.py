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
    cursor = connections['default'].cursor()
    cursor.execute("select * from help")
    raw = dictfetchall(cursor)
    cursor.close()

    newraw = []
    for record in raw:
        record["left"] = getsecond(record["hddl"])
        record["hddl"] = datetime.strftime(record["hddl"],"%Y-%m-%d %H:%M:%S")
        record["hpublic"] = datetime.strftime(record["hpublic"],"%Y-%m-%d %H:%M:%S")
        if record["ismoney"] == 1:
            record["hmoney"] = float(record["hmoney"]) / 100
    newraw = sorted(raw, key=lambda x:x["left"])
    response = HttpResponse(json.dumps(newraw), content_type="application/json")
    return response

def detail(request):
    hno = request.GET['hno']
    cursor = connections['default'].cursor()
    cursor.execute("select * from help where hno = %s",[hno])
    raw = dictfetchall(cursor)
    cursor.close()

    newraw = raw[0]
    if newraw["ismoney"] == 1:
        newraw["hmoney"] = float(newraw["hmoney"]) / 100
    newraw["hddl"] = datetime.strftime(newraw["hddl"],"%Y-%m-%d %H:%M:%S")
    newraw["hpublic"] = datetime.strftime(newraw["hpublic"],"%Y-%m-%d %H:%M:%S")
    response = HttpResponse(json.dumps(newraw), content_type="application/json")
    return response