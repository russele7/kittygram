from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter

from cats.views import (
    cat_list,
    cat_detail,

    APICat,
    APICatDetail,

    CatList,
    CatDetail,

    CatViewSet,
)

router = DefaultRouter() 
router.register('cats', CatViewSet) 

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
   path('', include(router.urls)),
]

