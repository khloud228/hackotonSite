from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    start,
    upload_video,
)


urlpatterns = [
    path('', start, name='start_page'),
    path('upload/', upload_video, name='upload_video')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
