from django.shortcuts import render
from django.views import View
from task_manager.users.forms import UsersForm

def index(request):
    return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = UsersForm()
        return render(request, 'login.html',{'form': form})
