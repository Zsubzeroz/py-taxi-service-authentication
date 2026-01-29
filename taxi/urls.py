from django.urls import path
from . import views

# Nota: Como as views são protegidas com LoginRequiredMixin,
# você não precisa de @login_required aqui, exceto para a 'index' (FBV).

urlpatterns = [
    path("", views.index, name="index"),
    path("drivers/", views.DriverListView.as_view(), name="drivers"),
    path("drivers/<int:pk>", views.DriverDetailView.as_view(), name="driver-detail"),
    path("cars/", views.CarListView.as_view(), name="cars"),
    path("cars/<int:pk>", views.CarDetailView.as_view(), name="car-detail"),
    path(
        "manufacturers/",
        views.ManufacturerListView.as_view(),
        name="manufacturers"
    ),
]
