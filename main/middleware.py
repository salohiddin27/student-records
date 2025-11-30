from django.http import HttpResponse

def custom_404(request, exception):
    return HttpResponse("Natog'ri URl yozding baraka topgur ", status=404)