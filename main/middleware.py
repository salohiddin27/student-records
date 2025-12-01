from django.http import HttpResponse

def custom_404(request, exception):
    return HttpResponse("qise ", status=404)

def custom_400(request, exception):
    return HttpResponse("Noto‘g‘ri so‘rov ", status=400)

def custom_401(request, exception):
    return HttpResponse("foydalanuvchi tizimga kirishi kerak ", status=401)

def custom_403(request, exception):
    return HttpResponse("Ruxsat yo‘q (taqiqlangan) ", status=403)

def custom_405(request, exception):
    return HttpResponse("Bu HTTP method ruxsat etilmagan (masalan GET o‘rniga POST ishlatildi) ", status=405)

def custom_408(request, exception):
    return HttpResponse("So‘rov muddati tugadi (server javob bera olmadi) ", status=408)

