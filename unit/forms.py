# -*- coding: utf-8 -*-
from django import forms
from unit.models import Project, Unit
from django.forms.models import inlineformset_factory

class ProjectForm(forms.ModelForm):


    name = forms.CharField(max_length=128, help_text= u"Proje Adı",
                              widget=forms.TextInput(attrs={'class': 'form-control','id':'focusedInput',}))
    city = forms.CharField(max_length=50, help_text= u"Projenin Şehri",
                              widget=forms.TextInput(attrs={'class': 'form-control','id':'focusedInput',}))
    year = forms.IntegerField(max_value=2100,min_value=1980, initial=2004, help_text= u"Projenin Yılı",
                              widget=forms.NumberInput(attrs={'class': 'form-control','id':'focusedInput','size':'4',}))


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Project
        fields = ('name', 'city', 'year')

class UnitForm(forms.ModelForm):
    #project = forms.ModelChoiceField(queryset = Project.objects.all(), help_text= u"Proje",)

    directions = [('K', 'G', 'D', 'B', 'KB', 'KD', 'GB', 'GD',)]
    DIRECTIONS = (
    ('K', 'Kuzey'),
    ('G', 'Güney'),
    ('D', 'Doğu'),
    ('B', 'Batı'),
    ('KD', 'Kuzey Doğu'),
    ('KB', 'Kuzey Batı'),
    ('GD', 'Güney Doğu'),
    ('GB', 'Güney Batı'),
                )
    floor = forms.IntegerField(max_value=200,min_value=-200, initial=1, help_text= u"Kat",
                              widget=forms.NumberInput(attrs={'class': 'form-control','id':'focusedInput','size':'2',}))
    unit_no = forms.IntegerField(max_value=999,min_value=0, initial=1, help_text= u"Daire No",
                              widget=forms.NumberInput(attrs={'class': 'form-control','id':'focusedInput','size':'3',}))
    area = forms.IntegerField(max_value=999,min_value=0, initial=1, help_text= u"Alan (m2)",
                              widget=forms.NumberInput(attrs={'class': 'form-control','id':'focusedInput','size':'3',}))
    direction = forms.ChoiceField(choices=DIRECTIONS, help_text= u"Daire Yönü",
                              widget=forms.Select(attrs={'class': 'form-control','id':'select','size':'3',}))

    class Meta:
        model = Unit
        exclude = ['project']




#UnitFormSet = inlineformset_factory(Unit, Project)