from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


from task_manager.users.models import Users


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()[:15]
        return render(request, 'users/user_list.html', context={
            'users': users,
        })


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/user_create.html',)


class UserUpdateView(View):

    def get(self, *args, **kwargs):
        user_id = kwargs.get('id')
        return HttpResponse("user_id", user_id)


class UserDeleteView(View):

###  GET   deleted  user. but  not  POST  dont UNDERSTAND WHY!!

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Users.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users_index')
