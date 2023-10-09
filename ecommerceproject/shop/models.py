from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    Description = models.TextField(blank=True)
    Image = models.ImageField(upload_to='category', blank=True)
    class Meta:
        ordering = ('Name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
            return '{}'.format(self.Name)

class Product(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    Description = models.TextField(blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="product/", blank=True)
    Stock = models.IntegerField()
    Available = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('Name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def get_url(self):
            return reverse('shop:prodCatDetail', args=[self.category.slug, self.slug])
    def __str__(self):
            return '{}'.format(self.Name)