from django.views.generic.edit import FormView
from .models import Subscribers
from .forms import SubscribersForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.views import View



class AddToSubscriptionList(FormView) :
    model_form = SubscribersForm
    model = Subscribers
    template_name = "widgets/subscribe.html"
    fields = ['email',]
    success_url = '/'
    msg = ''

    def form_invalid(self,form):
        return render(self.request, self.template_name,{'form':self.model_form(form),'msg':self.msg,})

    def post(self, request, *args, **kwargs):
        form= self.model_form(request.POST)
        if form.is_valid():
            email = form['email'].value()
            email_in_db = Subscribers.objects.filter(email=email)
            if email_in_db:
                msg = ' Already Subscribed. '
                msg = "<div class = 'alert alert-info'><b>STATUS :</b> %s </div>"%(msg)
            else :
                s = Subscribers()
                s.email = email
                s.token = get_random_string(length=32)
                s.active = False
                s.save()
                send_mail(
                    'Subscription Activation Approval',
                    """ Hey User, This email ( %s ) have been requested to subscribe in our News Channel, \
                    if You are Interested Please Activate through this link :  \
                    \
                        127.0.0.1:8000/widgets/activate/%s/    \
                    \
                    From The News Reporter.com
                    """ % (s.email, s.token),
                    'activate-subscription@thenewsreporter.dtn',
                    [s.email],
                    fail_silently=True,
                )
                msg = 'Successfully Subscribed! Activate It From Your Inbox.'
                msg = "<div class='alert alert-success'><b>STATUS :</b> %s</div>" % (msg)
            print(msg)
        else:
            print('form_invalid')
            msg = "Invalid Email"
            msg = "<div class='alert alert-danger'><b>STATUS :</b> %s</div>" % (msg)
        return render(request, self.template_name,{'form': self.model_form(), "msg": msg})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.model_form()})


class ActivateSubscription(View):

    def get(self, request, *args, **kwargs):

        try:
            token = self.kwargs['token']
            subscriber = Subscribers.objects.get(token=token)
            subscriber.backend = 'django.contrib.auth.backends.ModelBackend'

        except (TypeError, ValueError, OverflowError, Subscribers.DoesNotExist):

            subscriber = None

        finally:
            print("FINAL BLOCK")


        if subscriber is not None :

            subscriber.active = True
            subscriber.save()
            return render(request, 'widgets/subscribe.html',{'sub_pass': "Subscription Activation Successful"})
        else :
            return render(request, 'widgets/subscribe.html',{'sub_fail': "Subscription Failed. Please Try Again!"})



