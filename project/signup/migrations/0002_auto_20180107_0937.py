# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(default=b'ML', max_length=2, choices=[(b'ML', b'Male'), (b'FM', b'Female')]),
        ),
    ]
