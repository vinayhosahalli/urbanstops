# Generated by Django 2.2.5 on 2019-12-02 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='remark',
        ),
    ]
