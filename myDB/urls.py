from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts',views.contact,name='get_name'),
    path('detail',views.detail,name='detail'),
]