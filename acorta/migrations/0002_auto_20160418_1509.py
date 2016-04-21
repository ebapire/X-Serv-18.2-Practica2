# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_reales',
            name='num',
        ),
        migrations.RemoveField(
            model_name='url_reales',
            name='url',
        ),
        migrations.AddField(
            model_name='url_reales',
            name='url_corta',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='url_reales',
            name='url_larga',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
