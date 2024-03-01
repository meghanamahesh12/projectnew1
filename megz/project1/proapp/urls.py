from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('page1/',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('listform/',views.form1,name='listform'),

   
]
