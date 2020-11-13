from django.urls import path
from idd import code
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plot', views.plotly, name='plotly'),
    path('page1',views.page1,name='page1')
]