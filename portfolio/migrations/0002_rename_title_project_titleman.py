# Generated by Django 3.2.4 on 2021-06-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='titleman',
        ),
    ]