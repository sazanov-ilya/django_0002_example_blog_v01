"""project_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL маршруты для системы аутентификации (авторизации)
    # Как отмечается в документации к LoginView,
    # по умолчанию Django будет искать файл login.html в папке registration.
    # Таким образом, нам нужно создать новую директорию под названием registration,
    # а внутри нее создать необходимый HTML файл шаблона
    # templates/registration/login.html
    # ! Отдельно создавать View НЕ нужно
    # ! Но нужно в "settings.py" прописать страницу для переадресации "LOGIN_REDIRECT_URL = 'home"
    # http://127.0.0.1:8000/accounts/login/
    path('accounts/', include('django.contrib.auth.urls')),

    # URL маршруты для системы регистрации (создание нового пользователя)
    path('accounts/', include('app_accounts.urls')),

    # URL маршруты блога
    path('', include('app_blog.urls')),
]
