Веб-приложение, с помощью которого люди могут хранить свои впечатления о посещаемых местах с отметками на карте (GeoDjango)

Реализовано:
* Авторизация через социальные сети
* Получение списка воспоминаний для каждого пользователя
* Добавление воспоминаний
* Просмотр и редактирование воспоминаний
* Покрыто unit-тестами, тест покрытия coverage


    Coverage report:
    Name                                                                   Stmts   Miss  Cover
    ------------------------------------------------------------------------------------------
    geodjango/__init__.py                                                      0      0   100%
    geodjango/asgi.py                                                          4      4     0%
    geodjango/settings.py                                                     32      0   100%
    geodjango/urls.py                                                          4      0   100%
    geodjango/wsgi.py                                                          4      4     0%
    manage.py                                                                 12      2    83%
    world/__init__.py                                                          0      0   100%
    world/admin.py                                                             6      0   100%
    world/apps.py                                                              4      0   100%
    world/forms.py                                                             7      0   100%
    world/load.py                                                              8      8     0%
    world/migrations/0001_initial.py                                          11      0   100%
    world/migrations/0002_remove_user_nickname_user_avatar_user_image.py       4      0   100%
    world/migrations/0003_alter_user_avatar.py                                 4      0   100%
    world/migrations/__init__.py                                               0      0   100%
    world/models.py                                                           39      2    95%
    world/pipeline.py                                                         21     21     0%
    world/tests/__init__.py                                                    0      0   100%
    world/tests/test_api.py                                                   58      0   100%
    world/views.py                                                            50      8    84%
    ------------------------------------------------------------------------------------------
    TOTAL                                                                    268     49    82%