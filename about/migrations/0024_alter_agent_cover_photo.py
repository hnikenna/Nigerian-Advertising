# Generated by Django 4.1.1 on 2022-10-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0023_alter_agent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='cover_photo',
            field=models.ImageField(blank=True, default='default/white.png', upload_to='agents/cover_photos'),
        ),
    ]
