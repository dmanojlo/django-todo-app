from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
            ListView,
            CreateView,
            DeleteView,
            UpdateView
)

from .models import Todo
from .forms import TodoForm
# Create your views here.

# class TodoListView(ListView):
#     template_name = 'todo/todo_list.html'
#     queryset = Todo.objects.all()


class TodoListCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo_list.html'
    form_class = TodoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.order_by('-completed')
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'

class TodoDeleteView(DeleteView):
    model = Todo
    def get_success_url(self):
        return reverse('todo:todo-create')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['completed']
