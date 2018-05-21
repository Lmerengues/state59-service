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



    raw = {"id":1,"text":"xxx"}

    cursor = connections['default'].cursor()
    cursor.execute("select * from homework limit 10")

    raw = dictfetchall(cursor)
    cursor.close()




    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response



