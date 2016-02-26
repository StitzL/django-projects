# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_id', models.SlugField(max_length=4, primary_key=True, serialize=False)),
                ('long_url', models.URLField(max_length=2000)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]