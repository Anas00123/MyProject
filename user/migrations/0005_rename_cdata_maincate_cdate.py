# Generated by Django 3.2.4 on 2022-09-03 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220903_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincate',
            old_name='cdata',
            new_name='cdate',
        ),
    ]
