# Generated by Django 3.0.3 on 2020-03-03 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200304_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='grage',
            new_name='garage',
        ),
    ]
