from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import DiaryForm
from .models import Diary
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentRegistrationForm, LoginForm
from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'index.html'

class StatusView(TemplateView):
    template_name = 'status.html'

class activityCreateView(CreateView):
    template_name = 'activity.html'
    form_class = DiaryForm
    success_url = reverse_lazy('api:diary_create_complete')

class activityCreateCompleteView(TemplateView):
    template_name = 'activity_complete.html'

class whoView(TemplateView):
    template_name = 'who.html'

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            student_id = form.cleaned_data['student_id']
            try:
                student = Student.objects.get(name=name, student_id=student_id)
                return redirect('profile', student_id=student.student_id)
            except Student.DoesNotExist:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def profile(request, student_id):
    student = Student.objects.get(student_id=student_id)
    if request.method == 'POST':
        student.is_present = not student.is_present
        student.save()
    return render(request, 'profile.html', {'student': student})