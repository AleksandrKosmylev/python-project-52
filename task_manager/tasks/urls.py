from django.urls import path
from task_manager.tasks.views import (TaskView,
                                      TaskCreateView,
                                      TaskInfoView,
                                      TaskUpdateView,
                                      TaskDeleteView)

urlpatterns = [
    path('', TaskView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskInfoView.as_view(), name='task_card'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
