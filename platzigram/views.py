"""Platzigram views"""

"""Django"""
from django.http import HttpResponse

"""Utilities"""
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting. Funcion que retorna una respuesta a traves de la urlpatterns"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def hi(request):
    """Mostrar unos numeros enviados por GET del url en forma de JSON"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers':sorted_ints,
        'message':'integers sorted succesfull'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
        )

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}! Welcome to Platzigram'.format(name)
    
        return HttpResponse(message)