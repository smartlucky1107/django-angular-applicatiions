# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='aaa')),
                ('radio', models.CharField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three')], max_length=1)),
            ],
        ),
    ]
