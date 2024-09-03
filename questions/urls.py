from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('admin/', admin.site.urls),
    path('showme/', include('showme.urls')),  # Include the URLs from the showme app
    path('tellme/', include('tellme.urls')),
    path('testoverview/', include('testoverview.urls')),
    path('cardiagram/', include('cardiagram.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
