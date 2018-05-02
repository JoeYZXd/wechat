from django.shortcuts import render
from django.http import HttpResponse
import hashlib

def wx(request):
    parameters = request.GET
    signature = parameters.get('signature')
    timestamp = parameters.get('timestamp')
    nonce = parameters.get('nonce')
    echostr = parameters.get('echostr')
    token = "wuchabangwuxihuishanwanda"
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print ("handle/GET func: hashcode, signature: ", hashcode, signature)
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("error")
