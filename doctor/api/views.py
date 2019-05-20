from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from doctor.models import Doctor,Specialization,Emergency,DoctorType
from .serializers import *
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView,FlatMultipleModelAPIView

class DoctorList(generics.ListCreateAPIView):
  queryset = Doctor.objects.all()
  serializer_class = ListSerializer

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Doctor.objects.all()
  serializer_class = ListSerializer



@api_view(['GET', 'POST'])
def ddoctorList(request):
    """
 List  customers, or create a new customer.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Doctor.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = PListSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = PListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def ddoctorDetails(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        customer = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DetailSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DetailSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST'])
def Type(request):
    """
 List  customers, or create a new customer.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = DoctorType.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = TypeSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def DType(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        customer = DoctorType.objects.get(pk=pk)
    except DoctorType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TypeSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TypeSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
 