from django.conf.urls import patterns, include, url
from unit import views


urlpatterns = [
    url(r'^project/(?P<id>[\d]+)/$', views.project, name='project'),
    url(r'^project_list/(?P<page>[\d]+)/(?P<maxlist>[\d]+)/$', views.project_list, name='project_list_page_max'),
    url(r'^project_list/(?P<page>[\d]+)/$', views.project_list, name='project_list_page'),
    url(r'^project_list/$', views.project_list, name='project_list'),
    url(r'^$', views.index, name='index'),
    url(r'^delete_project/(?P<id>[\d]+)/$', views.delete_project, name='delete_project'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^edit_project/(?P<id>[\d]+)/$', views.edit_project, name='edit_project'),
    url(r'^add_unit/(?P<id>[\d]+)/$', views.add_unit, name='add_unit'),
    url(r'^edit_unit/(?P<id>[\d]+)/$', views.edit_unit, name='edit_unit'),
    url(r'^delete_unit/(?P<id>[\d]+)/$', views.delete_unit, name='delete_unit'),
    ]

