from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.profile.urls")),
    path('api/auth/token/', obtain_jwt_token),
    path('api/auth/token/refresh/', refresh_jwt_token),
    path('api/auth/token/verify/', verify_jwt_token),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'), name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
