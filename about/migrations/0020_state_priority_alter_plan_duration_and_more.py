# Generated by Django 4.1.1 on 2022-09-27 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0019_remove_pricing_features_remove_pricing_price1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='duration',
            field=models.CharField(choices=[('Year', 'Annually'), ('Month', 'Monthly')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='plan1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price1', to='about.plan'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='plan2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price2', to='about.plan'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='plan3',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price3', to='about.plan'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(blank=True, choices=[('Remote', 'Remote'), ('Abuja', 'Abuja'), ('Lagos', 'Lagos'), ('Rivers', 'Rivers'), ('Oyo', 'Oyo'), ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Plateau', 'Plateau'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'), ('All Nigeria', 'All Nigeria')], max_length=30, null=True, unique=True),
        ),
    ]
