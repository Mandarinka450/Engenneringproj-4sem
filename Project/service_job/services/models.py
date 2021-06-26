from django.db import models


STATUS_CHOICES = [
    ('2300', '2300'),
    ('580', '580'),
    ('3200', '3200'),
]


class Services(models.Model):
    id_service = models.AutoField(primary_key=True)
    title = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание услуги')
    tariff_plan = models.CharField('Тарифный план', max_length=255)
    price = models.IntegerField('Цена(в руб.)')
    id_specialist = models.IntegerField('ID специалиста')
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


    def __str__(self):
        return self.title





class Specialist(models.Model):
     id_specialist = models.ForeignKey(Services, on_delete=models.CASCADE)
     name = models.CharField('Имя специалиста', max_length=55)
     surname = models.CharField('Фамилия специалиста', max_length=255)
     description = models.TextField('О специалисте')
     class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

     def __str__(self):
        return self.name


