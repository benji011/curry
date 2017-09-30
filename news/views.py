from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    """
    The top page

    :param request:
    :return:
    """
    template = loader.get_template('news/index.html')
    context = {}
    return HttpResponse(template.render(context, request))