from django import forms
from .models import Subscribers

class SubscribersForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    # mode = forms.CharField(max_length=10 )

    class Meta:
        model = Subscribers
        fields = ('email')
