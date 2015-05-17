from django.conf.urls import patterns, include, url
from django.contrib import admin
from opal.core.api import OPALRouter
from . import views

admin.autodiscover()

from opal.urls import urlpatterns as opatterns

router = OPALRouter()
router.register(r'supply_to_ward', views.SupplyToWardViewSet)
router.register(r'drug_formulation', views.DrugFormulationViewSet)
router.register(r'supplied_from_pharmacist', views.SuppliedFromPharmacistViewSet)
router.register(r'received_by_pharmacist', views.ReceivedByPharmacistViewSet)
router.register(r'adhoc_adjustment', views.AdhocAdjustmentViewSet)
router.register(r'practitioner', views.PractitionerViewSet)


urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^formulations/new', views.DrugFormulationCreateFormView.as_view(), name="formulation_create"),
    url(r'^formulations/(?P<pk>\d+)/$', views.DrugFormulationDetailView.as_view(), name="formulation_detail"),
    url(r'^formulations/$', views.DrugFormulationListView.as_view(), name="formulation_list"),
    url(r'^transactions/(?P<formulation>\d+)/$', views.TransactionListView.as_view(), name="transactions_list"),
    url(r'^inventory/$', views.DrugFormulationListView.as_view(), name="inventory"),
    url(r'^supplied_from/$', views.SuppliedFromPharmacistCreateFormView.as_view(), name="supplied_from"),
    url(r'^supplied_from/(?P<pk>\d+)/cancel', views.CancelSuppliedFromPharmacistView.as_view(), name="supplied_from_cancel"),
    url(r'^received_by/(?P<pk>\d+)/cancel', views.CancelReceivedByPharmacistView.as_view(), name="received_by_cancel"),
    url(r'^ad_hoc/(?P<pk>\d+)/cancel', views.CancelAdHocAdjustmentView.as_view(), name="ad_hoc_cancel"),
    url(r'^api/', include(router.urls)),
)


urlpatterns += opatterns
