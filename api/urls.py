from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:student_id>/', views.person_detail, name='person_detail'),
    path('status/', views.StatusView.as_view(), name='status'),
    path('activity/', views.activityCreateView.as_view(), name='activity'),
    path('activity/complete/', views.activityCreateCompleteView.as_view(), name='activity_complete'),
    path('who/', views.whoView.as_view(), name='who'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/<str:student_id>/', views.profile, name='profile'),
]
