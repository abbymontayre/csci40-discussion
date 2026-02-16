from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from django.views.generic.list import *
from django.views.generic.detail import *
from django.views.generic import FormView
from .models import *

tasks = []

def index(request):
    return HttpResponse('Hello world! This came from the index view.')

def task_list(request):
        
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                tasks.append( (form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
                return redirect('/blogpage/list')
        else:
            form = TaskForm()

        tasks = Task.objects.all()

        return render(request, "blogpage/task_list.html", {
             "form": form,
             "tasks": tasks,
        })

def task_detail(request, id):
    task = Task.objects.get(pk=id)

    return render(request, "blogpage/task_detail.html", {
         "task": task,
    }) 

class TaskAddView(FormView):
    template_name = "blogpage/task_add.html"
    form_class = TaskForm
    success_url = "/blogpage/list"

    def form_valid(self, form):
        tasks.append( (form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
        return super().form_valid(form)

class TaskListView(ListView):
    model = Task
    template_name = 'blogpage/task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'blogpage/task_detail.html'


# def task_list(request, id):
#     context = {}
#     if id == 1:
#         context = {
#             "tasks": [
#                 "task 1",
#                 "task 2",
#                 "task 3",
#                 "task 4"
#             ]
#         }
#     else:
#         context = {
#             "tasks": [
#                 "task 5",
#                 "task 6",
#                 "task 7",
#                 "task 8"
#             ]
#         }
#     return render(request, "blogpage/task_list.html", context)

# def task_list(request, name):
#         context = {
#             "tasks": [
#                 "task 1",
#                 "task 2",
#                 "task 3",
#                 "task 4"
#             ],
#             "name": name
#         }
#         return render(request, "blogpage/task_list.html", context)


#views.py is how we display things as a website
# it can be the template, html, JS, Vue, or anything to disa