# Generated by Django 4.1.1 on 2022-10-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0027_alter_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('0', 'Pending'), ('1', 'Approved')], max_length=250),
        ),
    ]
