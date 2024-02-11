from django.urls import path 
from .views import FoodAPIView

urlpatterns = [ 
    path('generic/food/', FoodAPIView.as_view()),
    path('generic/food/<int:id>/', FoodAPIView.as_view()),
]
