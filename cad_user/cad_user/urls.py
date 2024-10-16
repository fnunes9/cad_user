from django.urls import path
from app_cad_user import views

urlpatterns = [
    path('', views.index , name='index'),
]
