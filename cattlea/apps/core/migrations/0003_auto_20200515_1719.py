# Generated by Django 3.0.6 on 2020-05-15 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200515_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='color',
            new_name='colors',
        ),
    ]
