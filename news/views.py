from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import News

class IndexView(generic.ListView):


    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return News.objects.all()


class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'



