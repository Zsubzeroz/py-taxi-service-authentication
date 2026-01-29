from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin # NOVO: Importação para proteção de CBV
from django.contrib.auth.decorators import login_required # NOVO: Importação para proteção de FBV

from .models import Driver, Car, Manufacturer


@login_required # NOVO: Protege a view de função (FBV)
def index(request):
    """View function for the home page of the site."""

    # --- INÍCIO: Lógica do Contador de Visitas ---
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    # --- FIM: Lógica do Contador de Visitas ---

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits, # NOVO: Adicionado ao contexto
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView): # NOVO: Adicionado LoginRequiredMixin
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(LoginRequiredMixin, generic.ListView): # NOVO: Adicionado LoginRequiredMixin
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView): # NOVO: Adicionado LoginRequiredMixin
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView): # NOVO: Adicionado LoginRequiredMixin
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView): # NOVO: Adicionado LoginRequiredMixin
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
