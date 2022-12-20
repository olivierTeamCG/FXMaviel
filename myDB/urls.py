from django.urls import path
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this


urlpatterns = [
    path('', views.index, name='index'),
    path('contactFx',views.contactfx,name='get_contactfx'),
    path('contactFrancois',views.contactfrancois,name='get_contactfrancois'),
    path('detail',views.detail,name='detail'),
]