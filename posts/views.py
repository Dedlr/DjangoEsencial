# Django

from django.http import HttpResponse

#Utilities
from datetime import datetime

posts=[
    {
        'name':'Mont Blac',
        'user':'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://nichecanvas.com/cdn/shop/products/artwork_5a23aaf9-c8d3-4893-825f-17ef0a0509b6_256x256.jpg?v=1634754511',
    },
    {
        'name':'Via Lactea',
        'user':'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://i.pinimg.com/originals/b3/fe/bf/b3febf26db015be223f3c1068e3a6394.jpg',
    },
        {
        'name':'Nuevo Auditorio',
        'user':'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://www.tn23.tv/wp-content/uploads/2023/08/Difusores-Acusticos-256x256.jpg',
    }
]


def list_posts(request):

    content=[]

    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
            """.format(**post))
    return HttpResponse('<br>'.join(content))
