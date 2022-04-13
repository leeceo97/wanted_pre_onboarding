from rest_framework import serializers
from products.models import Product, Sponsor


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'publisher',
            'description',
            'target_amount',
            'deadline',
            'one_time_funding_amount',
        )

    def create(self, validated_data):
        validated_data["publisher"] = self.context.get("request").user
        return super().create(validated_data)

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'publisher_name',
            'total_amount',
            'target_amount',
            'achievement_rate',
            'd_day'
        )

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'publisher_name',
            'total_amount',
            'target_amount',
            'achievement_rate',
            'description',
            'd_day',
            'sponsor_count',
        )