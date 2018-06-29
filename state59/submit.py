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
	cursor = connections['default'].cursor()
	cursor.execute("select * from help where hno = %s",str(hno))
	raw = dictfetchall(cursor)
	cursor.close()

	newraw = raw[0]
	if newraw["ismoney"] == 1:
		newraw["hmoney"] = float(newraw["hmoney"]) / 100
	newraw["hddl"] = datetime.strftime(newraw["hddl"],"%Y-%m-%d %H:%M:%S")
	newraw["hpublic"] = datetime.strftime(newraw["hpublic"],"%Y-%m-%d %H:%M:%S")
	response = HttpResponse(json.dumps(newraw), content_type="application/json")
	return response
