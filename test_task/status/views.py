# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.shortcuts import render

from datetime import date
import json
import subprocess
from django.http import HttpResponse
from django.views.generic import View

class StausView(View):

    def get(self, request):
        '''
        Метод возвращает информацию по текущей машине и дату
        :param request:
        :return: json
        '''
        try:
            o = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            message = o.stdout.strip()
        # Знаю, что сюда надо вставлять AtributError, а еще лучше все конструкцию вынести в отдельную функцию, очень неудобно было дебажить на 2.7
        except:
            message = subprocess.check_output("uname -a", shell=True)
        
        result = {
            'host': message.strip(),
            'date': str(date.today()),
            'status': 'Ok'
        }

        return HttpResponse(json.dumps(result), content_type='application/json')
