"""
WSGI config for aamasWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
#added for debugging python version issue on server
import sys

#import logging
#with open("/home/mukhopa/log.txt","w+") as dest:
#    dest.write(sys.version)
# logger = logging.getLogger(__name__)
#
# logger.debug(sys.version)

# add the virtualenv site-packages path to the sys.path
#sys.path.append('/home/mukhopa/.local/lib/python3.5/site-packages/')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aamasWeb.settings")

application = get_wsgi_application()
