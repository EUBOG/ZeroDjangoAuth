# glav/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Кастомизация LoginView (можно оставить как есть, но указываем шаблон)
class CustomLoginView(LoginView):
    template_name = 'login.html'

# LogoutView можно использовать по умолчанию