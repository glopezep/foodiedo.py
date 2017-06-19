from rest_framework import serializers

from .models import Product, Category, Status, Order


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'category_id', ]


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True,
    #     queryset=Product.objects.all(),
    # )
    # products = ProductSerializer(many=True)
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        source='status'
    )

    class Meta:
        model = Order
        fields = ['id', 'status', 'status_id', 'products', ]
