# Generated by Django 5.1.2 on 2024-10-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='Наименование модели')),
                ('price', models.IntegerField(max_length=500, verbose_name='Цена')),
                ('image', models.URLField()),
                ('release_date', models.DateTimeField(verbose_name='Дата выхода')),
                ('lte_exists', models.BooleanField(default=True, verbose_name='Наличие LTE')),
                ('slug', models.SlugField()),
            ],
        ),
    ]