from django.http import HttpResponse

import json
from django.db import connections

def index(request):
    hno = request.GET['hno']
    raw = {"id":1,"text":"xxx"}
    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response