from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_view

app_name = 'news'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/category/$', views.CategoryView.as_view(), name='category'),
    url(r'^search/$',views.SearchResultView.as_view(),name='search_result')
    ]

