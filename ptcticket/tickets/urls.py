from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets_detail),
    path('teachers/', views.student_list),
    path('teachers/<int:id>/', views.manage, name='views-teachers'),
]