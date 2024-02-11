from django.db import models

# Create your models here.
class Food(models.Model):
    scale_values = [
        ("grams", "grams"),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(null= True, blank=True)
    calories = models.DecimalField(max_digits=200,decimal_places=2)
    cabohydrate = models.DecimalField(max_digits=200,decimal_places=2)
    protein = models.DecimalField(max_digits=200,decimal_places=2)
    fat = models.DecimalField(max_digits=200,decimal_places=2)
    measurement_scale = models.CharField(max_length=50, choices=scale_values)
    serving_size = models.CharField(max_length=200) 
    is_active = models.BooleanField(default=True, null=False, blank=False)
    
    def __str__(self):
        return self.name + '-->' + str(self.calories)
    