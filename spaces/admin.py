from django.contrib import admin
from .models import (
    Space,
    Tag
)

# Register your models here.

admin.site.register(Space)
admin.site.register(Tag)
