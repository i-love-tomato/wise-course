from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    realname = models.CharField(max_length=50)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    hobby = models.CharField(max_length=50)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    workplace = models.CharField(max_length=50)
    lastLogin = models.DateTimeField(auto_now=True)  # 上次登录时间
    c_time = models.DateField(auto_now_add=True) #注册时间
    introduction = models.CharField(max_length=100, blank=True)  #个性签名   blank=True  允许为空

    def __str__(self):
        return 'user {}'.format(self.user.username)

    class Meta:
        ordering = ['c_time']
