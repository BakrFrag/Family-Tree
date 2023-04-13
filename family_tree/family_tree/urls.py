from django.contrib import admin
from django.urls import path , include , re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Family Tree API",
      default_version='v1',
      description="every user can view his relatives or add new relatives to his own family tree",
      terms_of_service="http://127.0.0.1:8000/swagger/",
      contact=openapi.Contact(email="contact@support.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    # admin panel 
    path('admin/', admin.site.urls),
    # debug toolbar 
    path('__debug__/', include("debug_toolbar.urls")),
    # swagger open api 
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # api token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # family member app
    path('member/',include("family_member.urls")), 
]
