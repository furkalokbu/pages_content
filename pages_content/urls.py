
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
   
    path('jet/', include('jet.urls', 'jet')),
    path('banks/admin/', admin.site.urls),
    path('banks/', include('pages.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

