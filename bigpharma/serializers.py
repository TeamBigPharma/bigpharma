from rest_framework import serializers
from .models import SuppliedFromPharmacist, DrugFormulation, ReceivedByPharmacist, AdhocAdjustment, Practitioner


class DrugFormulationSerializer(serializers.ModelSerializer):
#    name = serializers.RelatedField(source='drug')
    stock = serializers.SerializerMethodField()
    
    class Meta:
        model = DrugFormulation

    def get_stock(self, obj):
        return '{} {}'.format(obj.get_stock(), obj.get_stock_units())


class SuppliedFromPharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliedFromPharmacist


class SuppliedFromPharmacistUpdateSerializer(SuppliedFromPharmacistSerializer):
    """
    Update serializer - only allow 'cancelled' to be updated.
    """
    class Meta:
        model = SuppliedFromPharmacist
        fields = ('cancelled',)


class ReceivedByPharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedByPharmacist


class ReceivedByPharmacistUpdateSerializer(SuppliedFromPharmacistSerializer):
    """
    Update serializer - only allow 'cancelled' to be updated.
    """
    class Meta:
        model = ReceivedByPharmacist
        fields = ('cancelled',)


class AdhocAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdhocAdjustment


class AdhocAdjustmentUpdateSerializer(serializers.ModelSerializer):
    """
    Update serializer - only allow 'cancelled' to be updated.
    """
    class Meta:
        model = AdhocAdjustment
        fields = ('cancelled',)


class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
