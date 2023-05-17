from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('Puddle.core.urls')),
    path('items/', include('Puddle.item.urls')),
    path('dashboard/', include('Puddle.dashboard.urls')),
    path('inbox/', include('Puddle.conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
