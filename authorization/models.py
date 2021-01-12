from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from random import randint


# Create your models here.
class User(AbstractUser):
    STATUS = (
        ('USER', "Change Own"),
        ('SUPERUSER', "Change ALL"),
    )

    status = models.CharField(max_length=12, choices=STATUS, null=True, default='USER', verbose_name='Пользователи')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Group(Group):
    class Meta:
        verbose_name = 'Группа доступа'
        verbose_name_plural = 'Группы доступа'


class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="profile")
    slug = models.SlugField(unique=True, default=str(randint(100000, 999999)))
    name = models.CharField('Имя', max_length=100, null=True)
    second_name = models.CharField('Фамилия', max_length=100, null=True)
    age = models.IntegerField(null=True)
    registration_data = models.DateField(auto_now=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name
