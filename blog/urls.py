from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index),
    path("post/<slugInput>/", views.detailPost),
    path("category/<categoryInput>/", views.categoryPost),
    path("gambar/<gambarInput>/", views.gambarPost),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
