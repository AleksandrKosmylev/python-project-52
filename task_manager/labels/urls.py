from django.urls import path
from task_manager.labels.views import main_labels, LabelCreateView, LabelUpdateView, LabelDeleteView

urlpatterns = [
    path('', main_labels, name='labels'),
    path('create/', LabelCreateView.as_view(), name='label_create'),
    path('<int:id>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('<int:id>/delete/', LabelDeleteView.as_view(), name='label_delete'),
]
