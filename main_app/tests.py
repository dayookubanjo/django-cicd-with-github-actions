from django.test import TestCase
from .models import Food

# Create your tests here.
class ModelTests(TestCase):

    def setUp(self):
        self.new_food = Food.objects.create(
            name = 'Potato',
            description = 'Irish Potato',
            calories = 135.68,
            cabohydrate = 32.5,
            protein = 0.96,
            fat = 2.54,
            measurement_scale = 'grams',
            serving_size = '100 grams'
            )
        
    def test_food_model(self):
        data = self.new_food
        #Check that new_food is an instance of Food
        self.assertTrue(isinstance(data, Food))
        self.assertEqual(str(data), 'Potato-->135.68')