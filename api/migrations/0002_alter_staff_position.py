# Generated by Django 4.0.4 on 2023-06-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('JR', 'Junior'), ('MD', 'Middle'), ('SR', 'Senior')], max_length=12),
        ),
    ]
