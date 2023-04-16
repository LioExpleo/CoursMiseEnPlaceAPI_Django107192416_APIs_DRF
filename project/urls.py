from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryViewset, ProductViewset, ArticleViewset

router1 = routers.SimpleRouter()
router1.register('category', CategoryViewset, basename='category')

router2 = routers.SimpleRouter()
router2.register('product', ProductViewset, basename='product')

router3 = routers.SimpleRouter()
router3.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/', include(router1.urls)),
    path('api/', include(router2.urls)),
    path('api/', include(router3.urls)),
    #path('api/product/', ProductView.as_view()),
]
# 'api/category/' correspond à l'affichage dans le navigateur
# CategoryView.as_view() correspond à CategoryView dans le views sous shop
