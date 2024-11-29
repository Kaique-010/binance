from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'autenticacao/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário no banco de dados
            login(request, user)  # Faz login automático após registro
            return redirect('dashboard')  # Redireciona para o painel
    else:
        form = CustomUserCreationForm()

    return render(request, 'autenticacao/register.html', {'form': form})