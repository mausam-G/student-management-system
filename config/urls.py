from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 

schema_view = get_schema_view( 
    openapi.Info(
        title="Student Management API",
        default_version="v1",
        description="Student Management API using DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="albert.abraham.official@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),     # API route (e.g. /api/student/)
    path('', include('api.urls')),         # 👈 यो थप्नुभयो भने / मा पनि काम गर्छ
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
