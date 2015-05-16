from django.conf.urls import patterns, include, url
from . import views

from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^formulations/', views.DrugFormulationCreateFormView.as_view(), name="drug_formulation"),
    url(r'^supplied_from/', views.SuppliedFromPharmacistCreateFormView.as_view(), name="supplied_from"),
)

urlpatterns += opatterns
