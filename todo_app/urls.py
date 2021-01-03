from django.urls import path
from .views import ( TodoListCreateView, TodoDeleteView, TodoUpdateView,)

app_name = 'todo'

urlpatterns = [
    path('todo_list/', TodoListCreateView.as_view(), name='todo-create'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
]
