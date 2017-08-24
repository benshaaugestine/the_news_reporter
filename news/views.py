from django.views import generic
from django.views.generic import ListView

from .models import News,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'
    paginate_by = 3

    def get_queryset(self):
        return News.objects.all()

    def get_context_data(self):
        context = super().get_context_data()
        category_list = Category.objects.all()
        context['category_list']= category_list
        return  context



class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'


class CategoryView(generic.ListView):
    model=Category
    template_name='news/category.html'
    context_object_name = 'list'
    paginate_by = 3
    def get_queryset(self):
        pk = self.kwargs.get('pk', 'lat')
        if pk != 'lat':
            cat = self.model._default_manager.get(pk=int(pk))
            return cat.news_set.all()
        else:
            return self.model._default_manager.all()




class SearchResultView(generic.ListView):
    """ class view to display list of news  on the page """
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'news'
    paginate_by = 3


    def get_queryset(self,*args,**kwargs):
        return News.objects.filter(title__icontains = self.request.GET['searchitem'])
        #TODO: try catch

    def get_context_data(self):
        # Call the base implementation first to get a context
        context = super().get_context_data()
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context











