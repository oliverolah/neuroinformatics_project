# Generated by Django 3.2.9 on 2022-03-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitdata', '0002_alter_submitdata_submitfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitdata',
            name='title',
            field=models.TextField(max_length=50, verbose_name='Title'),
        ),
    ]