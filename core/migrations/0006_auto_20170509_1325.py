# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170509_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pp',
            field=models.ImageField(default='images/profile.jpg', upload_to='images/'),
        ),
    ]