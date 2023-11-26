from django.urls import path
from .views import ApartmentsView, ManagersView, HomeView, ApartmentEditView, ApartmentDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('apartments/', ApartmentsView.as_view(), name='apartments'),
    path('apartments/<int:pk>/edit/', ApartmentEditView.as_view(), name='apartment_edit'),
    path('apartments/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='apartment_delete'),
    path('managers/', ManagersView.as_view(), name='managers'),
]
