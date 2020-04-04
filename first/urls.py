"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('index.html', views.echo),  # 在url中凡是以url开头的访问都使用index函数来处理该请求
    path('charts.html', views.charts),
    path('charts2.html', views.charts2),
    path('charts3.html', views.charts3),
    path('notifications.html', views.showAll),
    path('tables.html', views.tousu),
    path('typography.html', views.typography),
    path('page_profile.html', views.update_msg),
    path('login.html', views.login),
    path('register.html', views.register),
    path('delete', views.delete, ),
    path('delete1', views.delete1)
]
