from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('bedDetails/', views.bedDetails, name='bedDetails'),
    path('remInjection/', views.remInjection, name='injection'),
    path('careCentre/', views.careCenter, name='careCenter'),
    path('freeVaccination/', views.freeVaccination, name='freeVaccination'),
    path('helplineDetail/', views.helplineDetail, name='helplineDetail'),
    path('o2Cylinders/', views.o2Cylinders, name='o2Cylinders'),
    path('testingCenter/', views.testingCenter, name='testingCenter'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]