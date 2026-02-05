from django.urls import path
from .views import index, task_list #from .views in blogpage, import index function

urlpatterns = [
    path('', index, name='index'),
    # path('list/<int:id>', task_list, name='task_list')
    path('list', task_list, name='task_list')
]

app_name = "blogpage"