from django.contrib import admin
from .models import Note

# Register the Note model with Django's admin
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created', 'updated')
    search_fields = ('body',)