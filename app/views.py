from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(request):
    # 1~49
    numbers = random.sample(range(1, 50), 6)
    numbers = sorted(numbers)
    # numbers = " ".join([str(n) for n in numbers])
    numbers = " ".join(map(str, numbers))

    spec_number = random.randint(1, 49)
    result = {"numbers": numbers, "spec_numbers": spec_number}
    return render(request, "lotto.html", result)
    # return JsonResponse(result)


# Create your views here.
def hello(request):
    result = {
        "message": "測試",
        "data": 123,
    }
    # return HttpResponse("<h1>hello</h1>")
    return JsonResponse(result)
