from django.urls import path

from AppCoder import views

urlpatterns = [
    
    path('', views.inicio, name= "Inicio"), #esta era nuestra primer view
    path('vegan', views.vegan, name="Vegan"),
    path('vegetarian', views.vegetarian, name="Vegetarian"),
    path('meats', views.meats, name="Meats"),
    path('glutenFree', views.glutenFree, name="Gluten Free"),
    path('veganFormulario', views.veganFormulario, name="VeganFormulario"),
    path('vegetarianFormulario', views.vegetarianFormulario, name="VegetarianFormulario"),
    path('meatsFormulario', views.meatsFormulario, name="MeatsFormulario"),
    path('glutenFreeFormulario', views.glutenFreeFormulario, name="GlutenFreeFormulario"),
    path('busquedaVegetariano', views.busquedaVegetariano, name="BusquedaVegetariano"),
    path('busquedaVegano', views.busquedaVegano, name="BusquedaVegano"),
    path('busquedaMeats', views.busquedaMeats, name="BusquedaMeats"),
    path('busquedaGlutenFree', views.busquedaGlutenFree, name="BusquedaGlutenFree"),
    path('resultadoVegetariano', views.buscarVegetariano),
    path('resultadoVegano', views.buscarVegano),
    path('resultadoMeats', views.buscarMeats),
    path('resultadoGlutenFree', views.buscarGlutenFree),
] 

