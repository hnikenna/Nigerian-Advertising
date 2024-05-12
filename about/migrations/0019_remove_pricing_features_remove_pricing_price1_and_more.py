# Generated by Django 4.1.1 on 2022-09-26 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0018_feature_pricing_price1_pricing_price2_pricing_price3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='features',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='price3',
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(default=0)),
                ('duration', models.CharField(choices=[('Year', 'Annually')], max_length=100)),
                ('features', models.ManyToManyField(to='about.feature')),
            ],
        ),
        migrations.AddField(
            model_name='pricing',
            name='plan1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price1', to='about.plan'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='plan2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price2', to='about.plan'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='plan3',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price3', to='about.plan'),
        ),
    ]
