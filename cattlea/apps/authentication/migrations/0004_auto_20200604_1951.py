# Generated by Django 3.0.6 on 2020-06-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200604_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment_address',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='building_address',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
