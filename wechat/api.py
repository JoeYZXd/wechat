from membership.models import BaseProperty
import requests
import datetime
from django.core.exceptions import ObjectDoesNotExist

class WechatApi():
    
    @classmethod
    def fetchAccessToken(cls):
        accessTokenUrl = "https://api.weixin.qq.com/cgi-bin/token"
        exists = False
        try:
            accessToken = BaseProperty.objects.get(code='WECHAT_APP_ACCESS_TOKEN')
            exists = True
            print ("exists [%s]" %(accessToken))
        except ObjectDoesNotExist:
            print ("Not Exists")
        finally:
            if not exists or accessToken.updated_at + datetime.timedelta(hours=2) < datetime.datetime.now():
                appId = BaseProperty.objects.get(code='WECHAT_APP_ID_WCB')
                appSecret = BaseProperty.objects.get(code='WECHAT_APP_SECRET_WCB')
                params = {
                    'grant_type': "client_credential",
                    'appid': appId.value,
                    'secret': appSecret.value
                }
                response = requests.get(accessTokenUrl, params = params)
                print (response.url)
                if response.status_code == 200:
                    result = response.json()
                    if 'errcode' in result:
                        print ('fetch access token failed with reason %s(%s)'
                               %(result['errmsg'], result['errcode']))
                        return
                    if exists:
                        accessToken.value = result['access_token']
                    else:
                        accessToken = BaseProperty(code='WECHAT_APP_ACCESS_TOKEN', name="乌茶邦公众号AccessToken",
                                                   value=result['access_token'])
                    print (accessToken)
                    accessToken.save()
                else:
                    response.raise_for_status()
            return accessToken.value
