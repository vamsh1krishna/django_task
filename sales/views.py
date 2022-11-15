from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Products,Category
from .serializers import ProductSerializer,CategorySerializer,ProductSearchSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(APIView):
    serializer_class = ProductSerializer
    
    def get(self,request):
        product = request.query_params.get('product')
        products = Products.objects.filter(product=product)
        serializer = ProductSerializer(products,many=True)
        data = serializer.data
        return Response({'status':'success','results':data})
        

class ProductPostSearch(APIView):
    def post(self,request):
        searchserializer = ProductSearchSerializer(data=request.data)
        if searchserializer.is_valid():
            product = searchserializer.data['product']
            products = Products.objects.filter(product=product)[:5]
            serializer = ProductSerializer(products,many=True)
            data = serializer.data
            return Response({'status':'success','results':data})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


