from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets_detail),
    path('teachers/', views.manage),
]