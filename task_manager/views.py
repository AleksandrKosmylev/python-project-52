from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.forms import UsersForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# new edit
from django.views.generic import TemplateView

"""
def index(request):
    return render(request, 'index.html')
"""
class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(View):

    def get(self, request, *args, **kwargs):
        # form = LoginForm()
        # return render(request, 'login.html',{'form': form})
        return render(request, 'login.html')
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user, 'user')
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы залогинены')
                    print("login success active")
                    return redirect('index')
                else:
                    print("login success not active")
                    return HttpResponse('Disabled account')
            else:
                messages.error(request, "Пожалуйста, введите правильные имя пользователя и пароль."
                                        " Оба поля могут быть чувствительны к регистру.")
                print('smt wrong')
                # tag ="Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру."
                return redirect('login')
        else:
            return HttpResponse('Invalid ')



def logout_view(request):
    logout(request)
    messages.success(request, 'Вы разлогинены')
    return redirect('index')


"""
# from django.contrib.auth.views import get_user_model
from django.contrib.auth.models import User

class UserView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        print(type(users))
        return HttpResponse(users.date)

        return render(request, 'USER.html', context={
            'user': users,
        })
"""
