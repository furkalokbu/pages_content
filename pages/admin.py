from django.contrib import admin
from pages.models import Page 

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_filter = ('enabled', )
    list_display = ( 'title', 'url', 'enabled')
    list_editable = ('enabled',)
    list_display_links = ('title','url')

