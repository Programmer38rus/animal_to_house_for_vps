from django.db import models
from datetime import datetime


# Create your models here.
class Kind(models.Model):
    name = models.CharField(max_length=50, verbose_name="Вид", null=True, blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=13, verbose_name='Кличка')
    description = models.TextField(verbose_name='О питомце')
    receipt_date = models.DateField(auto_now=True, verbose_name="Поступил")
    face = models.ImageField(upload_to='pets_foto', blank=True, verbose_name="Фотография")
    birth_data = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    MALE = 'Мальчик'
    FEMALE = 'Девочка'
    GENDER = [(MALE, "Мальчик"), (FEMALE, "Девочка"), ]

    gender = models.CharField(max_length=10, choices=GENDER, verbose_name='Пол', null=True)

    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Вид")

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Добавить животное"

    @property
    def age(self):
        age = int((datetime.now().date() - self.birth_data).days / 31)

        if age < 12:
            last_simbol = age % 10
            if last_simbol == 1:
                return f'{age} месяц'
            elif last_simbol in (2, 3, 4):
                return f'{age} месяца'
            elif age % 100 in range(5, 21):
                return f'{age} месяцев'
        if age > 12:
            age = int(age / 12)
            last_simbol = age % 10
            if last_simbol == 1:
                return f'{age} год'
            elif last_simbol in (2, 3, 4):
                return f'{age} года'
            elif age % 100 in range(5, 21):
                return f'{age} лет'

    def __str__(self):
        return self.name
