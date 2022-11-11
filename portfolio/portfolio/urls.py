
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('home_app.urls')),
    path('account/',include('login_app.urls')),
    path('dashboard/',include('admin_app.urls')),
]
# urlpatterns+=staticfiles_urlpatterns()
# urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

