from webpages import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="home"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("features",views.features,name="features"),
    path("calculater",views.calculater,name="calculater"),
    path("car",views.car,name="car"),

]
