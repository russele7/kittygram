from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import generics
from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer, CatListSerializer


# VIEW-SETS
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # Пишем метод, а в декораторе разрешим работу со списком объектов
    # и переопределим URL на более презентабельный
    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        # Нужны только последние пять котиков белого цвета
        cats = Cat.objects.filter(color='White')[:5]
        # Передадим queryset cats сериализатору 
        # и разрешим работу со списком объектов
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data) 

    def get_serializer_class(self):
        # Если запрошенное действие (action) — получение списка объектов ('list')
        if self.action == 'list':
            # ...то применяем CatListSerializer
            return CatListSerializer
        # А если запрошенное действие — не 'list', применяем CatSerializer
        return CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

#######################################################

# Собираем вьюсет, который будет уметь изменять или удалять отдельный объект.
# А ничего больше он уметь не будет.


class UpdateDeleteViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass

# CreateModelMixin — создать объект (для обработки запросов POST);
# ListModelMixin — вернуть список объектов (для обработки запросов GET);
# RetrieveModelMixin — вернуть объект (для обработки запросов GET);
# UpdateModelMixin — изменить объект (для обработки запросов PUT и PATCH);
# DestroyModelMixin — удалить объект (для обработки запросов DELETE).


class CreateRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    # В теле класса никакой код не нужен! Пустячок, а приятно.
    pass


class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


#####################################################################


# В классе ViewSet есть шесть предопределённых методов:
# list(self, request) — для получения списка объектов из queryset;
# create(self, request) — для создания объекта в модели;
# retrieve(self, request, pk=None) — для получения определённого объекта из queryset;
# update(self, request, pk=None) — для перезаписи (полного обновления) определённого объекта из queryset;
# partial_update(self, request, pk=None) — для частичного обновления объекта из queryset;
# destroy(self, request, pk=None) — для удаления одного из объектов queryset.


# class CatViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Cat.objects.all()
#         serializer = CatSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Cat.objects.all()
#         cat = get_object_or_404(queryset, pk=pk)
#         serializer = CatSerializer(cat)
#         return Response(serializer.data) 

###################################################

# # VIEW-ФУНКЦИИ
# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def cat_detail(request, pk):
#     cat = Cat.objects.get(pk=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     serializer = CatSerializer(cat)
#     return Response(serializer.data)


# # VIEW-КЛАССЫ
# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# class APICatDetail(APIView):
#     def get(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         serializer = CatSerializer(cat)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         serializer = CatSerializer(cat, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# # VIEW-КЛАССЫ ДЖЕНЕРИКИ
# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


