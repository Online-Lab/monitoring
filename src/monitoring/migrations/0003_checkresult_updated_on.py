# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20150623_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkresult',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 10, 26, 57, 986537, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
