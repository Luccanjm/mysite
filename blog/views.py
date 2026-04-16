from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello_post(request):
    return HttpResponse("Hello World")