from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, null=True, blank=True)
    

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("product_variant")
        verbose_name_plural = ("product_variants")

    def __str__(self):
        return self.name



