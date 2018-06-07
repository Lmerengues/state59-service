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
    day_min = date.split()
    year = day_min[0].split('-')[0]
    month = day_min[0].split('-')[1]
    day = day_min[0].split('-')[2]
    hour = day_min[1].split(':')[0]
    minute = day_min[1].split(':')[1]
    dt = datetime(int(year), int(month), int(day), int(hour), int(minute))
    return (dt - now).seconds

def index(request):


    cursor = connections['default'].cursor()
    cursor.execute("select * from task")
    raw = dictfetchall(cursor)
    cursor.close()

    for record in raw:
        record["left"] = getsecond(record["tddl"])
    raw = sort(raw, key=lambda x:x["left"])

    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response
