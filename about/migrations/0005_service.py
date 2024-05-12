# Generated by Django 4.1.1 on 2022-09-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_category_headline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('headline', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='about.category')),
            ],
        ),
    ]
