from django.shortcuts import render
from django.views import View

from .forms import ApartmentForm
from .models import Apartment, Manager
from .services import ApartmentService
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomeView(View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ApartmentsView(View):
    template_name = 'main/apartments.html'

    def get(self, request, *args, **kwargs):
        apartments_list = ApartmentService.get_apartment()
        return render(request, self.template_name, {'apartments_list': apartments_list})


class ManagersView(View):
    template_name = 'main/managers.html'

    def get(self, request, *args, **kwargs):
        managers_list = Manager.objects.all()
        return render(request, self.template_name, {'managers_list': managers_list})


class ApartmentEditView(UpdateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'main/apartment_edit.html'
    success_url = reverse_lazy('apartments')


class ApartmentDeleteView(DeleteView):
    model = Apartment
    template_name = 'main/apartment_confirm_delete.html'
    success_url = reverse_lazy('apartments')
