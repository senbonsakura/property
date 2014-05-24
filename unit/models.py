from django.db import models

class Project(models.Model):
    name = models.CharField('project_name', max_length=80)
    city = models.CharField('project_city', max_length=80)
    year = models.IntegerField('launch_year')
    # date = models.DateField('start_date')

    class Meta:
        unique_together = ('name', 'city',)

    def __unicode__(self):
        return self.name + " (" + self.city + ")"


class Unit(models.Model):
    project = models.ForeignKey(Project)
    floor = models.IntegerField('unit_floor')
    unit_no = models.IntegerField('unit_no', unique=True)
    area = models.IntegerField('gross area (m2)')
    direction = models.CharField('direction', max_length=2)

    class Meta:
        unique_together = ('project', 'floor','unit_no',)

    def __unicode__(self):
        return u"Unit {0} of {1}".format(self.unit_no, self.project)
