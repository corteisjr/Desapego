from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from doeja.forms.AuthForm import LoginForm



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
    
def logout_viw(request):
    logout(request)
    return redirect('/login')
