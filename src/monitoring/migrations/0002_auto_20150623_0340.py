# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkresult',
            name='url',
            field=models.ForeignKey(related_name='checks', to='monitoring.Url'),
        ),
    ]
