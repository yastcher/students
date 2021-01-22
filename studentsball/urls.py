from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^students/', include('studentsapi.urls')),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(title="Snippets API", default_version='v1'),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns.append(
        url(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui')
    )
