from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.members),
    # path('addTodo/', views.addToDo),
    # path("calculation/", views.calculation),
    # path('admin/', admin.site.urls),
]