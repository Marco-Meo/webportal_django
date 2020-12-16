from rest_framework import serializers
from faq.models import Faq

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "api:faq-detail"}
        }