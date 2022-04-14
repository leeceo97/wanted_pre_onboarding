from rest_framework import serializers
from products.models import Product, Sponsor


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'target_amount',
            'deadline',
            'one_time_funding_amount',
        )

    def create(self, validated_data):
        validated_data["publisher"] = self.context.get("request").user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print('ss')
        data = self.context.get('request').data
        target_amount = data.get('target_amount', None)
        if instance.target_amount != target_amount:
            raise serializers.ValidationError('목표금액은 수정할수 없습니다.')
        return super().update(instance, validated_data)

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
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
            'id',
            'title',
            'publisher_name',
            'total_amount',
            'target_amount',
            'achievement_rate',
            'description',
            'd_day',
            'sponsor_count',
        )

class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'sponsor',
            'product',
        )
        read_only_fields = (
            'sponsor',
            'product',
        )
    def create(self, validated_data):
        validated_data["sponsor"] = self.context.get("request").user
        validated_data["product_id"] = self.context.get("pk")
        return super().create(validated_data)