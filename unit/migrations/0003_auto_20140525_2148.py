# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0002_auto_20140524_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='unit_no',
            field=models.IntegerField(verbose_name=b'unit_no'),
        ),
    ]
