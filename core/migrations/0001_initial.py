# Generated by Django 3.0.6 on 2020-05-06 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_code', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=32)),
                ('color_en', models.CharField(max_length=32, null=True)),
                ('color_hy', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('size_description', models.CharField(max_length=32)),
                ('size_description_en', models.CharField(max_length=32, null=True)),
                ('size_description_hy', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accessorie',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Item')),
                ('material', models.CharField(max_length=32)),
                ('material_en', models.CharField(max_length=32, null=True)),
                ('material_hy', models.CharField(max_length=32, null=True)),
            ],
            bases=('core.item',),
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Item')),
                ('material_inner', models.CharField(max_length=32)),
                ('material_inner_en', models.CharField(max_length=32, null=True)),
                ('material_inner_hy', models.CharField(max_length=32, null=True)),
                ('material_outer', models.CharField(max_length=32)),
                ('material_outer_en', models.CharField(max_length=32, null=True)),
                ('material_outer_hy', models.CharField(max_length=32, null=True)),
                ('outsole', models.CharField(max_length=32)),
                ('outsole_en', models.CharField(max_length=32, null=True)),
                ('outsole_hy', models.CharField(max_length=32, null=True)),
                ('season', models.CharField(blank=True, max_length=16)),
                ('season_en', models.CharField(blank=True, max_length=16, null=True)),
                ('season_hy', models.CharField(blank=True, max_length=16, null=True)),
            ],
            bases=('core.item',),
        ),
        migrations.CreateModel(
            name='ShoeSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='core.Size')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='core.Shoe')),
            ],
        ),
    ]
