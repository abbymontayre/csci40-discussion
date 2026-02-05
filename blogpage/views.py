from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm

tasks = []

def index(request):
    return HttpResponse('Hello world! This came from the index view.')

def task_list(request):
        
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                tasks.append( (form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
                return redirect('/blogpage/list')
        elif request.method == "UPDATE":
            pass
        else:
            form = TaskForm()

        return render(request, "blogpage/task_list.html", {
             "form": form,
             "tasks": tasks,
        })


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