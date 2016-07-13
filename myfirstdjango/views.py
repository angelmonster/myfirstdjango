from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("hello ,ronghuaihai!")

def current_time(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s housrs(s),it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)

def current_time2(request):
    now=datetime.datetime.now()
    return render_to_response('current_time.html',{'current_time':now})
