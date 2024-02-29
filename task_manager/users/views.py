from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from task_manager.users import forms
from task_manager.users.forms import UsersForm
# from task_manager.users.models import Users
from django.contrib.auth import get_user_model
from django.contrib import messages

Users = get_user_model()

class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all().order_by('id').exclude(username='admin')
        return render(request, 'users/users_list.html', context={
            'users': users,
        })


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/user_create.html')

    def post(self, request, *args, **kwargs):
        user_form = UsersForm(request.POST)
        if user_form.is_valid():
            # print(user_form.cleaned_data['first_name'], "userform!")
            new_user = user_form.save(commit=False)
            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            if password1 != password2:
                messages.warning(request, 'Введенные пароли не совпадают.')
                return redirect('user_create')
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            # print("success")
            return redirect('login')
        else:
            print(user_form.errors.as_data(), 'errors')
            return HttpResponse("FAILED. CREATE FLASH FOR IT")
            return redirect('user_create')


class UserUpdateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Users.objects.get(id=user_id)
        return render(request, 'users/user_update.html',{'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Users.objects.get(id=user_id)
        form = UsersForm(request.POST, instance=user)
        print("in it")
        if form.is_valid():
            form.save()
            print(form.errors.as_data(), 'errors1')
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('users_index')
        else:
            print(form.errors.as_data(), 'errors2')
            return HttpResponse("Error form")
        print(form.errors.as_data(), 'errors3')
        return render(request, 'users/user_update.html',{'form': form, 'user': user})

class UserDeleteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Users.objects.get(id=user_id)
        return render(request, 'users/user_delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Users.objects.get(id=user_id)
        if user:
            user.delete()
            messages.success(request, 'Пользователь успешно удален')
            return redirect('users_index')
        return HttpResponse("DELETE USER FAILED. CREATE FLASH FOR IT")
