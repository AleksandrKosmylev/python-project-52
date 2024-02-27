from django.urls import path
from task_manager.statuses.views import main_statuses,StatusCreateView


urlpatterns = [
    path('', main_statuses, name='statuses'),
    path('create/', StatusCreateView.as_view(), name='status_create'),

]
