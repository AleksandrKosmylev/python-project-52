from django.urls import path
from task_manager.tasks.views import main_tasks, TaskCreateView

urlpatterns = [
    path('', main_tasks, name='tasks'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    # path('<int:id>/update/', StatusUpdateView.as_view(), name='task_update'),
    # path('<int:id>/delete/', StatusDeleteView.as_view(), name='task_delete'),
]
