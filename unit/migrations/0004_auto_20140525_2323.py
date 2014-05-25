# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0003_auto_20140525_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='block',
            field=models.CharField(default='', max_length=10, verbose_name=b'block'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together=set([(b'project', b'block', b'floor', b'unit_no')]),
        ),
    ]
