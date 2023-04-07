from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'), # 회원가입 페이지
    path('login/', views.login, name='login'), # 로그인 페이지
]
