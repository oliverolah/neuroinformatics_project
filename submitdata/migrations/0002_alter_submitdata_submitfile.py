# Generated by Django 3.2.9 on 2022-01-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitdata',
            name='submitFile',
            field=models.FileField(upload_to='submitdata/', verbose_name='Submitted File(s)'),
        ),
    ]
