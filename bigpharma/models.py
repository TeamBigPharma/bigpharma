"""
bigpharma models.
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils import timezone

from opal import models as opal_models

User = get_user_model()

class Demographics(opal_models.Demographics):
        address = models.TextField(blank=True, null=True)
        
class Location(opal_models.Location): pass
class Allergies(opal_models.Allergies): pass
class Diagnosis(opal_models.Diagnosis): pass
class PastMedicalHistory(opal_models.PastMedicalHistory): pass
class Antimicrobial(opal_models.Antimicrobial): pass
class Investigation(opal_models.Investigation): pass


class Drug(models.Model):
        name = models.CharField(max_length=200, primary_key=True)

	def __unicode__(self):
                return self.name


class DrugFormulation(models.Model):
        STATE_CHOICES = (
                ('powder', 'powder',),
                ('liquid', 'liquid',),
                ('tablets', 'tablets',),
                ('amp', 'amp',),
        )

	UNIT_CHOICES = (
                ('mg', 'mg',),
                ('mcg', 'mcg',),
                ('g', 'g',),
                ('ml', 'ml',),
                ('l', 'l',),
        )

	amount = models.IntegerField(blank=True, null=True)
        units = models.CharField(choices=UNIT_CHOICES, max_length=200)
        state = models.CharField(choices=STATE_CHOICES, max_length=200)
        drug = models.ForeignKey(Drug)
        custom_name = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
                if self.custom_name:
                        return self.custom_name
                else:
                        return u'{} - {}{}'.format(self.drug, self.amount, self.units)

	def get_absolute_url(self):
                return reverse('formulation_detail', args=[self.pk])

	def get_stock(self):
                quantity_in = ReceivedByPharmacist.objects.filter(cancelled=False, formulation=self).aggregate(models.Sum('amount'))['amount__sum'];
                quantity_out = SuppliedFromPharmacist.objects.filter(cancelled=False, formulation=self).aggregate(models.Sum('amount'))['amount__sum'];
                adjustments = AdhocAdjustment.objects.filter(cancelled=False, formulation=self).aggregate(models.Sum('amount'))['amount__sum'];

                return (quantity_in or 0) - (quantity_out or 0) + (adjustments or 0)

	def get_stock_units(self):
                if self.amount:
                        # e.g. we are counting in tablets of a certain size
                        return self.state
                else:
                        # we don't know a unit size, so this is continuous, i.e. we are measuring directly in the units
                        return self.units

class Practitioner(models.Model):
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        title = models.CharField(max_length=200)

	def __unicode__(self):
                return u' '.join([self.title, self.first_name, self.last_name])


class BaseFormulationModel(models.Model):
        formulation = models.ForeignKey(DrugFormulation)
        amount = models.IntegerField()
        cancelled = models.BooleanField(default=False)

	# datetime is the datetime recorded by the user
        datetime = models.DateTimeField(default=timezone.now)

	# created is the datetime stamp on the serverp
        created = models.DateTimeField(auto_now_add=True)
        pharmacist = models.ForeignKey(User)

	class Meta:
                abstract=True

                
class Supplier(opal_models.LocatedModel):
        name = models.CharField(max_length=200)	
        
	def __unicode__(self):
                return self.name


class SuppliedFromPharmacist(BaseFormulationModel):
        # when you're giving a one to many formulations to a patient/nurse to take away
        authorising_practitioner = models.ForeignKey(Practitioner,
                                                     related_name="authorised_supplies",
                                                     blank=True, null=True)
        supplied_individual = models.CharField(max_length=200)
        ward = models.CharField(max_length=200, blank=True, null=True)
        collected_by_patient = models.BooleanField(default=False)
        patient = models.ForeignKey(opal_models.Patient, blank=True, null=True)

	def __unicode__(self):
                return u'{} {} supplied to {}'.format(
                        self.amount, self.formulation, self.supplied_individual)


class ReceivedByPharmacist(BaseFormulationModel):
        # when an external supplier brings in drugs
        supplier = models.ForeignKey(Supplier)

	def __unicode__(self):
                return u'{} {} received from {}'.format(
                        self.amount, self.formulation, self.supplier)


class AdhocAdjustment(BaseFormulationModel):
        ''' if the system is out, allow an adhoc adjustment '''
        reason_for_error = models.TextField()

