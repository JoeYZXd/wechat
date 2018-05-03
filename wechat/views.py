from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from .api import WechatApi

def wx(request):
    parameters = request.GET
    signature = parameters.get('signature')
    timestamp = parameters.get('timestamp')
    nonce = parameters.get('nonce')
    echostr = parameters.get('echostr')
    token = "wuchabangwuxihuishanwanda"
    sortedList = [token, timestamp, nonce]
    sortedList.sort()
    s = "".join(sortedList)
    print (s)
    hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()
    print ("handle/GET func: hashcode, signature: ", hashcode, signature)
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("error")

def accessToken(request):
    WechatApi.fetchAccessToken()
    return HttpResponse("Success")
