# Generated by Django 2.1.7 on 2019-04-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0003_auto_20190202_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]