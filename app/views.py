from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def hello(request):
    result = {
        "message": "測試",
        "data": 123,
    }
    # return HttpResponse("<h1>hello</h1>")
    return JsonResponse(result)
