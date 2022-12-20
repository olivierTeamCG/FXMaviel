from django.contrib import admin
from django.urls import include, path

from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('myDB/', include('myDB.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)