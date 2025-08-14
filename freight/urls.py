from django.urls import path
from .views import CountryListView, CategoryListView, CalculateFreightView,  DestinationCityListView, UserRegistration

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('calculate-freight/', CalculateFreightView.as_view(), name='calculate-freight'),
    path('destinations/', DestinationCityListView.as_view(), name='destination-list'),
    path('register/', UserRegistration.as_view(), name='user-register'),
]