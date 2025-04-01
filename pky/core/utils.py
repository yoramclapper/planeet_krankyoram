from django.conf import settings


def get_my_apps():
    return [(app, app) for app in settings.MY_APPS]
