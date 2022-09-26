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
        
        p = Person(picture = request.FILES['picture']).save()
        
        logging.basicConfig(level=logging.NOTSET) # Here
        logging.debug("---------------------------------")
        logging.info("DATOS")
        logging.info(p)
        logging.info("----------------------------------")
        
        data = {"status": "OK"}
        return JsonResponse(data)