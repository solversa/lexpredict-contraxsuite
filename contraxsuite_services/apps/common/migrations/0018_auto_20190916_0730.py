# Generated by Django 2.2.4 on 2019-09-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_methodstatscollectorplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodstatscollectorplugin',
            name='batch_size',
            field=models.PositiveSmallIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='methodstatscollectorplugin',
            name='batch_time',
            field=models.PositiveSmallIntegerField(blank=True, default=60, null=True),
        ),
    ]
