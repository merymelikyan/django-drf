from rest_framework import serializers
from shopapi.models import Category, Product, Subscriber


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title_hy", "title_ru", "title_en", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "title_hy",
            "title_ru",
            "title_en",
            "description_hy",
            "description_ru",
            "description_en",
            "image",
            "category",
            "slug",
            "price",
            "created",
            "updated",
            "available",
            "hidden",
        ]
        
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"