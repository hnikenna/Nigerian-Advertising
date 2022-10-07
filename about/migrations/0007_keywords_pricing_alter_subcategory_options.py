# Generated by Django 4.1.1 on 2022-09-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_subcategory_alter_service_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'subcategories'},
        ),
    ]
