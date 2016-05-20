# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_auto_20160520_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=58, choices=[('Dublin', 'dublin'), ('Cavan', 'cavan'), ('Kilkenny', 'kilkenny'), ('Meath', 'meath')]),
        ),
    ]
