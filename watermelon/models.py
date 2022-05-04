from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Card(models.Model):
    card = models.CharField(max_length=50)

    class Meta:
        verbose_name = '显卡型号'
        verbose_name_plural = verbose_name

class User(models.Model):
    user = models.CharField(max_length=20)

    class Meta:
        verbose_name = '主用人'
        verbose_name_plural = verbose_name

class Information(models.Model):
    ip = models.CharField('ip地址', max_length=50)
    cpu = models.CharField('cpu型号', max_length=100)
    gpu = models.CharField('gpu型号', max_length=100)
    passwd = models.CharField('密码', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    car = models.ForeignKey(Card, verbose_name='显卡型号', on_delete=models.CASCADE)
    user = models.ManyToManyField(User, verbose_name='主用人', blank=True)

    def get_absolute_url(self):
        return reverse('watermelon:detail', kwargs={'pk': self.pk})