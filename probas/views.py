from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer
import uuid

import logging

# Create your views here.

@csrf_exempt
def decode(request):
    if request.method == 'GET':
        probas = Person.objects.all()
        serializer = PersonSerializer(probas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        
        logging.basicConfig(level=logging.NOTSET) # Here
        logging.debug("---------------------------------")
        logging.info("DATOS")
        logging.info(request.FILES['picture'])
        logging.info("----------------------------------")
        
        Person(picture = request.FILES['picture']).save()
        
        data = {"status": "OK"}
        return JsonResponse(data)
        
        #data = JSONParser().parse(request)
        #serializer = PersonSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer.errors, status=400)