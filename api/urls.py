from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('status/', views.StatusView.as_view(), name='status'),
    path('activity/', views.activityCreateView.as_view(), name='activity'),
    path('activity/complete/', views.activityCreateCompleteView.as_view(), name='activity_complete'),
    path('who/', views.whoView.as_view(), name='who'),
]
