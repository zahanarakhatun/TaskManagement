from django.shortcuts import render,redirect
from.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Task
# Create your views here.


# registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'taskApp/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'taskApp/login.html'

@login_required
def dashboard_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskApp/dashboard.html', {'tasks': tasks})