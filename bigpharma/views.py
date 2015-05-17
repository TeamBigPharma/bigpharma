from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import SuppliedFromPharmacist, DrugFormulation, ReceivedByPharmacist, AdhocAdjustment, Practitioner
from . import serializers


class DrugFormulationViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.DrugFormulationSerializer
    queryset = DrugFormulation.objects.all()


class SuppliedFromPharmacistViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.SuppliedFromPharmacistSerializer
    queryset = SuppliedFromPharmacist.objects.all()


class ReceivedByPharmacistViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.ReceivedByPharmacistSerializer
    queryset = ReceivedByPharmacist.objects.all()    


class AdhocAdjustmentViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.AdhocAdjustmentSerializer
    queryset = AdhocAdjustment.objects.all()    


class PractitionerViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.PractitionerSerializer
    queryset = Practitioner.objects.all()  


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
