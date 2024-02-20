from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.forms import UsersForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html',{'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы залогинены')
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return redirect('login')
        else:
            return HttpResponse('Invalid ')


