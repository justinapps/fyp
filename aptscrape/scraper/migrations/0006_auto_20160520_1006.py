# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_auto_20160520_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
