from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html' , {
        'message': 'Listado de productos',
        'products':'Destacados de la semana'
    })
    
    
def login_views(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        
        user = authenticate(username=username , password = password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'El username o password son incorrectos')
    return render(request, 'login.html', {
        
    })

def logout_views(request):
    logout(request)
    messages.success(request, 'sesión cerrada con exito')
    return redirect('login')
    

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Creado exitosamente')
            return redirect('index')
    
    return render(request, 'registro.html', {
        'form':form
    })