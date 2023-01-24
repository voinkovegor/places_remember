
from django.contrib import admin

from django.urls import path, include, re_path

from world.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    re_path('', include('social_django.urls', namespace='social')),
    path('memory/', MemoryListView.as_view(), name='memory'),
    path('logout/', logout_user, name='logout'),
    path('memory/new_memory/', MemoryCreateView.as_view(), name='new_memory'),
    path('memory/<int:pk>/', ShowMemory.as_view(), name='detail_memory'),
]
