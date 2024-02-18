from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.forms import UsersForm
from task_manager.users.models import Users


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all().order_by('id')
        return render(request, 'users/users_list.html', context={
            'users': users,
        })


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UsersForm()
        return render(request, 'users/user_create.html',{'form': form})

    def post(self, request, *args, **kwargs):
        form = UsersForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password1")
            password_check = form.cleaned_data.get("password2")
            if password == password_check:
                form.save()
                return redirect('users_index')
            else:
                # IN PROCESS (ADD FLASH )
                return HttpResponse("FAILED. CREATE FLASH FOR IT")
                # IN PROCESS
        return render(request, 'users/user_create.html', {'form': form})



class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        print(kwargs, 'kwargs')
        print(user_id, 'user_id', type(user_id))
        user = Users.objects.get(id=user_id)
        all = Users.objects.all
        print(all, 'all')
        print(user, 'user')
        form = UsersForm(instance=user)
        return render(request, 'users/user_update.html',{'form': form, 'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        print(user_id, 'user_id_post', type(user_id))
        user = Users.objects.get(id=user_id)
        print(user, 'user_post', type(user))
        form = UsersForm(request.POST, instance=user)
        print("after-form")
        if form.is_valid():
            form.save()
            print(user, 'user_post_after', type(user))
            print("REDIRECT")
            return redirect('users_index')
        else:
            print("ERRoR")
        return render(request, 'users/user_update.html',{'form': form, 'user': user})


class UserDeleteView(View):

#  GET   deleted  user. but  not  POST  dont UNDERSTAND WHY!!

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Users.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users_index')