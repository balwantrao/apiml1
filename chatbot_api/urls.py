from django.urls import path
import views

urlpatterns = [
    # path('', views.index, name='index'), 
    path('train/', views.train_chatbot_api),
    path('test/<str:query>', views.test_chatbot_api),
]
