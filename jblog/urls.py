from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import main, post, cat, search

urlpatterns = [
    path('', main),
    path('<int:pk>', post, name="single"),
    path('category/<int:pk>', cat, name="category"),
    path('q', search, name="search"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
