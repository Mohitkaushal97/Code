# Generated by Django 3.1.2 on 2020-10-09 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formm',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='formm',
            name='lname',
        ),
    ]
