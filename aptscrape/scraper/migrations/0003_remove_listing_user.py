# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20160504_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
    ]
