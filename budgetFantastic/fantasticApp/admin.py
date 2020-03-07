from django.contrib import admin

from .models import Category, Overall, User, Entry

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Entry)
admin.site.register(Overall)