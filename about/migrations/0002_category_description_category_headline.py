# Generated by Django 4.1.1 on 2022-09-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='headline',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
