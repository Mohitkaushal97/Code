# Generated by Django 3.1.2 on 2020-10-09 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
