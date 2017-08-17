from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', views.UpdateView.as_view(), name='profile'),
    url(r'^setpassword/', views.UpdatePasswordView.as_view(), name='set_password'),
    url('^', include('django.contrib.auth.urls'))
        ]