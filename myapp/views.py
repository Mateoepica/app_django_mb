from django.shortcuts import render, redirect
from .form import LoginForm
from .models import Login
import random 

def login(request):
    if request.method == 'POST':
        #print('ENTRO')
        form = LoginForm(request.POST)

        if form.is_valid():
            #print('login table content')
            valid_user, valid_password = Login.objects.all()[0].name, Login.objects.all()[0].password
            name = request.POST['name']
            password = request.POST['password']
            # print(valid_user)
            # print(valid_password)
            # print('name', name)
            # print('password', password)
            if name == valid_user  and  password == valid_password:
                #form.save()
                print('SESSION')
                print(request.session.session_key)
                
                request.session['bubu'] = 'jejejeje'
                
                print('request.COOKIES from POST')
                #cookies = request.COOKIES
                #cookies.set_cookie('alabama','32')
                print(request.COOKIES)
                return redirect('/after_login', foo='mateo')
    
    form = LoginForm()
    #print('NO ES UN POST')
    return render(request, 'form.html', {'form': form})

def after(request):
    print('request')
    print(request.COOKIES)
    print(request.COOKIES['sessionid'])
    print('sessions')
    print(request.session['bubu'])
    #if request.session['bubu']:
    return render(request, 'after_form.html')