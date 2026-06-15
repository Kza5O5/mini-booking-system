from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "project": "Mini Booking System API",
        "status": "running"
    })


def health_check(request):
    return JsonResponse({
        "status": "healthy"
    })