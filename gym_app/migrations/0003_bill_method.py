# Generated by Django 3.2.3 on 2021-07-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_auto_20210715_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='method',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
