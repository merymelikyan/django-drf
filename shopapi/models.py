from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title_hy = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Կատեգորիա"
        verbose_name_plural = "Կատեգորիաներ"

    def __str__(self):
        return self.title_hy


class Product(models.Model):
    title_hy = models.CharField(
        max_length=255,
        verbose_name="Հայերեն Վերնագիր։"
    )
    title_ru = models.CharField(
        max_length=255,
        verbose_name="Ռուսերեն Վերնագիր։"
    )
    title_en = models.CharField(
        max_length=255,
        verbose_name="Անգլերեն Վերնագիր։"
    )

    description_hy = CKEditor5Field(
        config_name="extends",
        verbose_name="Հայերեն Նկարագրություն:"
    )
    description_ru = CKEditor5Field(
        config_name="extends",
        verbose_name="Ռուսերեն Նկարագրություն:"
    )
    description_en = CKEditor5Field(
        config_name="extends",
        verbose_name="Անգլերեն Նկարագրություն:"
    )

    image = models.ImageField(
        upload_to="products/",
        verbose_name="Գլխավոր նկար:",
        blank=True,
        null=True
    )
    slug = models.SlugField(unique=True, verbose_name="Ցուցիչ:")
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)
    reviews_qty = models.IntegerField(default=0)
    stars_qty = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    class Meta:
        verbose_name = "Ապրանք"
        verbose_name_plural = "Ապրանքներ"

    def __str__(self):
        return self.title_hy


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Ապրանքի Նկարներ։"
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Ապրանքի նկար:",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Ապրանքի Նկար"
        verbose_name_plural = "Ապրանքի Նկարներ"

    def __str__(self):
        return self.product.title_hy