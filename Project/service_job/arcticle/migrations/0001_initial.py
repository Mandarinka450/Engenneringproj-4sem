# Generated by Django 3.2.4 on 2021-06-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id_articles', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=55, verbose_name='Заголовок статьи')),
                ('description', models.TextField(verbose_name='Содержимое статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=55, verbose_name='Заголовок новости')),
                ('description', models.TextField(verbose_name='Описание новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
