from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from .models import SuppliedFromPharmacist, DrugFormulation, ReceivedByPharmacist, AdhocAdjustment, Practitioner
from . import serializers


class ReadAndCreateModelViewSet(
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass


class DrugFormulationViewSet(ReadAndCreateModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.DrugFormulationSerializer
    queryset = DrugFormulation.objects.all()


class SuppliedFromPharmacistViewSet(ReadAndCreateModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)

    def create(self, request):
        request.data['pharmacist'] = request.user.id
        return super(SuppliedFromPharmacistViewSet, self).create(request)

    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.SuppliedFromPharmacistUpdateSerializer
        return serializers.SuppliedFromPharmacistSerializer

    queryset = SuppliedFromPharmacist.objects.all()


class ReceivedByPharmacistViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.ReceivedByPharmacistUpdateSerializer
        return serializers.ReceivedByPharmacistSerializer

    queryset = ReceivedByPharmacist.objects.all()


class AdhocAdjustmentViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.AdhocAdjustmentUpdateSerializer
        return serializers.AdhocAdjustmentSerializer


class PractitionerViewSet(ReadAndCreateModelViewSet):
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
