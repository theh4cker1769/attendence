# Generated by Django 4.0.2 on 2022-02-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
    ]