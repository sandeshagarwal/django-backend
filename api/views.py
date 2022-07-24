from django.shortcuts import render
from django.http import JsonResponse
#from sqlalchemy import false

from rest_framework.decorators import api_view
from rest_framework.response import Response
#from yaml import serialize

from .models import carSales
from .serializers import carSalesSerializer

# Create your views here.
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/sales-list/',
#         'Detail View':'/sales-details/<str:pk>/',
#         'Create':'/add-sales/',
#         'Update':'/update-sales/<str:pk>/',
#         'Delete':'/delete-sales/<str:pk>/',
#     }
#     return Response(api_urls)


@api_view(['GET'])
def carSalesList(request):
        sales = carSales.objects.all()
        serializer = carSalesSerializer(sales, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def carDetailsbysales_id(request,pk):
        sales = carSales.objects.get(sales_id=pk)
        serializer = carSalesSerializer(sales, many = False)
        return Response(serializer.data)

@api_view(['GET'])
def carDetailsbycustomer_id(request,pk):
        sales = carSales.objects.get(customer_id=pk)
        serializer = carSalesSerializer(sales, many = False)
        return Response(serializer.data)

@api_view(['POST'])
def carSalesCreate(request):
        serializer = carSalesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def carSalesUpdate(request,pk):
        sale = carSales.objects.get(customer_id=pk)
        serializer = carSalesSerializer(instance=sale,data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def carSalesDelete(request,pk):
        sale = carSales.objects.get(customer_id=pk)
        sale.delete()
        return Response("Item successfully deleted !")

