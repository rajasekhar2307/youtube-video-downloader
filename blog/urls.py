from django.urls import path, include
from . import views

urlpatterns =[
    path('',views.index, name ='index'),
    path('get',views.getdetails,name='getdetails'),
    path('download',views.download,name='download')
]