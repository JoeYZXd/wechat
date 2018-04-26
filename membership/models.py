from django.db import models

class Member(models.Model):
    wechatId = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    mobile = models.CharField(max_length=16)
    birthday = models.DateField("birthday")

    def __str__(self):
        return self.nickname
