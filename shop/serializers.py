from rest_framework.serializers import ModelSerializer
#1 import du ModelSerialiser de rest_framework

from shop.models import Category, Product, Article
#2 import de class Category du modèle

#3 Construction du Serializers
class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']
