from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Task


class TasksListView(ListView):
    template_name = 'list.html'
    queryset = Task.objects.all().order_by('level')


class TasksDetailView(DetailView):
    template_name = 'details.html'
    queryset = Task.objects.filter()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(TasksDetailView, self).get_context_data(*args, **kwargs)
    #     return context

    # def get_object(self,*args, **kwargs):
    #     url_id = self.kwargs.get('pk')
    #     obj = get_object_or_404(Task, id=url_id)
    #     return obj

