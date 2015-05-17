from rest_framework import serializers
from .models import SuppliedFromPharmacist, DrugFormulation, ReceivedByPharmacist, AdhocAdjustment, Practitioner


class DrugFormulationSerializer(serializers.ModelSerializer):
#    name = serializers.RelatedField(source='drug')
    
    class Meta:
        model = DrugFormulation


class SuppliedFromPharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliedFromPharmacist


class ReceivedByPharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedByPharmacist


class AdhocAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdhocAdjustment


class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
