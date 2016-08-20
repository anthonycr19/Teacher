# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20160819_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(related_name='students', to='snippets.Student'),
        ),
    ]
