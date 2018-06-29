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

def index(request):

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

def submitinfo(request):
	hno = request.GET['hno']
	phone = request.GET['phone']
	wxnumber = request.GET['wxnumber']
	note = request.GET['note']
	uid = request.GET['uid']
	cursor = connections['default'].cursor()
	cursor.execute("insert into help_accept (hhno,mobile,wechatnum,accepted_label,message,uid) values(%s,%s,%s,%d,%s,%s)",[hno,phone,wxnumber,0,note,uid])
	raw = dictfetchall(cursor)
	cursor.close()

	response = HttpResponse(json.dumps(raw), content_type="application/json")
	return response