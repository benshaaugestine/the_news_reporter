
from django.views import generic
from django.views.generic import FormView

from .models import News,Category
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash





from news.forms import SignUpForm,SettingsForm,PasswordForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('news:index')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'form': form})


class UpdateView(FormView):
    template_name = 'news/updateprofile.html'
    form_class = SettingsForm
    success_url = '/'

    def form_valid(self,form):
        form = form.cleaned_data
        ret = super(UpdateView,self).form_valid(form)
        if(ret):
            self.request.user.first_name = form['first_name']
            self.request.user.last_name = form['last_name']
            self.request.user.email = form['email']
            self.request.user.save()
        return ret




class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

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

class CategoryView(generic.DetailView):
    model=Category
    template_name='news/category.html'




class UpdatePasswordView(FormView):
    template_name = 'news/update_password.html'
    form_class = PasswordForm
    success_url = '/'

    def form_valid(self,form):
        data = super(UpdatePasswordView,self).form_valid(form)
        form = form.cleaned_data
        if(form['password'] == form['password_confirm']):
            self.request.user.set_password(form['password'])
            self.request.user.save()
            update_session_auth_hash(self.request, self.request.user)
            login(self.request, self.request.user)

        return data







