from news.views import UpdatePasswordView
from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views



app_name = 'news'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


    url(r'^profile/$', views.UpdateView.as_view(), name='profile'),

    url('^', include('django.contrib.auth.urls')),


    url(r'^setpassword/', UpdatePasswordView.as_view(), name='set_password'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/category/$', views.CategoryView.as_view(), name='category')
    ]

