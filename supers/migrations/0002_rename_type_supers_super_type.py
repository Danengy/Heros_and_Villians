# Generated by Django 4.1.2 on 2022-10-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supers',
            old_name='type',
            new_name='super_type',
        ),
    ]