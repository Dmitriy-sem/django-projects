from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('task-list/', taskList, name="task-list"),
    path('task-create/', taskCreate, name="task-create"),
    path('task-update/<str:pk>/', taskEdit, name="task-update"),
    path('task-delete/<str:pk>/', taskDelete, name="task-delete"),
]
