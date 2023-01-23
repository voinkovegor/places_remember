from .models import *

def get_avatar(backend, response, user=None, *args, **kwargs):

    url = None
    print(backend.name)
    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

    if backend.name == 'google-oauth2':
        url = response.get('picture', '')

    if url:
        user.avatar = url
        user.save()
        print(user.avatar)