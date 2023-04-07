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
    
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    
    # 로그인시 실행되는 로직
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)  # 사용자 불러오기
        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return redirect('/erp')
        else: # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/login')
    # 로그인 view
