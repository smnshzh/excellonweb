from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('showall',views.all_data,name="show_all"),
    path('<int:id>',views.data_show,name="data_show")
]
