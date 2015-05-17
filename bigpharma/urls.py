from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views

admin.autodiscover()

from opal.urls import urlpatterns as opatterns

router = DefaultRouter()
router.register(r'drug_formulation', views.DrugFormulationViewSet)
router.register(r'supplied_from_pharmacist', views.SuppliedFromPharmacistViewSet)
router.register(r'received_by_pharmacist', views.ReceivedByPharmacistViewSet)
router.register(r'adhoc_adjustment', views.AdhocAdjustmentViewSet)
router.register(r'practitioner', views.PractitionerViewSet)


urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^formulations/new', views.DrugFormulationCreateFormView.as_view(), name="formulation_create"),
    url(r'^formulations/(?P<pk>\d+)/edit', views.DrugFormulationUpdateFormView.as_view(), name="formulation_edit"),
    url(r'^formulations/(?P<pk>\d+)/$', views.DrugFormulationDetailView.as_view(), name="formulation_detail"),
    url(r'^formulations/$', views.DrugFormulationListView.as_view(), name="formulation_list"),
    url(r'^supplied_from/', views.SuppliedFromPharmacistCreateFormView.as_view(), name="supplied_from"),
    url(r'^api/', include(router.urls)),
)

urlpatterns += opatterns
