from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import DeletionMixin

from task_manager.users.forms import UsersForm
# from task_manager.users.models import Users
from django.contrib.auth import get_user_model
from django.contrib import messages
# edited ->
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from task_manager.users.models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
# from task_manager.users.models import Users
from task_manager.mixins import CustomLoginRequiredMixin
from task_manager.users.mixins import AccessCheck

# Users = get_user_model()
"""
class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all().order_by('id').exclude(username='admin')
        return render(request, 'users/users_list.html', context={
            'users': users,
        })
"""
class IndexView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'

"""
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
"""
class UserCreateView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UsersForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('login')
    success_message = _('Successfully registered!')

"""
class UserUpdateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'users/user_update.html',{'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        form = UsersForm(request.POST, instance=user)
        print("in it")
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('users_index')
        else:
            print(form.errors.as_data(), 'errors2')
            return HttpResponse("Error form")
        return render(request, 'users/user_update.html',{'form': form, 'user': user})
"""
class UserUpdateView(CustomLoginRequiredMixin, AccessCheck, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UsersForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('Successfully updated!')


class UserDeleteView(CustomLoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _("Product successfully deleted!")
"""
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
"""

"""
class UserDeleteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'users/user_delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        if user:
            user.delete()
            messages.success(request, 'Пользователь успешно удален')
            return redirect('users_index')
        return HttpResponse("DELETE USER FAILED. CREATE FLASH FOR IT")
"""


