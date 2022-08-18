from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Profile
import json
from django.http import JsonResponse
from django.views import View
from account.validation  import validate_email
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get['username',None]   #딕셔너리형태
        nickname = request.POST.get['nickname',None]
        email = email.POST.get['email',None]
        password = request.POST.get['password',None]
        re_password = request.POST.get['re_password',None]
        git_adress = request.POST.get['git_adress',None]
        res_data = {} 
        # if not (username and password and re_password and nickname and git_adress) :
        #     res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 일치하지 않습니다'
        
        #입력한 이메일 형식이 다를경우
        elif validate_email(email) == False :
                return JsonResponse({'MESSAGE':'INVALID_EMAIL_ADDRESS'}, status=400)
        
        #입력한 이메일이 이미 존재할 경우
        elif Profile.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE':'ALREADY_EXISTS_EMAIL'}, status=400)
        
        elif KeyError :
            return JsonResponse({'MESSAGE':"KEY_ERROR"}, status = 400)

        else :
            user = Profile(username=username, password=make_password(password))
            user.save()
    return render(request, 'signup.html', res_data) #signup를 요청받으면 signup.html 로 응답.

# def signup(request):

#     return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
            
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


