from rest_framework import serializers
from reviewproduct.models import ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ('id','productID', 'customerID', 'review_at','review','starreview')
