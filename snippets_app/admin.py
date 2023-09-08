from django.contrib import admin
from .models import Snippet, Tag, Language

# Register your models here.
admin.site.register(Snippet)
admin.site.register(Tag)
admin.site.register(Language)