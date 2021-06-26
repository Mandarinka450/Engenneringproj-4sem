from django.db import models

class Articles(models.Model):
    id_articles = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок статьи', max_length=55)
    description = models.TextField('Содержимое статьи')
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


    def __str__(self):
        return self.title


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок новости', max_length=55)
    description = models.TextField('Описание новости')
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

