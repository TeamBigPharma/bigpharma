from django.contrib import admin

from models import (
    DrugFormulation,
    Practitioner,
    Supplier,
    SuppliedFromPharmacist,
    ReceivedByPharmacist,
    AdhocAdjustment,
)


admin.site.register(DrugFormulation)
admin.site.register(Practitioner)
admin.site.register(Supplier)
admin.site.register(SuppliedFromPharmacist)
admin.site.register(ReceivedByPharmacist)
admin.site.register(AdhocAdjustment)
