from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import DiaryForm
from .models import Diary

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
