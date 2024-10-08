# Generated by Django 5.0.6 on 2024-08-19 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_add_alter_cat_cimage'),
        ('userapp', '0002_cont'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('cartproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.add')),
                ('cartuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.reg')),
            ],
        ),
    ]
