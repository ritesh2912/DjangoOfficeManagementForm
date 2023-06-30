from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_all_emp', views.all_emp, name='view_all_emp'),
    path('view_add_emp', views.add_emp, name='view_add_emp'),
    path('view_remove_emp', views.remove_emp, name='view_remove_emp'),
    path('view_remove_emp/<int:emp_id>', views.remove_emp, name='view_remove_emp'),
    path('view_filter_emp', views.filter_emp, name='view_filter_emp'),
]