# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-02-05 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imanage_integration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imanagedocument',
            name='imanage_doc_number',
            field=models.CharField(blank=True, db_index=True, max_length=1024, null=True),
        ),
    ]
