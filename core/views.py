from django.http import HttpResponse, JsonResponse

def homePage(request):
    return HttpResponse("<h1>This is home page</h1>")

def jsonTest(request):
    return JsonResponse({"name": "Ilia", "age": 19})
    
