from django.views import generic
from .models import News,Category
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from news.forms import SignUpForm

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




