# Generated by Django 4.1.1 on 2022-09-22 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_keywords_pricing_alter_subcategory_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Keywords',
            new_name='Keyword',
        ),
    ]
