from django.urls import path, include
from erp import views

urlpatterns = [
    path('', views.main_view, name='main_page'),
]
