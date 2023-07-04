from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from doeja.forms.AuthForm import LoginForm, RegisterForm



def login_view(request):
    loginForm = LoginForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)
        
        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = {
                    'type' : 'danger',
                    'text' : 'Dados de usuário incorrectos'
                }
                
    context = {
        'form' : loginForm,
        'message' : message,
        'button_text' : 'Login'
    }
        
    return render(
        request,
        template_name='auth/auth.html',
        context=context,
        status=200
    )
    
def register_view(request):
    registerForm = RegisterForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)
        
        if registerForm.is_valid():
            # verify that user exist
            verify_username = User.objects.filter(username=username).first()
            verify_email = User.objects.filter(email=email).first()
            
            if verify_username is not None:
                message = {
                    'type' : 'danger',
                    'text' : 'Já existe um usuário com este username!!'
                }
            
            elif verify_email is not None:
                message = {
                    'type': 'danger',
                    'text' : 'Já existe um usuário com este e-mail!!'
                }
            else:
                user = User.objects.create_user(username, email, password)
                if user is  not None:
                    message = {
                        'type': 'success',
                        'text': 'Conta criada com sucesso!'
                    }
                else:
                    message = {
                        'type': 'danger',
                        'text': 'Um erro ocorreu ao tentar criar a conta'
                    }
                    
    context = {
        'form' : registerForm,
        'message': message,
        'title' : 'Registrar',
        'button_text' : 'Registrar'
    }
    
    return render(request, template_name='auth/auth.html', context=context, status=200)
        
def logout_view(request):
    logout(request)
    return redirect('/login')
