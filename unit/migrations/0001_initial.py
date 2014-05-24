# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=b'Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'name', models.CharField(max_length=80, verbose_name=b'project_name')),
                (b'city', models.CharField(max_length=80, verbose_name=b'project_city')),
                (b'year', models.IntegerField(verbose_name=b'launch_year')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'project', models.ForeignKey(to=b'unit.Project', to_field='id')),
                (b'floor', models.IntegerField(verbose_name=b'unit_floor')),
                (b'unit_no', models.IntegerField(verbose_name=b'unit_no')),
                (b'area', models.IntegerField(verbose_name=b'gross area (m2)')),
                (b'direction', models.CharField(max_length=2, verbose_name=b'direction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
