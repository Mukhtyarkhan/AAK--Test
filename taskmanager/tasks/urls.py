from django.urls import path
from .views import (
    create_label, update_label, delete_label, user_labels,
    create_task, update_task, delete_task
)

urlpatterns = [
    # Label URLs
    path('labels/', user_labels, name='user-labels'),
    path('labels/create/', create_label, name='create-label'),
    path('labels/<int:label_id>/update/', update_label, name='update-label'),
    path('labels/<int:label_id>/delete/', delete_label, name='delete-label'),
    
    # Task URLs
    path('tasks/create/', create_task, name='create-task'),
    path('tasks/<int:task_id>/update/', update_task, name='update-task'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete-task'),
]

