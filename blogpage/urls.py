from django.urls import path
from .views import *  # from .views in blogpage, import index function

urlpatterns = [
    path('', index, name='index'),
    path('list', task_list, name='task_list'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('add/', TaskCreateView.as_view(), name='task_add'),

]

app_name = "blogpage"
