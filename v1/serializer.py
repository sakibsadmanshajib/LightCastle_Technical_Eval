
from rest_framework import serializers
from .models import OutputData

"""
Serializer for OutputData model
"""
class OutputDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OutputData
        fields = (
            'sl',
            'timestamp',
            'transaction_at',
            'product',
            'qty',
            'price',
            'side',
            'acct',
            'group'
        )