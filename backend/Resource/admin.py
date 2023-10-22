from django.contrib import admin
from Resource.models import Type

admin.site.site_header = "Tableau de Bord - TEAM3"

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)