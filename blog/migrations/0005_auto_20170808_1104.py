# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170808_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
