from audioop import reverse

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import AddMemoryForm
from .models import *


class MemoryListView(LoginRequiredMixin, generic.ListView):
    model = Memory
    template_name = 'world/list_memories.html'

    extra_context = {'title': 'Список воспоминаний'}

    def get_queryset(self):
        return Memory.objects.filter(user_id=self.request.user.pk)

# class AddMemory(CreateView):      класс добавления нового воспоминания (ур № 15)
#     form_class =


def index(request):
    return render(request, 'world/index.html')

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


def show_memory(request):
    return render(request, 'world/detail_memory.html')


class MemoryCreateView(LoginRequiredMixin, CreateView):
    form_class = AddMemoryForm

    # model = Memory
    template_name = 'world/new_memory.html'
    # fields = ['title', 'description', 'location']

    def get_success_url(self):
        return reverse_lazy('memory')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)