from django import forms

from bigpharma.models import (
    SuppliedFromPharmacist,
    ReceivedByPharmacist,
    AdhocAdjustment,
)

class DrugFormulationForm(forms.ModelForm):
	pass

class SuppliedFromPharmacistForm(forms.ModelForm):
	pass

class ReceivedByPharmacistForm(forms.ModelForm):
	pass

class AdhocAdjustmentForm(forms.ModelForm):
	pass


class SupplyCancellationForm(forms.ModelForm):
    class Meta:
        model = SuppliedFromPharmacist
        fields = ('cancellation_reason',)

class ReceiveCancellationForm(forms.ModelForm):
    class Meta:
        model = ReceivedByPharmacist
        fields = ('cancellation_reason',)

class AdHocCancellationForm(forms.ModelForm):
    class Meta:
        model = AdhocAdjustment
        fields = ('cancellation_reason',)
