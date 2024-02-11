from django.shortcuts import render
from requests import request 
from .models import Food
from .serializers import FoodSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class FoodAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    lookup_field = "id"
    authentication_classes= [TokenAuthentication, SessionAuthentication, BasicAuthentication]
  
    permission_classes = [IsAuthenticated]
    def get(self,request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request, id=None):
        return self.update(request, id)

    def delete(self,request,id=None):
        return self.destroy(request, id)
    