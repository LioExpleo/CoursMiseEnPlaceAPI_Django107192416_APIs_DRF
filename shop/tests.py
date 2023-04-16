from django.urls import reverse_lazy # permet de déterminer l'url des endpoint à tester
from rest_framework.test import APITestCase # API test de base django

from shop.models import Category # import du modèle Category



class ShopAPITestCase(APITestCase):

        def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères (format de l’api)
            return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


# Ecriture de la class de test :
class TestCategory(ShopAPITestCase):
    # stockage de l’url de l'endpoint dans un attribut de classe pour pouvoir l’utiliser plus facilement dans
    # chacun de nos tests
    url = reverse_lazy('category-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères (format de l’api)
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
       # Créons deux catégories dont une seule est active
       category = Category.objects.create(name='Fruits55', active=True)
       Category.objects.create(name='Légumes55', active=False)

       # On réalise l’appel en GET en utilisant le client de la classe de test
       response = self.client.get(self.url) # méthode http de l'url
       # Nous vérifions que le status code est bien 200 (succès)
       # et que les valeurs retournées sont bien celles attendues
       self.assertEqual(response.status_code, 200)

       expected = [
           {
               #'date_created': self.format_datetime(category.date_created),
               #'date_updated': self.format_datetime(category.date_updated),
               'id': category.id,
               'name': category.name,
           }
       ]
       x='excepted'
       # expected.pop()
       expected.append(x)
       #del expected[2]

       x='response'
       resp = response.json()
       resp.append(x)
       self.assertEqual(resp, expected)

    def test_create(self):
        # Nous vérifions qu’aucune catégorie n'existe avant de tenter d’en créer une
        self.assertFalse(Category.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouvelle catégorie'})
        # Vérifions que le status code est bien en erreur et nous empêche de créer une catégorie
        self.assertEqual(response.status_code, 405)
        # Enfin, vérifions qu'aucune nouvelle catégorie n’a été créée malgré le status code 405
        self.assertFalse(Category.objects.exists())
