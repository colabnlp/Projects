# Generated by Django 2.2 on 2019-04-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='numbers',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]