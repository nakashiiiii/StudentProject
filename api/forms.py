from django import forms
from .models import Diary

#login用
from django.contrib.auth.forms import UserCreationForm #,AuthenticationForm #login用
#AuthenticationForm：username passwordに対して
#from .models import Person
#

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'title', 'text',)

#login用
#class LoginForm(AuthenticationForm):
#    class Meta:
#        model = Person
#