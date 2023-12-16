from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import JsonResponse
import json
from django.core.files.storage import default_storage
from rest_framework.response import Response
from rest_framework.views import APIView


from django.db import connection

def get_product_details(request):
    with connection.cursor() as cursor:
        cursor.callproc("GetProductDetails")
        results = cursor.fetchall()
        data = [{'product_name': row[0],'product_brand':[1],'product_category':[2],'product_subcategory':row[3], 'product_description': row[4] ,'product_price':[5] } for row in results]
    return JsonResponse(data, safe=False)


# @csrf_exempt
# def Api(request, id=0):
#     if request.method == 'GET':
#         if id == 0:
#             person = Person.objects.all()
#             person_serializer = PersonSerializer(person, many=True)
#             return JsonResponse(person_serializer.data, safe=False)
#         else:
#             person = Person.objects.filter(Id=id)
#             person_serializer = PersonSerializer(person, many=True)
#             response = JsonResponse(person_serializer.data, safe=False)
#             response_data = json.loads(response.content)
#             if not response_data:
#                 return JsonResponse("NO DATA FOUND",safe=False)
#             else:
#                 return JsonResponse(person_serializer.data, safe=False)
            


#     elif request.method == 'POST':
#         person_data = JSONParser().parse(request)
#         person_serializer = PersonSerializer(data=person_data)
#         if person_serializer.is_valid():
#             person_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add")

#     elif request.method == 'PUT':
#         person_data = JSONParser().parse(request)
#         person = Person.objects.get(Id = person_data['Id'])
#         person_serializer = PersonSerializer(person, data=person_data)
#         if person_serializer.is_valid():
#             person_serializer.save()
#             return JsonResponse("Update Successful",safe=False)
#         return JsonResponse("Failed to Update")

#     elif request.method == "DELETE":
#         person = Person.objects.get(Id=id)
#         person.delete()
#         return JsonResponse("Deleted Successfully", safe=False)
