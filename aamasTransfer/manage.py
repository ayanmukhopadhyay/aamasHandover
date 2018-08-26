#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aamasWeb.settings")

    from django.core.cache import cache
    from django.core.management import execute_from_command_line
    cache.clear()
    execute_from_command_line(sys.argv)
