from django.shortcuts import render
from .models import Article

"""
GET - Get the page/information
POST - Upload information
PUT - Update information
DELETE - Delete information
"""


def index(request):
    if request.method == 'GET':
        articles = Article.objects.order_by('-id')
        return render(request, 'index.html', {'articles': articles})
