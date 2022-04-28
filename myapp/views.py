from django.shortcuts import render, redirect
from .form import LoginForm

def login(request):
    if request.method == 'POST':
        print('ENTRO')
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/after_login')
    
    form = LoginForm()
    print('NO ES UN POST')
    return render(request, 'form.html', {'form': form})

def after(request):
    return render(request, 'after_form.html')