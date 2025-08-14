from rest_framework import generics, status
from rest_framework.views import APIView     
from rest_framework.response import Response 
from .models import Country, Category
from .serializers import CountrySerializer, CategorySerializer, UserSerializer 
from decimal import Decimal 
from django.contrib.auth.models import User
import requests 
from django.conf import settings
import json 
import os
from rest_framework.permissions import IsAuthenticated

class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        queryset = Country.objects.all()
        search_term = self.request.query_params.get('search', None)
        if search_term is not None:
            queryset = queryset.filter(country_name__icontains=search_term)
        return queryset
    
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        country_id = self.request.query_params.get('country_id', None)
        if country_id is None:            
            return Category.objects.none()

        queryset = Category.objects.filter(country_id=country_id)
        
        search_term = self.request.query_params.get('search', None)
        if search_term is not None:
            queryset = queryset.filter(category_title__icontains=search_term)
            
        return queryset


class CalculateFreightView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        country_id = request.data.get('country_id')
        category_id = request.data.get('category_id')
        destination_id = request.data.get('destination_id')
        weight_str = request.data.get('weight')

        if not all([country_id, category_id, destination_id, weight_str]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            country = Country.objects.get(id=country_id)
            category = Category.objects.get(id=category_id, country=country)
            weight = Decimal(weight_str)
        except (Country.DoesNotExist, Category.DoesNotExist):
            return Response({"error": "Invalid Country or Category"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "Invalid weight format"}, status=status.HTTP_400_BAD_REQUEST)
     
        
        international_price = weight * category.price_kg
        
        domestic_price = Decimal(75000) 
        destination_name = f"Kota Tujuan (ID: {destination_id})"

        total_price = international_price + domestic_price


        response_data = {
            "origin": country.country_name,
            "destination": destination_name,
            "category_name": category.category_title,
            "international_price": international_price,
            "domestic_price": domestic_price,
            "total_price": total_price
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
class DestinationCityListView(APIView):

    permission_classes = [IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('search', '').lower()

        if not search_term:
            return Response([], status=status.HTTP_200_OK)

        try:
            file_path = os.path.join(settings.BASE_DIR, 'freight', 'data', 'cities.json')
            
            with open(file_path, 'r', encoding='utf-8') as f:
                all_cities = json.load(f)

            filtered_cities = [
                city for city in all_cities 
                if search_term in city['city_name'].lower()
            ]
            
            return Response(filtered_cities[:20], status=status.HTTP_200_OK)

        except FileNotFoundError:
            return Response({"error": "City data file not found on server."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": f"An error occurred on server: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []