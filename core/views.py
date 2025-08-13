from django.http import HttpResponse

def homePage(request):
    return HttpResponse("<h1>This is home page</h1>")