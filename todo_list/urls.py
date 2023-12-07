from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("py_todo_list.urls", namespace="py_todo_list")),
]
