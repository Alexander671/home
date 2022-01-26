
from django.core.files import File
from django.utils import timezone, dateformat
from .models import Request
from requests import get
def printHello():
    now = timezone.now().replace(second=0, microsecond=0)
    print(now)
    req = list(Request.objects.filter(time_request=now))
    print(req)
    ###############################################


    for i in range(len(req)):
        if(req[i].url == 'ON'):
            req[i].response = get("http://192.168.2.7/LED=OFF")
        if(req[i].url == 'OFF'):
            req[i].response = get("http://192.168.2.7/LED=ON")

    print(req)
    Request.objects.bulk_update(req, ["response"])
    ###############################################
