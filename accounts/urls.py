from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
]