# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-22 17:08
from __future__ import unicode_literals

from django.db import migrations, models

LANDLORD_FIELD_DETECTORS_TO_FIX = [
    ('17bc812e-5eda-4927-8096-3f6b4bede74d', '35d6fb9f-881c-4108-b525-8dbbcabd7097', '78425541-fe21-4ede-9445-ca88ceb3fc4c'),
    ('353c94d6-b5fd-411f-9542-fec57a015dd0', '35d6fb9f-881c-4108-b525-8dbbcabd7097', '78425541-fe21-4ede-9445-ca88ceb3fc4c'),
    ('48ec554d-0a11-4e05-a1bb-6be116ba594f', '5cfa8a72-8ebd-47e6-9187-614f7d4e7e28', '78425541-fe21-4ede-9445-ca88ceb3fc4c'),
    ('77bcdf8b-ff31-4e3b-a44e-f6dc48e87cc0', '5cfa8a72-8ebd-47e6-9187-614f7d4e7e28', '78425541-fe21-4ede-9445-ca88ceb3fc4c'),
]


def replace_in_regexps(apps, ids, replace_from, replace_to):
    DocumentFieldDetector = apps.get_model('document', 'DocumentFieldDetector')
    for detector_pk, field_pk, document_type_pk in ids:
        try:
            detector = DocumentFieldDetector.objects.get(pk=detector_pk, field_id=field_pk,
                                                         document_type_id=document_type_pk)
        except:
            continue

        if detector and detector.include_regexps:
            fixed_regexp = detector.include_regexps.replace(replace_from, replace_to)
            if fixed_regexp != detector.include_regexps:
                detector.include_regexps = fixed_regexp
                detector.save()


def fix_field_detectors(apps, schema_editor):
    replace_in_regexps(apps, LANDLORD_FIELD_DETECTORS_TO_FIX, '.*:\\W*(?P<landlord>.*)',
                       '.{0,16000}:\\W*(?P<landlord>.{0,16000})')
    replace_in_regexps(apps, LANDLORD_FIELD_DETECTORS_TO_FIX, '.*:\\W*(?P<tenant>.*)',
                       '.{0,16000}:\\W*(?P<tenant>.{0,16000})')


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0065_auto_20180828_0757'),
    ]

    operations = [
        migrations.RunPython(fix_field_detectors, reverse_code=migrations.RunPython.noop),
    ]
