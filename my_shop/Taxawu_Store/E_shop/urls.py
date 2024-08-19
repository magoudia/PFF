from django.urls import path
from E_shop import views # type: ignore
from django.conf import settings
from django.conf.urls.static import static

app='E_shop'

urlpatterns = [
    path('', views.home, name='shop.html'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)