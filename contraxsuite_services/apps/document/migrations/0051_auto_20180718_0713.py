# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-18 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0050_migrate_doc_size_20180706_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfieldvalue',
            name='removed_by_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicaldocumentfieldvalue',
            name='removed_by_user',
            field=models.BooleanField(default=False),
        ),
    ]
