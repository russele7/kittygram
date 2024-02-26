from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.authtoken import views

from cats.views import (
    # cat_list,
    # cat_detail,

    # APICat,
    # APICatDetail,

    # CatList,
    # CatDetail,

    CatViewSet,
    OwnerViewSet,
    LightCatViewSet,
)

router = DefaultRouter() 
router.register('cats', CatViewSet, basename='opa')
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
   # VIEW-ФУНКЦИИ
   # path('cats/', cat_list),
   # path('cats/<int:pk>/', cat_detail),

   # VIEW-КЛАССЫ
   # path('cats/', APICat.as_view()),
   # path('cats/<int:pk>/', APICatDetail.as_view())

   # VIEW-КЛАССЫ ДЖЕНЕРИКИ
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view())

   # VIEWSETS
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
    
    #    path('api-token-auth/', views.obtain_auth_token),

    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]
