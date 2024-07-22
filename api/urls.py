from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    
    #login
    #path("",views.IndexView.as_view(), name='login'),
    #
    path('index/', views.IndexView.as_view(), name='index'), #home画面
    path('status/', views.StatusView.as_view(), name='status'), #ステータスを選択す画面
    path('activity/', views.activityCreateView.as_view(), name='activity'), #記録（日付とコメントを残す画面）
    path('activity/complete/', views.activityCreateCompleteView.as_view(), name='activity_complete'), #記録が完了しました（homeに戻るボタン）
    path('who/', views.whoView.as_view(), name='who'), #在室情報
]
