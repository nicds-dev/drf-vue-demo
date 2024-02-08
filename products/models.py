from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products/', default='default.jpg', verbose_name='Image')
    name = models.CharField(max_length=255, verbose_name='Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name='Price'
        )
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name