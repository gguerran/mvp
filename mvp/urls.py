from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'MVP'

schema_view = get_schema_view(
   openapi.Info(
      title="API - Federação de Comércio",
      default_version='v1',
      description="API - Demandas",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gustavoguerra.gr@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'
    ),
    url(
        r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    url(
        r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('api/v1/accounts/', include('mvp.accounts.urls'), name='accounts'),
    path('api/v1/demand/', include('mvp.demand.urls'), name='demand'),
    path(
        'api/v1/oauth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
