import os
# Overrides
from .settings import *  # noqa: F401


DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     },
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# TODO-specific settings
TODO_STAFF_ONLY = False
TODO_DEFAULT_LIST_SLUG = 'tickets'
TODO_DEFAULT_ASSIGNEE = None
TODO_PUBLIC_SUBMIT_REDIRECT = '/'