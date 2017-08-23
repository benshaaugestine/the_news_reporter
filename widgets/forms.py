from django import forms
from .models import Subscribers,Contact

class SubscribersForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    # mode = forms.CharField(max_length=10 )

    class Meta:
        model = Subscribers
        fields = ('email')


# class ContactForm(forms.Form) :
#     name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     message = forms.CharField(max_length=30, required=False, help_text='Optional.')
#
#     class Meta:
#         model = Contact
#         fields = ('name', 'email', 'message')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
