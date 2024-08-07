# from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),

    # Djoser создал набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path(r'auth/', include('djoser.urls')),

    # JWT-эндпоинты, для управления JWT-токенами:
    path(r'auth/', include('djoser.urls.jwt')),
]


# # Дополнительные настройки для документации Swagger and Redoc
# schema_view = get_schema_view(
#    openapi.Info(
#       title="zloy_wear API",
#       default_version='v1',
#       description="Документация для проекта zloy_wear",
#       # terms_of_service="URL страницы с пользовательским соглашением",
#       contact=openapi.Contact(email="example@example.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

# urlpatterns += [
#    url(r'^swagger(?P<format>\.json|\.yaml)$', 
#        schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
#        name='schema-swagger-ui'),
#    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
#        name='schema-redoc'),
# ]
