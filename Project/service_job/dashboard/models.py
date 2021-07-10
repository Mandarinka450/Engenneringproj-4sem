from django.db import models

class Category(models.Model):
    category = models.CharField('Название категории', max_length=100)
    description = models.TextField('Описание категории')
    salary_of_mounth = models.IntegerField('Средняя заработная плата (руб/мес)')
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


    def __str__(self):
       return self.category
