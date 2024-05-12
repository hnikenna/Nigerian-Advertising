# Generated by Django 4.1.1 on 2022-09-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_alter_agent_description_alter_agent_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='avatar',
        ),
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.ImageField(blank=True, upload_to='agents'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='subcategories'),
        ),
    ]
