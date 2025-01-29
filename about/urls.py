from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import include, path
from .views import about_view

urlpatterns = [
      path('', about_view, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)