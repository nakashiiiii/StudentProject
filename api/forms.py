from django import forms
from .models import Diary, Student


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'title', 'text',)



class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'grade', 'lab']

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=20)