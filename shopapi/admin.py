from django.contrib import admin

from .models import (
    Category,
    Product,
    ProductImages,
    Subscriber
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title_hy", "title_ru", "title_en", "slug"]
    list_display_links = ["title_hy", "title_ru", "title_en"]
    list_filter = ["title_hy", "title_ru", "title_en"]
    prepopulated_fields = {"slug": ["title_en"]}


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id", "title_hy", "title_ru",
        "title_en", "slug", "reviews_qty", "stars_qty",
        "price", "available", "hidden"
    ]
    list_display_links = ["title_hy", "title_ru", "title_en"]
    list_filter = [
        "title_hy", "title_ru",
        "title_en", "category",
        "reviews_qty", "price",
        "available", "hidden",
    ]
    list_editable = [
        "reviews_qty", "stars_qty",
        "price", "available", "hidden"
    ]
    search_fields = [
        "title_hy", "title_ru", "title_en",
        "description_hy", "description_ru", "description_en"
    ]
    prepopulated_fields = {"slug": ["title_en"]}
    inlines = [ProductImagesInline]


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "created"]
    list_display_links = ["name", "email"]
    search_fields = ["name", "email"]
    list_filter = ["name", "created"]