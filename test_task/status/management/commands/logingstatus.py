# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
import requests
from django.conf import settings
import logging

class Command(BaseCommand):
    help = "Запись данных из настроек в логи"  # noqa

    def handle(self, *args, **options):
        
        logger = logging.getLogger("status")
        
        # logger.error("megasupertest", extra={'server':'demo'})
        url = settings.REMOTE_SERVER + ':' + settings.REMOTE_PORT +'/status'
        
        status = 'Error'
        try:
            result = requests.get(url)
            if result.status_code == 200 and result.json().get('status') == 'Ok':
                status = 'Ok'
        except requests.exceptions.ConnectionError:
            pass
        # Здесь есть вариант поделить на error и info
        logger.error(status, extra={'hostname': settings.REMOTE_SERVER + ':' + settings.REMOTE_PORT})
