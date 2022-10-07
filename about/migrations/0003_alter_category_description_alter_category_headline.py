# Generated by Django 4.1.1 on 2022-09-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_category_description_category_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='headline',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
