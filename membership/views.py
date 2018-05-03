from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from wechat.api import WechatApi
import requests

def index(request):
    return HttpResponse("Hello, World. You are at the membership index.")

def memberCard(request):
    print ("--------------------------")
    print ("request info %s" % request.GET)
    print ("--------------------------")
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

def enableMemberCardBalance(request):
    accessToken = WechatApi.fetchAccessToken()
    enableMemberCardBalanceUrl = "https://api.weixin.qq.com/card/update?access_token=%s" %(accessToken)
    params = {
        "card_id" : "pEFcx0aRFs-dn8gJJ2c1u0TuEcDY",
        "member_card" : {
            "supply_balance" : True
        }
    }
    response = requests.post(enableMemberCardBalanceUrl, json=params)
    print (response.text)
    return HttpResponse(response.text)

def addBonus(request):
    accessToken = WechatApi.fetchAccessToken()
    enableMemberCardBalanceUrl = "https://api.weixin.qq.com/card/membercard/updateuser?access_token=%s" %(accessToken)
    params = {
        "card_id" : "pEFcx0aRFs-dn8gJJ2c1u0TuEcDY",
        "member_card" : {
            "supply_balance" : True
        }
    }
    response = requests.post(enableMemberCardBalanceUrl, json=params)
    print (response.text)
    return HttpResponse(response.text)
