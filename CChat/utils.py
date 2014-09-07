# -*- coding: utf-8 -*-
from django.conf import settings
import random
import string
__author__ = 'D.Ivanets'


def random_string(length):
    """
    Returns random string of requested length, which contains uppercase letters, lowercase letters and numbers
    :length: Length of requested random string.
    :return: Random string of requested length.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def save_file(new_file, path):
    """
    Little helper to save a file
    """
    fd = open('%s/%s' % (settings.MEDIA_ROOT, str(path)), 'wb')
    for chunk in new_file.chunks():
        fd.write(chunk)
    fd.close()