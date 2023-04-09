from rest_framework.views import APIView #4 pour APIView
from rest_framework.response import Response # pour APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Category, Product #5 import du modèle Category
from shop.serializers import CategorySerializer, ProductSerializer #5 import serialisers créé

class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(active=True)

class ProductView(APIView):
    def get(self, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

