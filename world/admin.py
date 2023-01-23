from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin
from .models import *

admin.site.register(WorldBorder, admin.GISModelAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Memory, admin.GISModelAdmin)

