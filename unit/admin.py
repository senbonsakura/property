from django.contrib import admin
from unit.models import Project, Unit

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["name","city","year","id"]
    inlines =[UnitInline,]

class UnitAdmin(admin.ModelAdmin):
    model = Unit
    list_display = ["project","floor","unit_no","area","direction","id"]
    list_display_links = ["floor","unit_no"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Unit, UnitAdmin)



