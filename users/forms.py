from django import forms
from .models import Puser

YEARS= [x for x in range(1940,2010)]

class PuserForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control form-control-sm col-4', 'style': 'float:left'}, years=YEARS),
        )

    class Meta:
        model = Puser
        # exclude = ['author', 'updated', 'created', ]
        fields = ['first_name', 'last_name', 'email', 'password', 'city', 'state']
        
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-fname', 'class': 'form-control', 'required': True, 'placeholder': "Say something..."}
            ),
        }