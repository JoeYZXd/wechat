from django.db import models

class Member(models.Model):
    wechatId = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    mobile = models.CharField(max_length=16)
    birthday = models.DateField("birthday")

    def __str__(self):
        return self.nickname

class BaseProperty(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    status = models.BooleanField(default=True)
    value = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%d]%s:%s %s,%s" %(self.id, self.code, self.value, self.created_at, self.updated_at)
