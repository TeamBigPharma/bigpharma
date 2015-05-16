from django.conf.urls import patterns, include, url
from . import views

from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns

urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^formulations/new', views.DrugFormulationCreateFormView.as_view(), name="formulation_create"),
    url(r'^formulations/(?P<pk>\d+)/edit', views.DrugFormulationUpdateFormView.as_view(), name="formulation_edit"),
    url(r'^formulations/(?P<pk>\d+)/$', views.DrugFormulationDetailView.as_view(), name="formulation_detail"),
    url(r'^formulations/$', views.DrugFormulationListView.as_view(), name="formulation_list"),
    url(r'^supplied_from/', views.SuppliedFromPharmacistCreateFormView.as_view(), name="supplied_from"),
)

urlpatterns += opatterns
