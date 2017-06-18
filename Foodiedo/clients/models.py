from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        ordering = ('id',)


class Order(models.Model):
    status = models.ForeignKey(Status)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return 'Order {}'.format(self.pk)

    class Meta:
        ordering = ('id',)
