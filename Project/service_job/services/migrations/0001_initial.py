# Generated by Django 3.2.4 on 2021-06-13 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id_service', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('tariff_plan', models.CharField(max_length=255, verbose_name='Тарифный план')),
                ('price', models.IntegerField(verbose_name='Цена(в руб.)')),
                ('id_specialist', models.IntegerField(verbose_name='ID специалиста')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Имя специалиста')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия специалиста')),
                ('description', models.TextField(verbose_name='О специалисте')),
                ('id_specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
            },
        ),
    ]
