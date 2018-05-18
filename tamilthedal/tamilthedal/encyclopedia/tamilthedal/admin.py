from encyclopedia.tamilthedal.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    #list_filter = ['key_en']
    search_fields = ['key_en', 'key_ta']

admin.site.register(Entry, EntryAdmin)
