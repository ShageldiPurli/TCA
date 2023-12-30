"""
URL configuration for TCA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from TCA import settings
from main_app.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="TCA API",
        default_version='v1',
        description="Powered by Shagldi Purliyew",
        terms_of_service="https://www.yourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'sliderpic', SliderPicApi)
router.register(r'newsapi', NewsApi)
router.register(r'agentsapi', AgentsApi)
router.register(r'imagesapi', ImagesApi)
router.register(r'tablesapi', TableApi)
router.register(r'permitables', PermiTableApi)
router.register(r'postapi', PostApi)
# router.register(r'sliderrrr', SliderPicApi123)

urlpatterns = i18n_patterns(

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #
    # path('SliderPicget/', SliderPicget),
    # path('SliderPicget/<int:pk>', SliderPicDetail),
    #
    # path('NewsGet/', NewsGet),
    # path('NewsGet/<int:pk>', NewsApiDetail),
    #
    # path('AgentsGet/', AgentsGet),
    # path('AgentsGet/<int:pk>', AgentsApiDetail),
    #
    # path('ImagesGet/', ImagesGet),
    # path('ImagesGet/<int:pk>', ImagesApiDetail),
    #
    # path('PermiTableGet/', PermiTableGet),
    # path('PermiTableGet/<int:pk>', PermiTableApiDetail),
    #
    # path('PostGet/', PostGet),
    # path('PostGet/<int:pk>', PostDetail),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    path('swagger(<format>.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    prefix_default_language=False
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL,
                                                                           document_root=settings.STATIC_ROOT)
