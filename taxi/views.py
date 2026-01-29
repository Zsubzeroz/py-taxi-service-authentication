from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin  # Correção: Espaços e quebra de linha
from django.contrib.auth.decorators import login_required

from .models import Driver, Car, Manufacturer


@login_required  # Correção: Dois espaços antes do comentário
def index(request):
    """View function for the home page of the site."""

    # Lógica do Contador de Visitas
    num_visits = request.session.get("num_visits", 0)  # Correção: Aspas duplas (Q000)
    num_visits += 1
    request.session["num_visits"] = num_visits  # Correção: Aspas duplas (Q000)

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits,  # Correção: Dois espaços antes do comentário
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):  # Correção: Dois espaços antes do comentário
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(LoginRequiredMixin, generic.ListView):  # Correção: Dois espaços antes do comentário
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):  # Correção: Dois espaços antes do comentário
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView):  # Correção: Dois espaços antes do comentário
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):  # Correção: Dois espaços antes do comentário
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
