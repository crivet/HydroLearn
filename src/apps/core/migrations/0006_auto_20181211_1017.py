# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-11 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_collaboration_table_addition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_objective',
            name='outcomes',
            field=models.ManyToManyField(blank=True, to='core.Learning_Outcome'),
        ),
    ]
