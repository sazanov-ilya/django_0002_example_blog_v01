from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


class BlogListView(ListView):
    """ Класс списка статей """
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'  # имя переменной для шаблона (по умолчанию object_list)


class BlogDetailView(DetailView):
    """ Класс отдельной статьи """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'  # имя переменной для шаблона (по умолчанию object_list)


class BlogCreateView(CreateView):
    """ Класс добавдения новой статьи """
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    # Перенаправление по умолчания на страницу новой созданной статьи через get_absolute_url модели


class BlogUpdateView(UpdateView):
    """ Класс обновления статьи """
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'  # имя переменной для шаблона (по умолчанию object_list)
