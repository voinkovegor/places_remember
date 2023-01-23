from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic

from .models import *


class MemoryListView(LoginRequiredMixin, generic.ListView):
    model = Memory
    template_name = 'world/list_memories.html'


    def get_queryset(self):
        return Memory.objects.filter(user_id=self.request.user.pk)

# class AddMemory(CreateView):      класс добавления нового воспоминания (ур № 15)
#     form_class =


def index(request):
    return render(request, 'world/index.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def add_memory(request):
    return render(request, 'world/new_memory.html')


# def show_memory(request):
#     return render(request, 'world/detail_memory.html')