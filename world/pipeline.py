from .models import *

from django.contrib.auth import logout


def get_avatar(backend, response, user=None, *args, **kwargs):

    url = None

    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

    if backend.name == 'google-oauth2':
        url = response.get('picture', '')

    if url:
        user.avatar = url
        user.save()
        print(user.avatar)


def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}