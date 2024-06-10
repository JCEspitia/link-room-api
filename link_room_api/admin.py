from django.contrib import admin
from .models import Link, Tag, Category

# Register your models here.

admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Tag)
