from django.urls import path
from . import views

app_name = 'h_w_list'
urlpatterns = [
    path('', views.h_w_list, name = 'h_w_list'),
    

    

]