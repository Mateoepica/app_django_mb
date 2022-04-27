from django.shortcuts import render
from .form import LoginForm

def login(request):
    if request.method == 'POST':
        
        form = LoginForm(request.POST)

        if form.is_valid():
            
            form.save()
        else:
            print('ENTRO invalid')
    form = LoginForm()

    return render(request, 'form.html', {'form': form})
