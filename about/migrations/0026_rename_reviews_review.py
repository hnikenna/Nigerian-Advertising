# Generated by Django 4.1.1 on 2022-10-19 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0025_alter_agent_headline_alter_agent_name_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
