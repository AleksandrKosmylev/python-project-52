from django.shortcuts import render
from django.views import View


from task_manager.users.models import Users


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()[:15]
        return render(request, 'users/users_list.html', context={
            'users': users,
        })
