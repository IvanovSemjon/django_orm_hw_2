# Generated by Django 5.1.2 on 2024-11-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_id_alter_phone_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
