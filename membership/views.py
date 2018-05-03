from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from wechat.api import WechatApi
import requests

def index(request):
    return HttpResponse("Hello, World. You are at the membership index.")

def memberCard(request):
    accessToken = WechatApi.fetchAccessToken()
    fetchRedirectUrl = "https://api.weixin.qq.com/card/membercard/activate/geturl?access_token=%s" %(accessToken)
    params = {
        'card_id' : "pEFcx0aRFs-dn8gJJ2c1u0TuEcDY",
        'outer_str': '1'
    }
    response = requests.post(fetchRedirectUrl, json=params)
    print (response.text)
    result = response.json()
    return HttpResponseRedirect(result['url'])
