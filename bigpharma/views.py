from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import SuppliedFromPharmacist, DrugFormulation
from django.core.urlresolvers import reverse_lazy


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
	pass

class AdhocAdjustmentCreateFormView(CreateView):
	pass
