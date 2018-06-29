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

def getpastsecond(date):
    now = datetime.now()
    date = date.replace(tzinfo=None)
    return (now - date).seconds
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

    cursor = connections['default'].cursor()
    cursor.execute("select * from review where hno = %s",[hno])
    raw = dictfetchall(cursor)
    cursor.close()

    for record in raw:
        record["past"] = getpastsecond(record["rdate"])
        record["rdate"] = datetime.strftime(record["rdate"],"%Y-%m-%d %H:%M:%S")

    reviewlaw = sorted(raw, key=lambda x:x["past"])
    newraw["review"] = reviewlaw
    newraw["rcount"] = len(reviewlaw)
    response = HttpResponse(json.dumps(newraw), content_type="application/json")
    return response

def reply_post(request):
    ptype = request.GET['ptype']
    cursor = connections['default'].cursor()
    cursor.execute("select * from posts where ptype = %s",[ptype])
    raw = dictfetchall(cursor)
    cursor.close()

    newraw = []
    for record in raw:
        record["past"] = getpastsecond(record["ppublish"])
        record["ppublish"] = datetime.strftime(record["ppublish"],"%Y-%m-%d %H:%M:%S")
    newraw = sorted(raw, key=lambda x:x["past"])
    response = HttpResponse(json.dumps(newraw), content_type="application/json")
    return response