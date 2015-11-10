from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Article, Tag, Classification


def index(request):
    articles = Article.objects.all()
    classification = Classification.objects.all()
    return render_to_response('index.html',
                  locals(),
                  context_instance=RequestContext(request))


def content(request, id):
    article = get_object_or_404(Article, id=id)
    classification = Classification.objects.all()
    return render_to_response('content.html',
                  locals(),
                  context_instance=RequestContext(request))