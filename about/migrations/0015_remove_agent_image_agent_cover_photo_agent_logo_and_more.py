# Generated by Django 4.1.1 on 2022-09-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_state_remove_agent_state_agent_states'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='image',
        ),
        migrations.AddField(
            model_name='agent',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='agents/cover_photos'),
        ),
        migrations.AddField(
            model_name='agent',
            name='logo',
            field=models.ImageField(blank=True, upload_to='agents/logos'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='states',
            field=models.ManyToManyField(blank=True, null=True, to='about.state'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(blank=True, choices=[('Abuja', 'Abuja'), ('Lagos', 'Lagos'), ('Rivers', 'Rivers'), ('Oyo', 'Oyo'), ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Plateau', 'Plateau'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=30, null=True, unique=True),
        ),
    ]
