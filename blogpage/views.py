from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from django.views.generic.list import *
from django.views.generic.detail import *
from django.views.generic import FormView
from django.views.generic.edit import *
from .models import *

tasks = []


def index(request):
    return HttpResponse('Hello world! This came from the index view.')


def task_list(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.profile = Profile.objects.get(user=request.user)
            task.save()
            print(task)
            return redirect('blogpage:task_detail', pk=task.pk)

    else:
        form = TaskForm()

    tasks = Task.objects.all()

    return render(request, "blogpage/task_list.html", {
        "form": form,
        "task_list": tasks,
        "taskgroups": TaskGroup.objects.all(),
    })


@login_required
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
        tasks.append(
            (form.cleaned_data['task_name'], form.cleaned_data['task_date']))
        return super().form_valid(form)


class TaskListView(ListView):
    model = Task
    template_name = 'blogpage/task_list.html'

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset(**kwargs)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     profile = Profile.objects.get(user=self.request.user)
    #     context['task_list'] = Task.objects.filter(profile=profile)
    #     return context


class TaskDetailView(LoginRequiredMixin, DetailView):  # LoginMixin is view basis
    model = Task
    template_name = 'blogpage/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    # template_name = task_form.html

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'blogpage/task_update.html'

    def post(self, request, *args, **kwargs):
        pass
