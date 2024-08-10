from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Snippets.serializers import SnippetsSerializers
from .models import Snippets


@csrf_exempt
def snippets_list(request):

    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetsSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


def snippets_detail(request, pk):

    try:
        snippet = Snippets.objects.get(id=pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetsSerializers(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetsSerializers(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)