# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(null=True, verbose_name='HTTP Status')),
                ('content', models.TextField(null=True, verbose_name='Content')),
                ('error', models.TextField(default=None, null=True, verbose_name='Error')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CheckResult',
                'verbose_name_plural': 'CheckResults',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
            },
        ),
        migrations.AddField(
            model_name='checkresult',
            name='url',
            field=models.ForeignKey(to='monitoring.Url'),
        ),
    ]
