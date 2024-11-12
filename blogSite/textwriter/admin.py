from django.contrib import admin
from textwriter.models import Textwriter

class TextwriterAdmin(admin.ModelAdmin):
    list_display = ('Book_category','title','author','coverImage','body')

admin.site.register(Textwriter,TextwriterAdmin)
# Register your models here.
