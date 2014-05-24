# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'unit', b'0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'unit',
            name=b'unit_no',
            field=models.IntegerField(unique=True, verbose_name=b'unit_no'),
        ),
        migrations.AlterUniqueTogether(
            name=b'project',
            unique_together=set([(b'name', b'city')]),
        ),
        migrations.AlterUniqueTogether(
            name=b'unit',
            unique_together=set([(b'project', b'floor', b'unit_no')]),
        ),
    ]
