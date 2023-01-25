
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView, UpdateView

from .forms import AddMemoryForm, UpdateMemoryForm
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

# Пытался сделать переавторизацию
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_exempt
# from social_core.actions import do_complete
# from social_django.utils import psa
# from social_django.views import _do_login
#
# @never_cache
# @csrf_exempt
# @psa('social:complete')
# def complete(request, backend, *args, **kwargs):
#     """Override this method so we can force user to be logged out."""
#     return do_complete(request.backend, _do_login, user=None,
#                        redirect_name=REDIRECT_FIELD_NAME, request=request,
#                        *args, **kwargs)


def logout_user(request):
    logout(request)
    return redirect('main')


class MemoryCreateView(LoginRequiredMixin, CreateView):
    form_class = AddMemoryForm
    template_name = 'world/new_memory.html'

    def get_success_url(self):
        return reverse_lazy('memory')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowMemory(LoginRequiredMixin, UpdateView):
    template_name = 'world/detail_memory.html'
    model = Memory
    form_class = UpdateMemoryForm


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['memory']
        return context

    def get_success_url(self):
        return reverse_lazy('memory')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)