from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import SuppliedFromPharmacist, DrugFormulation, ReceivedByPharmacist, AdhocAdjustment, Practitioner
from . import serializers


class DrugFormulationViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.DrugFormulationSerializer
    queryset = DrugFormulation.objects.all()


class SuppliedFromPharmacistViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.SuppliedFromPharmacistSerializer
    queryset = SuppliedFromPharmacist.objects.all()


class ReceivedByPharmacistViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.ReceivedByPharmacistSerializer
    queryset = ReceivedByPharmacist.objects.all()    


class AdhocAdjustmentViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.AdhocAdjustmentSerializer
    queryset = AdhocAdjustment.objects.all()    


class PractitionerViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.PractitionerSerializer
    queryset = Practitioner.objects.all()  


class SupplyToWardViewSet(viewsets.ViewSet):
    base_name = 'supply_to_ward'

    def create(self, request):
        # {u'date': u'06/05/2015', u'product': u'Morphine 400 mg', u'collector': u'David', u'ward_name': u't8', u'quantity': u'97809'}        
        print request.data
        return Response('DONE')

class DrugFormulationCreateFormView(CreateView):
    model = DrugFormulation


class DrugFormulationUpdateFormView(UpdateView):
    model = DrugFormulation


class DrugFormulationDetailView(DetailView):
    model = DrugFormulation


class DrugFormulationListView(ListView):
    model = DrugFormulation


class SuppliedFromPharmacistCreateFormView(CreateView):
    model = SuppliedFromPharmacist


class ReceivedByPharmacistCreateFormView(CreateView):
    model = ReceivedByPharmacist


class AdhocAdjustmentCreateFormView(CreateView):
    model = AdhocAdjustment
