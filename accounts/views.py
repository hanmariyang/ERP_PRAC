from django.shortcuts import render, redirect
from accounts.models import UserModel


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    
    elif request.method == 'POST': # POST 메서드로 요청이 들어 올 경우
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        # 비밀번호가 비밀번호 재확인이랑 틀릴 경우
        if password != password2:
            return render(request, 'accounts/signup.html')
        
        # 비밀번호가 동일할 경우
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            new_user.save()
        return redirect('/login')