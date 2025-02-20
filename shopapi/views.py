from rest_framework import generics

from shopapi.models import Category, Product, Subscriber
from shopapi.serializers import CategorySerializer,  ProductSerializer, SubscriberSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SubscriberAPIView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer