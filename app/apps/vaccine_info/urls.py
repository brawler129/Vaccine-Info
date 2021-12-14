from django.urls import path
from .views import VaccineInfoCreateFormView, VaccineInfoListView, VaccineInfoDeleteView

urlpatterns = [
    path('create', VaccineInfoCreateFormView.as_view(), name='add-vaccine-info'),
    path('list', VaccineInfoListView.as_view(), name='vaccine-info-list'),
    path('delete/<str:pk>', VaccineInfoDeleteView.as_view(), name='vaccine-info-delete')
]
