# Generated by Django 3.2.3 on 2021-05-30 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20210528_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='type',
            new_name='shortname',
        ),
    ]
