# Generated by Django 4.1.1 on 2022-09-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0022_alter_agent_headline_alter_agent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
