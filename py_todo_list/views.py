from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task, Tag


class Index(generic.ListView):
    model = Task
    template_name = "py_todo_list/index.html"



class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "py_todo_list/task_form.html"
    success_url = reverse_lazy("pyTodoList:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "py_todo_list/task_form.html"
    success_url = reverse_lazy("pyTodoList:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "py_todo_list/task_delete.html"
    success_url = reverse_lazy("pyTodoList:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "py_todo_list/tag_list.html"



class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "py_todo_list/tag_form.html"
    success_url = reverse_lazy("pyTodoList:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "py_todo_list/tag_form.html"
    success_url = reverse_lazy("pyTodoList:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "py_todo_list/tag_delete.html"
    success_url = reverse_lazy("pyTodoList:tag-list")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('pyTodoList:index')
