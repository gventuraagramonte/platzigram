"""Post views. === Las vistas tienen la logica de presentar los datos"""


# Django
from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Yesica Cortez',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Lactea',
        'user': 'C. Vander',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Thespianartist',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(request):

    return render(request, 'feed.html', {'posts':posts})