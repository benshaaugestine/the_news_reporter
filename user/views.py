from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import FormView
from user.forms import SignUpForm,SettingsForm,PasswordForm
from django.contrib.auth import update_session_auth_hash

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
    return render(request, 'user/signup.html', {'form': form})

class UpdateView(FormView):
    template_name = 'user/updateprofile.html'
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


class UpdatePasswordView(FormView):
    template_name = 'user/update_password.html'
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