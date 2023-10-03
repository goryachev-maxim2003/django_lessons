from django.contrib import admin
from .models import Category, Owner, Djaba

# Register your models here.
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Djaba)