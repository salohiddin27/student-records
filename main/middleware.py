import json
import time

from django.http import JsonResponse


class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return JsonResponse({"qise": "bunday url yoq"})
        return response


class Custom400Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        started = time.time()
        response = self.get_response(request)
        ended = time.time()
        if response.status_code == 400:
            body = {
                "xatolik": "nimadir",
                "elapsed_time": round(ended - started, 3),
                "content": json.loads(response.content.decode())
            }
            return JsonResponse(body, status=400)
        return response
