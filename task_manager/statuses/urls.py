from django.urls import path
from task_manager.statuses.views import main_statuses


urlpatterns = [
    path('', main_statuses, name='main_statuses'),
]
