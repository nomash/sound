import django
import os


def django_setup():
    if not os.environ.get('DJANGO_SETTINGS_MODULE', None):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nomash.development")
    print('USING DJANGO %s settings' %
          os.environ.get('DJANGO_SETTINGS_MODULE', ''))
    django.setup()
