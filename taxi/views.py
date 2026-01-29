from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Driver, Car, Manufacturer


@login_required
def index(request):
    """View function for the home page of the site."""

    # Lógica do Contador de Visitas
    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(
    LoginRequiredMixin, generic.ListView
):  # Quebra de linha para E501
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(
    LoginRequiredMixin, generic.ListView
):  # Quebra de linha para E501
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(
    LoginRequiredMixin, generic.DetailView
):  # Quebra de linha para E501
    model = Car


class DriverListView(
    LoginRequiredMixin, generic.ListView
):  # Quebra de linha para E501
    model = Driver
    paginate_by = 5


class DriverDetailView(
    LoginRequiredMixin, generic.DetailView
):  # Quebra de linha para E501
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    ```


---

### 2. Configuração Refatorada de URLs (`taxi_service/urls.py`)

Quebrando as definições
de
`path`
para
ficar
abaixo
de
79
caracteres:

```python
# Em taxi_service/urls.py (ou o nome do seu diretório de configurações)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # URLs de Autenticação (Usando nomes de URL com hífens)
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="taxi/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout"
    ),

    # Incluir URLs do app
    path("", include("taxi.urls")),
]
