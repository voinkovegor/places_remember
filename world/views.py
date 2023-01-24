from django.contrib import gis
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.forms import OSMWidget
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import AddMemoryForm
from .models import *


class MemoryListView(LoginRequiredMixin, ListView):
    model = Memory
    template_name = 'world/list_memories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список воспоминаний'
        return context

    def get_queryset(self):
        return Memory.objects.filter(user_id=self.request.user.pk)


def index(request):
    return render(request, 'world/index.html', {'title': 'Главная страница'})

def logout_user(request):
    logout(request)
    return redirect('/')


# def add_memory(request):
#     if request.method == 'POST':
#         form = AddMemoryForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = AddMemoryForm()
#     return render(request, 'world/new_memory.html', {'title': "Добавить воспоминание", 'form': form})


# def show_memory(request):
#     return render(request, 'world/detail_memory.html')


class MemoryCreateView(LoginRequiredMixin, CreateView):
    form_class = AddMemoryForm
    template_name = 'world/new_memory.html'

    def get_success_url(self):
        return reverse_lazy('memory')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowMemory(LoginRequiredMixin, DetailView):
    model = Memory
    template_name = 'world/detail_memory.html'
    context_object_name = 'memory'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['memory']
        # context['location'] = gis.forms.PointField(widget=gis.forms.OSMWidget())
        return context