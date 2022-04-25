# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    # Список всех статей на главной странице
    path('', BlogListView.as_view(), name='home'),

    # Конкретная статья
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),

    # Добавление новой статьи
    path('post/new/', BlogCreateView.as_view(), name='post_new'),

    # Обновление статьи
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),

    # Удаление статьи
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
