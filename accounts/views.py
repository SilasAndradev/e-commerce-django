from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from accounts.forms import ClientForm
from accounts.models import Client

# Create your views here.
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except Exception:
            messages.error(request, 'Usuário não existe!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nome de usuário OU senha estão erradas!')

    context = {

    }
    return render(request, '', context)

def RegisterUser(request):
    form = UserCreationForm()
    client_form = ClientForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        client_form = ClientForm(request.POST)
        if form.is_valid and client_form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            client = client_form.save(commit=False)
            Client.objects.create(
                user=user,
                ClientPicture=client.ClientPicture,
                PhoneNumber=client.PhoneNumber,
                email=client.email,
            )

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ocorreu um erro durante o registro!')
    
    return render(request, 'accounts/register.html', {'form':form, 'client_form':client_form})

@login_required(login_url='/login')
def LogoutUser(request):
    logout(request)
    return redirect('home')